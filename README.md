# AFRO-EXPRESS EVENTS

## Data Analysis, Customer Segmentation, and Strategic Insights

This repository contains a complete data analysis and machine-learning
workflow conducted for Afro-Express Events. The goal was to transform
raw ticket sales data into actionable insights, segment the customer
base, and provide strategic recommendations that improve ticket
conversions, marketing efficiency, and overall event profitability.

------------------------------------------------------------------------

## Table of Contents

1.  Project Overview
2.  Key Findings & Behavioral Insights
3.  Customer Segmentation (KMeans)
4.  Strategic Recommendations
5.  Technical Stack & Repository Structure
6.  Setup & Execution
7.  Contact

------------------------------------------------------------------------

## 1. Project Overview

Afro-Express events attract a loyal, culturally engaged audience, but
purchasing behavior is highly time-sensitive, with the majority of sales
occurring very close to event dates. The core purpose of this analysis
was to:

-   Understand **when and how** customers buy tickets\
-   Classify customers into **high-impact segments** using KMeans\
-   Deliver **strategic recommendations** for higher conversions\
-   Build **email automation tools** for targeted engagement

------------------------------------------------------------------------

## 2. Key Findings & Behavioral Insights

The analysis uncovered strong patterns in purchase timing and buyer
behavior.

### Behavioral Insights Summary

  -----------------------------------------------------------------------
  Insight Category                          Key Finding
  ----------------------------------------- -----------------------------
  **Average Purchase Timing**               Customers buy **5 days
                                            before** the event

  **Last-Minute Sales**                     **50% of sales occur the
                                            night before / day of event**

  **Time of Day**                           Highest activity: **Evening
                                            (40%)**, **Afternoon (30%)**

  **Top Locations**                         Austin, Houston, Dallas, San
                                            Antonio (Texas)

  **Demographics**                          Balanced gender mix;
                                            Afro-diasporic audience
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 3. Customer Segmentation (KMeans)

KMeans clustering grouped attendees into three actionable segments:

### Cluster Summary

  -------------------------------------------------------------------------
  Cluster     Description    Purchase Behavior     Recommended Strategy
  ----------- -------------- --------------------- ------------------------
  **Cluster   Early Planners Buys \~14 days before Early-bird discounts,
  0**                        event                 exclusive access

  **Cluster   Last-Minute    Buys \<7 days before  Urgency messaging,
  1**         Buyers         event; spontaneous    countdown campaigns

  **Cluster   Group /        Highest per-order     Group deals, VIP
  2**         High-Value     spend                 upgrades, loyalty perks
              Buyers                               
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 4. Strategic Recommendations

### 1. Optimize Pricing by Timing

Introduce tiered pricing with increases **5--7 days before the event**
to encourage earlier purchases.

### 2. Personalized Outreach

Use cluster-specific promotions, such as: - Early-bird deals for Cluster
0\
- Urgency messaging for Cluster 1\
- Group-ticket/VIP offers for Cluster 2

### 3. Strengthen Cultural Messaging

Highlight community, Afro-vibes, and cultural celebration---core
motivators for the audience.

### 4. Retention & Loyalty

Reward frequent attendees to reduce acquisition costs and grow lifetime
value.

------------------------------------------------------------------------

## 5. Technical Stack & Repository Structure

### Technology Stack

-   **Language:** Python\
-   **Libraries:** pandas, numpy, matplotlib, seaborn, plotly.express\
-   **ML Tools:** scikit-learn (KMeans, PCA, silhouette_score)\
-   **Email Automation:** smtplib, email.mime

### Repository Files

  -------------------------------------------------------------------------
  File                     Description
  ------------------------ ------------------------------------------------
  **AFRO-EXPRESS.ipynb**   Main notebook: cleaning, EDA, clustering,
                           visualizations

  **AFRO-EXPRESS           Detailed analytical documentation
  DOCUMENTATION.pdf**      

  **RECOMMENDATION &       Strategic summary and execution plan
  STRATEGY.pdf**           

  **email_AT.py**          Automated HTML email sender for all clusters

  **testemail.py**         Test version of email script
  -------------------------------------------------------------------------

------------------------------------------------------------------------

## 6. Setup & Execution

### 1. Clone Repository

``` bash
git clone <repository-url>
```

### 2. Install Dependencies

``` bash
pip install pandas numpy scikit-learn matplotlib seaborn NameGenderPredictor
```

### 3. Prepare Data

-   Place the raw Excel file (e.g., Orders\_....xlsx) in the correct
    folder\
-   Update the path in `AFRO-EXPRESS.ipynb`

### 4. Run the Notebook

``` bash
jupyter notebook
```

Running the notebook will: - Clean the dataset\
- Generate cluster labels\
- Output processed CSV files

### 5. Email Automation

Update credentials in `email_AT.py`:

``` python
SENDER_EMAIL = "your_email"
SENDER_PASSWORD = "your_app_password"
```

Run:

``` bash
python email_AT.py
```

------------------------------------------------------------------------

## 7. Contact

For inquiries, collaborations, or consulting opportunities:\
**Developer:** Jay
