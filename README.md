# 🧭 **Culinary Compass — F&B Insights & Analytics Dashboard**

*A professional, CEO-grade analytics platform built to transform raw F&B data into strategic decisions.*

---

## 🌐 **Live Dashboard**

🚀 **Try the full interactive dashboard here:**
👉 **[https://iveman-fb-analytics-dashboard.streamlit.app/](https://iveman-fb-analytics-dashboard.streamlit.app/)**

---

# 👤 **User Story — How This Project Was Created**

### **📌 The Problem**

Most F&B brands struggle with:

* Low menu-to-order conversion
* Scattered sales data
* No structured visibility of which restaurants perform well
* No framework to prioritize promotional efforts
* Difficulty understanding GMV trends, area performance, and outlet-level insights

CEOs and operations teams often rely on manual Excel sheets and gut-feeling decisions — leading to missed revenue opportunities.

---

## **📌 My Vision**

I wanted to build a **professional-grade F&B intelligence system** that:

* Centralizes all brand, area, and monthly data
* Clearly highlights *where the business is losing money*
* Guides strategic, data-driven decisions
* Looks premium, feels premium, and works seamlessly across devices
* Can be used directly by founders, growth teams, marketing heads, or outlet managers

The goal was simple:
👉 *Convert data into clarity. Convert clarity into action.*

---

## **📌 The Journey (End-to-End Story)**

### **1️⃣ Understanding the Business Metrics**

Before writing a single line of code, I mapped out key F&B KPIs:

* Total Orders
* GMV
* Menu Opens
* Conversion Rate
* AOV (Average Order Value)
* Top Areas & Top Brands
* Priority Score for promo planning

This became the foundation of the dashboard.

---

### **2️⃣ Cleaning & Preparing Real-World F&B Data**

Inside Jupyter Notebook, I:

* Parsed dates
* Fixed null GMV values
* Created **month_year** dimension
* Engineered **conversion_rate**
* Aggregated brand-level and area-level performance
* Validated data consistency

This transformed raw CSV into business-ready intelligence.

---

### **3️⃣ Designing the Dashboard Structure**

After analyzing common pain points, I created **6 modules**:

#### ✔ Business Summary

The CEO’s at-a-glance control center.

#### ✔ Restaurant Performance

Conversion-based outlet ranking + Top 5 GMV chart.

#### ✔ Area Insights

Area-wise contribution, conversions & trends.

#### ✔ Promo Strategy

Color-coded priority mapping for campaign planning.

#### ✔ Conversion Strategy

Expert recommendations based on data patterns.

#### ✔ About & Methods

A transparent breakdown of methodology + project story.

---

### **4️⃣ Creating a Premium Brand Identity (Navy + Gold)**

Inspired by luxury hospitality dashboards:

* Navy blue = Trust, stability
* Gold = Premium, insights, leadership

Every element (buttons, KPIs, charts, badges, layout) was designed to look like a product that a **Fortune 500 F&B company** would proudly use.

---

### **5️⃣ Building a Seamless User Experience**

I implemented:

* Fully responsive KPI cards
* Glassmorphism cards
* Dual-axis charts
* A conversion funnel
* Downloadable CSV
* Smart sidebar filtering
* Page-level navigation
* Smooth layout spacing
* Professional typography (Inter font)
* Custom CSS for a brand-grade feel

---

### **6️⃣ Deploying to Production**

Finally, I deployed the entire system to **Streamlit Cloud**, making it accessible globally:

👉 [https://iveman-fb-analytics-dashboard.streamlit.app/](https://iveman-fb-analytics-dashboard.streamlit.app/)

This is now a polished, professional-ready F&B analytics application.

---

# ✨ **Key Features**

### 🟦 **1. Business Summary (CEO Dashboard)**

* KPI Cards: Orders, GMV, Conversion, Top Area, Top Brand
* Monthly Trend Graph (Orders + GMV)
* Conversion Funnel
* Performance Snapshot

---

### 🟦 **2. Restaurant Performance**

* Top 5 Restaurants (GMV-based)
* Month-based filtering
* Priority Matrix (High / Medium / Low conversions)
* Beautiful restaurant badge system
* CSV export

---

### 🟦 **3. Area Insights**

* Area-wise orders
* Conversion %
* Comparison graph
* Interactive data table

---

### 🟦 **4. Promo Strategy**

Shows where promos matter most using:

* Smart priority rules
* High-priority outlet detection (<10%)
* Strategic recommendations

---

### 🟦 **5. Conversion Strategy (Consultant Grade)**

Data-backed recommendations including:

* Menu redesign
* Personalized suggestions
* Conversion uplift boosters
* A/B test structures

---

### 🟦 **6. About + Scope of Improvement**

Includes:

* Project story
* Tech stack
* Core business insights
* Improvement opportunities
* Important note on data-dependency

---

# 🔧 **Tech Stack**

| Area           | Tools                 |
| -------------- | --------------------- |
| **Language**   | Python                |
| **Framework**  | Streamlit             |
| **Analysis**   | Pandas, NumPy         |
| **Charts**     | Plotly                |
| **Styling**    | HTML, CSS, Inter font |
| **Deployment** | Streamlit Cloud       |

---

# 📁 **Project Structure**

```
📦 culinary-compass-dashboard  
│  
├── app.py                # Full Streamlit app  
├── clean_case_study.csv  # Dataset  
├── assets/               # Logo & static files  
├── requirements.txt      # Dependencies  
└── README.md             # Documentation  
```

---

# 🚀 Running Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/iveman99/culinary-compass-dashboard.git
cd culinary-compass-dashboard
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Launch Application

```bash
streamlit run app.py
```

---

# 📈 Impact & Business Value

✔ Identifies revenue bottlenecks
✔ Highlights low-performing restaurants
✔ Enables targeted promotional spending
✔ Helps founders & ops teams make fast, smart decisions
✔ Reduces manual reporting time
✔ Converts complex data into beautiful insights

---

# 🧪 Scope of Improvement (Roadmap)

* Forecasting models for GMV, orders
* Auto email reports
* Mobile dashboard version
* Deep dive menus: items, categories, combos
* Geo heatmap
* Multi-brand portfolio mode
* API integrations

---

# ⚠️ Important Disclaimer

**All insights in this dashboard are based on the dataset provided.**
Real-world performance may differ if:

* Data quality varies
* More brands are added
* Different time ranges exist
* New KPIs are introduced

This dashboard is **data-dependent**.

---

# 👤 **Author — Veman Shrinivas Chippa**

Data Analyst • Dashboard Developer • Insight Architect
Turning raw data into beautiful, usable business intelligence.

---

## 🔗 Connect with Me

| Platform              | Link                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| 🌐 **Portfolio**      | [https://iveman.vercel.app/](https://iveman.vercel.app/)                                                     |
| 💼 **LinkedIn**       | [https://www.linkedin.com/in/veman-chippa](https://www.linkedin.com/in/veman-chippa)                         |
| 💻 **GitHub**         | [https://github.com/iveman99](https://github.com/iveman99)                                                   |
| 📊 **Live Dashboard** | [https://iveman-fb-analytics-dashboard.streamlit.app/](https://iveman-fb-analytics-dashboard.streamlit.app/) |

---

# ⭐ Like this project?

If this dashboard inspired you or helped you, please ⭐ **star the repository** — it motivates me to build more such high-quality analytics experiences!
