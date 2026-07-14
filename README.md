# Enterprise Customer Churn Predictor & Retention Pipeline

## 🎯 Business Context & Objective
Customer churn directly impacts operational revenue metrics within the telecommunications sector. This system transitions away from static analytical execution models to deliver an end-to-end, production-grade Machine Learning engine. 

The pipeline segments subscriber accounts across an enterprise-mapped relational database, handles feature preprocessing with data-leakage boundaries, trains a classification engine achieving **82% test accuracy (64% Churn F1-Score)**, and instantly serves real-time retention offer strategies through a microservice backend API linked to a user-facing dashboard.

---

## 🏗️ Technical Architecture
The application layout isolates data storage, processing machinery, and inference serving:
1. **Relational Database Layer (SQLite):** Normalizes subscriber data records across three separate relational schemas (`demographics`, `services`, and `billing_accounts`) utilizing foreign key integrity and secondary join indexing.
2. **Preprocessing Pipeline (Scikit-Learn):** Encapsulates feature preprocessing using a modular `ColumnTransformer` to enforce robust categorical one-hot encoding and data scaling without data leakage.
3. **Microservice Serving Layer (FastAPI):** Exposes a `/predict` endpoint that processes incoming structured JSON payloads, executes mathematical inference, and maps results to dynamic retention actions.
4. **Interactive Dashboard (Gradio):** Provides a visual user panel with real-time sliders and inputs allowing team managers to evaluate account risk factors on the fly.

---

## 📊 Core Data Insights (EDA)
* **The Lifespan Danger Zone:** Customers who churn exhibit a mean tenure of **18 months**, compared to **37.5 months** for stable accounts. The first 1.5 to 2 years represent the critical customer retention window.
* **Product Infrastructure Core Driver:** **69.4%** of all customer attrition occurs among users subscribed to high-cost **Fiber optic** services, indicating a strong correlation between baseline plan rates and churn risk.

---

## 🚀 Local Installation & Execution

1. Clone the project structure and install the dependencies:
```bash
git clone [https://github.com/yourusername/customer-churn-retention-pipeline.git](https://github.com/yourusername/customer-churn-retention-pipeline.git)
cd customer-churn-retention-pipeline
pip install -r requirements.txt
