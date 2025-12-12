# DSA20: Data Mining & Data Warehousing Project

This repository contains my complete submission for the DSA 2040 FS 2025 End Semester Practical Exam.

It is organized exactly by the exam sections and tasks, with runnable scripts, SQL, generated datasets, database files, and exported visuals.


📁 Folder Structure
```
DSA2040a_practical_exam_Nelisa_347/
├── DataMining/
│   ├── preprocessing_iris.py
│   ├── clustering_iris.py
│   ├── mining_iris_basket.py
│   ├── clustering_iris_r.pdf
│   ├── preprocessing_r.pdf
│   ├── images/
│   │   ├── boxplot_outliers.png
│   │   ├── cluster_scatter.png
│   │   └── correlation_heatmap.png
│   │   └──elbow_curve.png
│   │   └──pairplot_iris.png
│   
├── DataWarehousing/
│   ├── etl_retail.ipynb
│   ├── retail_dw.db
│   ├── schema.sql
│   ├── olap_queries.sql
│   ├── OLAP_query_re.pdf
│   ├── images/
│   │   ├── star_schema.png
│   │   ├── sales_by_country.png
└── README.md
```
# Task 1: Data Warehouse Design
## STAR SCHEMA

The diagram is located in the images folder in the data wrehousing folder

Fact Table: sales

Dimension Tables: date, product, customer, store

## Why Star Schema Instead of Snowflake?

The star schema is chosen because it is simpler, denormalized, and optimized for fast OLAP queries, which is ideal for analytical workloads. It reduces the number of joins, improving query performance and making the structure easier for business users to understand. A snowflake schema adds normalization and complexity, which is unnecessary for this dataset and would slow down aggregation queries.

## Snippet of schema.sql
```
-- DIMENSION TABLES

CREATE TABLE dim_product (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    category TEXT NOT NULL,
    brand TEXT,
    unit_price REAL
);

CREATE TABLE dim_customer (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gender TEXT,
    age INTEGER,
    location TEXT
);

CREATE TABLE dim_time (
    time_id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    day INTEGER,
    month INTEGER,
    quarter INTEGER,
    year INTEGER
);
```

**There are two main processes performed**

Data Warehousing: ETL pipeline, star schema design, OLAP SQL queries, and visual analytics on synthetic retail data.

Data Mining: Classification, clustering, and association rule mining using the Iris dataset and synthetic market basket data.


Each section includes code, reports, and visual outputs to demonstrate technical proficiency and analytical insight.

# Task 2: ETL Process Implementation 
Extracted synthetic retail data.

Transformed and loaded into SQLite (retail_dw.db).

Script: etl_retail.ipynb.

## A snippet of the generation
```
# 0. Synthetic data generation
# -------------------------------------------------------------------
def generate_synthetic_data(n_rows: int = 1000) -> pd.DataFrame:
    """
    Generate synthetic retail invoice-like data.
    Columns: InvoiceNo, InvoiceDate, CustomerID, Country, ProductID,
             Quantity, UnitPrice.
    """
    logging.info("Generating synthetic data with %d rows...", n_rows)

    if HAS_FAKER:
        fake = Faker()
        Faker.seed(42)
    np.random.seed(42)
```
# Task 3: OLAP QUERIES
. Key OLAP operations include:

Drill Down: Navigate from summarized data to more detailed data (e.g., from year to quarter to month).

Roll Up: Aggregate data by climbing up a hierarchy or by reducing dimensions, summarizing detailed data into higher-level summaries.

Slice: Select a single dimension value to filter the data cube.

## Visualizations

![Sales by Country](DataWarehousing/images/sales_by_country.png)


# Section 2 :Data Mining

## Preprocessing

The Iris dataset was cleaned and prepared for analysis using Python. The preprocessing steps included:

- Handling missing values (none present in Iris, but checks were performed)

- Normalizing numerical features using StandardScaler

- Encoding class labels where necessary

- Splitting the dataset into training and testing sets

All preprocessing steps were implemented in preprocessing_iris.py to ensure reproducibility.

## Classification

Two supervised learning models were trained to classify Iris species:

**Models Used**

- Decision Tree Classifier

- K‑Nearest Neighbors (KNN)

Evaluation Metrics

Each model was evaluated using:

- Accuracy

- Precision

- Recall

- F1‑score

The decision tree structure was visualized using sklearn.tree.plot_tree, showing how features such as petal length and petal width drive classification decisions.

## Clustering

Applied KMeans and DBSCAN on Iris.

Visualized clusters with PCA.

## Association Rule Mining

Synthetic market basket data (40 transactions) was generated to demonstrate association rule mining.

Method

- Apriori algorithm from the mlxtend library

- min_support = 0.2

- min_confidence = 0.5

Outputs

Rules were sorted by lift, revealing strong associations such as:

- {milk} → {bread}

This suggests potential bundling or recommendation strategies in a retail context.

## Setup Instructions

## Requirements

Python 3.8+

Libraries: scikit-learn, pandas, matplotlib, mlxtend, sqlite3

## Installation
```
pip install -r requirements.txt
```


