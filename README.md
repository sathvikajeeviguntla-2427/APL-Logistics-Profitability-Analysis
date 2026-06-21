# APL Logistics Customer, Product & Profitability Performance Analysis

## Project Overview

This project analyzes customer profitability, product performance, discount impact, and market-level profitability in supply chain operations using transactional data from APL Logistics.

The objective is to identify high-value customers, profitable product categories, discount-driven margin erosion, and high-performing markets through Exploratory Data Analysis (EDA) and an interactive Streamlit dashboard.

---

## Business Problem

Organizations often focus on revenue growth without understanding the profitability drivers behind sales.

This can lead to:

* Revenue growth with declining profit margins
* Excessive discounting strategies
* Loss-making customers and product categories
* Poor pricing decisions
* Inefficient market expansion strategies

The purpose of this project is to provide visibility into:

* Customer profitability
* Product and category performance
* Discount impact on margins
* Market and regional profitability
* Strategic business recommendations

---

## Project Objectives

### Customer Analysis

* Identify top and bottom customers by profit contribution
* Analyze customer segment performance
* Calculate customer value metrics

### Product Analysis

* Evaluate profitability by product category
* Identify high-revenue and high-margin categories
* Detect low-margin product groups

### Discount Analysis

* Measure the impact of discounts on profitability
* Identify discount ranges causing margin erosion
* Recommend optimal discount levels

### Market Analysis

* Compare profitability across markets and regions
* Analyze country-level performance
* Identify high-value markets

### Dashboard Development

* Build an interactive Streamlit dashboard
* Enable dynamic filtering and business insights
* Support executive decision-making

---

## Dataset Information

| Metric        | Value   |
| ------------- | ------- |
| Total Records | 180,519 |
| Features      | 45      |
| Customers     | 20,652  |
| Products      | 118     |
| Categories    | 50      |
| Markets       | 5       |

### Key Dataset Attributes

* Customer Information
* Product Information
* Sales Data
* Profit Data
* Discount Information
* Market Information
* Shipping Information

---

## Project Structure

APL_LOGISTICS_PROJECT/

├── .gitignore

├── README.md

├── requirements.txt

│

├── dashboard/

│ ├── app.py

│ └── cleaned_APL_Logistics.csv

│

├── data/

│ └── APL_Logistics.csv

│

├── notebooks/

│ └── APL_Logistics_Analysis.ipynb

│

├── outputs/

│ └── screenshots/

│

└── venv/

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Plotly
* Streamlit
* Matplotlib
* Seaborn

### Development Tools

* VS Code
* Jupyter Notebook
* Git
* GitHub

---

## Data Cleaning & Validation

The following preprocessing steps were performed:

### Missing Value Treatment

Handled missing values in:

* Customer Lname
* Customer Zipcode

### Duplicate Record Validation

* Duplicate Records Found: 0

### Financial Validation

Validated:

* Sales values
* Profit values
* Discount rates
* Order totals

Results:

* Negative Sales Records: 0
* Invalid Discount Records: 0
* Negative Order Totals: 0

---

## Feature Engineering

Additional business metrics were created:

### Customer Name

Combined Customer Fname and Customer Lname.

### Profit Margin %

Calculated using:

Profit Margin % = (Order Profit Per Order / Sales) × 100

### Discount %

Calculated using:

Discount % = Order Item Discount Rate × 100

### Shipping Delay

Calculated using:

Shipping Delay = Actual Shipping Days − Scheduled Shipping Days

### Discount Bucket

Orders were categorized into:

* 0–10%
* 10–20%
* 20–30%
* 30–40%
* 40%+

---

## Key Performance Indicators (KPIs)

| KPI              | Value          |
| ---------------- | -------------- |
| Total Revenue    | $36.78 Million |
| Total Profit     | $3.97 Million  |
| Profit Margin    | 10.78%         |
| Total Customers  | 20,652         |
| Total Products   | 118            |
| Total Categories | 50             |
| Total Markets    | 5              |

---

## Customer Analysis

### Top Customer

**Betty Spears**

### Customer Segment Performance

| Segment     | Revenue | Profit |
| ----------- | ------- | ------ |
| Consumer    | $19.09M | $2.07M |
| Corporate   | $11.17M | $1.20M |
| Home Office | $6.52M  | $0.69M |

### Insights

* Consumer segment generated the highest revenue and profit.
* Customer profitability varies significantly.
* High sales do not always imply high profitability.

---

## Product & Category Analysis

### Most Profitable Categories

* Fishing
* Cleats
* Camping & Hiking
* Cardio Equipment
* Women's Apparel

### Lowest Margin Categories

* Strength Training
* As Seen on TV!
* Men's Clothing
* Basketball
* Books

### Insights

* Fishing is the highest profit-generating category.
* Strength Training shows extremely low margins.
* Several categories generate revenue but contribute limited profit.

---

## Discount Impact Analysis

### Findings

* Profitability declines as discounts increase.
* Orders with 0–10% discounts generated the highest profitability.
* Higher discount levels contribute to margin erosion.

### Recommendation

Maintain discounts below 10% whenever possible.

---

## Market & Regional Analysis

### Top Countries by Profit

* United States
* France
* Mexico
* Germany
* Brazil

### Insights

* United States generated the highest revenue and profit.
* Brazil achieved strong profitability relative to revenue.
* Market performance varies significantly across regions.

---

## Streamlit Dashboard Features

### Revenue & Profit Overview

* KPI cards
* Revenue vs Profit visualization

### Customer Analytics

* Top customers
* Bottom customers
* Segment profitability

### Product Analytics

* Category profitability
* Margin analysis

### Market Analytics

* Market profitability
* Regional performance
* Country profitability

### Discount Analytics

* Discount bucket analysis
* Profit impact visualization

### Executive Summary

* Business recommendations
* Strategic insights

---

## Business Recommendations

### Customer Strategy

* Retain high-value customers.
* Investigate loss-making customers.
* Improve customer profitability tracking.

### Product Strategy

* Focus on Fishing and Cleats categories.
* Review low-margin categories.
* Optimize category pricing.

### Discount Strategy

* Maintain discounts below 10%.
* Avoid excessive discounting.
* Monitor margin erosion.

### Market Strategy

* Expand high-performing markets.
* Improve profitability in weaker regions.
* Optimize region-specific pricing.

---

## Conclusion

This project successfully transformed raw supply chain transaction data into actionable business intelligence. Through customer, product, discount, and market profitability analysis, the organization gains a deeper understanding of the factors driving financial performance.

The findings demonstrate that revenue alone is not an accurate measure of business success. By focusing on profitability, margin optimization, customer value, and market performance, organizations can make more informed strategic decisions and improve long-term business outcomes.

---

## How to Run the Project

### Clone Repository

git clone <repository-url>

### Install Dependencies

pip install -r requirements.txt

### Launch Dashboard

streamlit run dashboard/app.py

---

## Author

**Jeeviguntla Sathvika**

Computer Science Undergraduate
G. Pulla Reddy Engineering College (GPREC)

---

## License

This project was developed for educational and analytical purposes as part of the Unified Mentor Program.