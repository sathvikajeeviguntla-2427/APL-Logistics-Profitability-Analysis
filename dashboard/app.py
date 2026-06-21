import streamlit as st
import pandas as pd
import plotly.express as px

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="APL Logistics Profitability Dashboard",
    page_icon="📦",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

from pathlib import Path

@st.cache_data
def load_data():
    csv_path = Path(__file__).parent / "cleaned_APL_Logistics.csv"
    return pd.read_csv(csv_path, encoding="latin1")

df = load_data()
st.write("CSV Loaded Successfully")
st.write(df.shape)

# ==================================================
# FEATURE CHECKS
# ==================================================

if 'Customer Name' not in df.columns:
    df['Customer Name'] = (
        df['Customer Fname'].astype(str)
        + ' '
        + df['Customer Lname'].astype(str)
    )

if 'Profit Margin %' not in df.columns:
    df['Profit Margin %'] = (
        df['Order Profit Per Order']
        / df['Sales']
    ) * 100

if 'Discount Bucket' not in df.columns:
    df['Discount Bucket'] = pd.cut(
        df['Order Item Discount Rate'],
        bins=[0, 0.1, 0.2, 0.3, 0.4, 1],
        labels=[
            '0-10%',
            '10-20%',
            '20-30%',
            '30-40%',
            '40%+'
        ]
    )

# ==================================================
# TITLE
# ==================================================

st.title("📦 APL Logistics Profitability Intelligence Dashboard")

st.markdown("""
### Customer • Product • Market • Margin Analytics
Analyze customer profitability, product performance,
discount impact, and market profitability.
""")

# ==================================================
# SIDEBAR FILTERS
# ==================================================

st.sidebar.header("Filters")

segment = st.sidebar.selectbox(
    "Customer Segment",
    ["All"] + sorted(df["Customer Segment"].dropna().unique())
)

market = st.sidebar.selectbox(
    "Market",
    ["All"] + sorted(df["Market"].dropna().unique())
)

category = st.sidebar.selectbox(
    "Category",
    ["All"] + sorted(df["Category Name"].dropna().unique())
)

region = st.sidebar.selectbox(
    "Order Region",
    ["All"] + sorted(df["Order Region"].dropna().unique())
)

shipping_mode = st.sidebar.selectbox(
    "Shipping Mode",
    ["All"] + sorted(df["Shipping Mode"].dropna().unique())
)

# ==================================================
# APPLY FILTERS
# ==================================================

filtered_df = df.copy()

if segment != "All":
    filtered_df = filtered_df[
        filtered_df["Customer Segment"] == segment
    ]

if market != "All":
    filtered_df = filtered_df[
        filtered_df["Market"] == market
    ]

if category != "All":
    filtered_df = filtered_df[
        filtered_df["Category Name"] == category
    ]

if region != "All":
    filtered_df = filtered_df[
        filtered_df["Order Region"] == region
    ]

if shipping_mode != "All":
    filtered_df = filtered_df[
        filtered_df["Shipping Mode"] == shipping_mode
    ]

# ==================================================
# KPI SECTION
# ==================================================

total_revenue = filtered_df["Sales"].sum()
total_profit = filtered_df["Order Profit Per Order"].sum()

profit_margin = (
    (total_profit / total_revenue) * 100
    if total_revenue > 0 else 0
)

total_customers = filtered_df["Customer Id"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "💰 Revenue",
    f"${total_revenue:,.0f}"
)

col2.metric(
    "📈 Profit",
    f"${total_profit:,.0f}"
)

col3.metric(
    "📊 Profit Margin",
    f"{profit_margin:.2f}%"
)

col4.metric(
    "👥 Customers",
    f"{total_customers:,}"
)

st.divider()

# ==================================================
# REVENUE VS PROFIT
# ==================================================

st.subheader("📈 Revenue vs Profit")

kpi_df = pd.DataFrame({
    "Metric": ["Revenue", "Profit"],
    "Value": [total_revenue, total_profit]
})

fig = px.bar(
    kpi_df,
    x="Metric",
    y="Value",
    text="Value",
    title="Revenue vs Profit"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# CUSTOMER ANALYSIS
# ==================================================

st.subheader("🏆 Top 10 Customers By Profit")

top_customers = (
    filtered_df.groupby("Customer Name")
    ["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    top_customers,
    orientation="h",
    title="Top Customers"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# BOTTOM CUSTOMERS
# ==================================================

st.subheader("⚠️ Bottom 10 Customers By Profit")

bottom_customers = (
    filtered_df.groupby("Customer Name")
    ["Order Profit Per Order"]
    .sum()
    .sort_values()
    .head(10)
)

fig = px.bar(
    bottom_customers,
    orientation="h",
    title="Bottom Customers"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# CUSTOMER SEGMENT
# ==================================================

st.subheader("👥 Customer Segment Profitability")

segment_profit = (
    filtered_df.groupby("Customer Segment")
    ["Order Profit Per Order"]
    .sum()
    .reset_index()
)

fig = px.pie(
    segment_profit,
    values="Order Profit Per Order",
    names="Customer Segment",
    title="Profit Contribution by Segment"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# CATEGORY PROFITABILITY
# ==================================================

st.subheader("📦 Top Categories By Profit")

category_profit = (
    filtered_df.groupby("Category Name")
    ["Order Profit Per Order"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

fig = px.bar(
    category_profit,
    orientation="h",
    title="Top Categories"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# CATEGORY MARGIN
# ==================================================

st.subheader("📊 Category Margin Analysis")

category_margin = (
    filtered_df.groupby("Category Name")
    .agg({
        "Sales": "sum",
        "Order Profit Per Order": "sum"
    })
    .reset_index()
)

category_margin["Margin %"] = (
    category_margin["Order Profit Per Order"]
    / category_margin["Sales"]
) * 100

top_margin = category_margin.sort_values(
    "Margin %",
    ascending=False
).head(10)

fig = px.bar(
    top_margin,
    x="Category Name",
    y="Margin %",
    title="Top Categories by Margin"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# MARKET ANALYSIS
# ==================================================

st.subheader("🌎 Market Profitability")

market_profit = (
    filtered_df.groupby("Market")
    ["Order Profit Per Order"]
    .sum()
    .reset_index()
)

fig = px.bar(
    market_profit,
    x="Market",
    y="Order Profit Per Order",
    title="Profit by Market"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# REGION ANALYSIS
# ==================================================

st.subheader("🗺️ Regional Profitability")

region_profit = (
    filtered_df.groupby("Order Region")
    ["Order Profit Per Order"]
    .sum()
    .reset_index()
)

fig = px.bar(
    region_profit,
    x="Order Region",
    y="Order Profit Per Order",
    title="Profit by Region"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# COUNTRY ANALYSIS
# ==================================================

st.subheader("🌍 Top Countries by Profit")

country_profit = (
    filtered_df.groupby("Order Country")
    ["Order Profit Per Order"]
    .sum()
    .reset_index()
)

top_countries = country_profit.sort_values(
    "Order Profit Per Order",
    ascending=False
).head(10)

fig = px.bar(
    top_countries,
    x="Order Country",
    y="Order Profit Per Order",
    title="Top 10 Countries by Profit"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# DISCOUNT ANALYSIS
# ==================================================

st.subheader("🎯 Discount Impact")

discount_analysis = (
    filtered_df.groupby("Discount Bucket")
    ["Order Profit Per Order"]
    .sum()
    .reset_index()
)

fig = px.bar(
    discount_analysis,
    x="Discount Bucket",
    y="Order Profit Per Order",
    title="Profit by Discount Bucket"
)

st.plotly_chart(fig, use_container_width=True)

# ==================================================
# BUSINESS INSIGHTS
# ==================================================

st.subheader("📋 Business Insights")

top_customer = (
    filtered_df.groupby("Customer Name")
    ["Order Profit Per Order"]
    .sum()
    .idxmax()
)

top_category = (
    filtered_df.groupby("Category Name")
    ["Order Profit Per Order"]
    .sum()
    .idxmax()
)

top_market = (
    filtered_df.groupby("Market")
    ["Order Profit Per Order"]
    .sum()
    .idxmax()
)

st.info(f"""
🏆 Top Customer: {top_customer}

📦 Most Profitable Category: {top_category}

🌎 Strongest Market: {top_market}

💡 Recommended Discount Range: 0–10%

📈 Current Profit Margin: {profit_margin:.2f}%
""")

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.subheader("📋 Executive Summary")

st.success("""
• Total Revenue: $36.78M

• Total Profit: $3.97M

• Profit Margin: 10.78%

• Most Profitable Category: Fishing

• Best Customer Segment: Consumer

• Recommended Discount Range: 0–10%

• Strongest Market: United States
""")

# ==================================================
# DOWNLOAD BUTTON
# ==================================================

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="APL_Filtered_Data.csv",
    mime="text/csv"
)

# ==================================================
# DATASET PREVIEW
# ==================================================

st.subheader("📄 Dataset Preview")

st.write("Filtered Dataset Shape:", filtered_df.shape)

st.dataframe(filtered_df.head(20))

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.markdown(
    "APL Logistics Customer, Product & Profitability Analysis Dashboard"
)