# 🍽️ **Culinary Compass — F&B Analytics Dashboard**

### *Data-Driven Insights for Restaurant Performance, Conversion Optimization & Promo Strategy*

*By **Veman Shrinivas Chippa** — Making Data Speak.*

---

## 🚀 **Overview**

Culinary Compass is a **full-stack data analytics dashboard** designed for the Food & Beverage industry to analyze:

* Restaurant performance
* Menu-to-order conversion rates
* Area-wise insights
* Promo campaign prioritization
* Month-over-month revenue trends
* Strategic recommendations for growth

This dashboard was built as part of a **Business Analyst case study** and demonstrates my ability to combine:

✔ Data cleaning & engineering
✔ Business problem-solving
✔ KPI-driven storytelling
✔ UI/UX design for executive stakeholders
✔ Full web deployment using Streamlit

---

## 🎯 **Key Features**

### 📊 **1. Business Summary (Executive Overview)**

* Total Orders, GMV, Conversion Rate
* Top Area & Top Restaurant KPIs
* Monthly trends (Orders + GMV)
* Conversion funnel with insights
* Auto-adjusting based on filters

### 🏆 **2. Restaurant Performance**

* Top 5 restaurants by GMV
* Priority Matrix (High, Medium, Low)
* Promo recommendations for low-performing outlets
* Downloadable CSV reports

### 📍 **3. Area Insights**

* Area-wise conversion & order performance
* Dual-axis charts (Orders vs Conversion %)
* Full structured table for deeper analysis

### 🎯 **4. Promo Strategy**

* Automatically flags restaurants needing promotions
* Uses conversion thresholds (<10% is HIGH priority)
* Business-friendly explanation for CEO visibility

### 🔁 **5. Conversion Optimization Strategy**

Includes my recommended strategies backed by real data:

* Menu simplification
* Smart upsell positioning
* Targeted discounts
* Combo deals
* Personalized recommendations

### ℹ️ **6. About**

A complete project story, tech stack, and scope for future enhancements.

---

## 🛠️ **Tech Stack**

| Layer                              | Tools Used                                           |
| ---------------------------------- | ---------------------------------------------------- |
| **Data Cleaning & Transformation** | Python, Pandas, NumPy                                |
| **Modeling & Business Logic**      | Feature engineering, MoM growth, conversion analysis |
| **Visualization**                  | Plotly (line, bar, dual-axis, funnel charts)         |
| **Web App Framework**              | Streamlit                                            |
| **Design / UI**                    | Custom CSS, Gradient Themes, Inter Font              |
| **Deployment**                     | Streamlit Cloud / Local Deployment                   |
| **Extras**                         | CSV Export, PDF Summary (optional), Priority Badges  |

---

## 🧠 **Business Logic Highlights**

### 🟢 **Conversion Rate Calculation**

```
conversion_rate = TOTAL_ORDERS / MENU_SESSIONS
```

### 🟠 **Priority Classification**

| Priority   | Condition              | Meaning                       |
| ---------- | ---------------------- | ----------------------------- |
| **High**   | Conversion < 10%       | Needs immediate promo         |
| **Medium** | 10% ≤ Conversion < 14% | Consider occasional campaigns |
| **Low**    | ≥ 14%                  | Healthy performance           |

### 🔵 **Top Restaurants by GMV**

Last 3 months (or filtered month) identified using aggregated GMV.

### 🟣 **Area Insights**

Dual-axis chart to visualize demand (orders) vs efficiency (conversion).

---

## 🧩 **Project Structure**

```
📁 culinary_compass_dashboard/
│
├── app.py                # Main Streamlit application
├── clean_case_study.csv  # Cleaned dataset used for analysis
├── requirements.txt      # Dependencies
│
└── assets/
      └── logo.jpeg       # Branding icon
```

---

## 📦 **How to Run Locally**

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/iveman99/culinary_compass_dashboard.git
cd culinary_compass_dashboard
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # (Mac/Linux)
.venv\Scripts\activate      # (Windows)
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the App

```bash
streamlit run app.py
```

---

## 🌟 **Key Results & Business Impact**

✔ Identified **high-priority restaurants** requiring promotional campaigns
✔ Mapped **area-wise demand** to focus expansion efforts
✔ Designed **conversion funnel** to evaluate customer drop-off
✔ Delivered **data-driven actionable recommendations**
✔ Built an intuitive dashboard for **CEO-level decision-making**

---

## 🔮 **Scope for Future Enhancements**

* Real-time API integration
* Predictive conversion & sales forecasting
* Customer segmentation using ML
* Automated promo simulation engine
* Benchmarking across competitors
* A/B testing impact visualization
* Role-based restricted dashboards

---

## 💛 **Author**

**Veman Shrinivas Chippa**
*Data Analyst • Business Analyst • Dashboard Developer*

🔗 **Portfolio:** [https://iveman.vercel.app](https://iveman.vercel.app)
🔗 **LinkedIn:** [https://www.linkedin.com/in/veman-chippa](https://www.linkedin.com/in/veman-chippa)
🔗 **GitHub:** [https://github.com/iveman99](https://github.com/iveman99)

---

## 📌 **Important Note**

This dashboard is built using a **sample dataset** provided for a business case study.
All insights, strategies, and recommendations are generated based on this dataset and may vary with real business data.

---

## ⭐ **If you like this project, please star the repository!**

Your support motivates me to build more analytical and business intelligence tools.
