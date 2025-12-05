# app.py - Full corrected version (month parsing + chart fixes + hover + legend color)
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import io
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.set_page_config(page_title="Culinary Compass", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
<style>

    /* Keep Streamlit header structure active but invisible */
    header[data-testid="stHeader"] {
        background: transparent !important;
        height: 0px !important;
        padding: 0px !important;
    }

    /* Make toolbar (which contains the sidebar hamburger button) visible */
    header[data-testid="stHeader"] > div:nth-child(1) {
        visibility: visible !important;
        display: flex !important;
        align-items: center !important;
        height: 40px !important;
        margin-left: 10px !important;
        z-index: 99999 !important;
        position: fixed !important;
        top: 18px !important; /* aligns nicely with banner */
    }

    /* Our custom top banner */
    /* Our custom top banner */
    .custom-top-banner {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        padding: 18px 0;
        background: linear-gradient(90deg,#ffd966,#f4c430);
        color: #081827;
        font-size: 22px;
        font-weight: 800;
        text-align: center;
        z-index: 9999;
        box-shadow:0px 4px 12px rgba(0,0,0,0.2);
    }

    /* Shine animation for banner text */
.banner-text {
    display: inline-block;
    background: linear-gradient(
        90deg,
        #081827 0%,
        #081827 40%,
        #ffffff 50%,
        #081827 60%,
        #081827 100%
    );
    background-size: 250%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: shineMove 4s infinite linear;
}

@keyframes shineMove {
    0% { background-position: 250% 0; }
    100% { background-position: -250% 0; }
}

    /* Push page content down */
    .main {
        margin-top: 110px !important;
    }

</style>

<div class="custom-top-banner">
    🍽️ <span class="banner-text">Transforming Restaurant Data Into Powerful Business Insights</span>
</div>


""", unsafe_allow_html=True)


# ------------------
# CSS / Branding (unchanged but included)
# ------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap');
    *{font-family:'Inter',sans-serif;}
    .stApp{
        background:linear-gradient(135deg,#051022 0%,#081827 50%,#0f2130 100%);
        color:#fff;

    }

    /* Sidebar background */
    section[data-testid="stSidebar"]{
        background:linear-gradient(180deg,#07121a 0%,#081827 100%);
        border-right:2px solid rgba(255,217,102,0.06);
        box-shadow:6px 0 36px rgba(0,0,0,0.55);
        padding-top:8px;
    }

    /* Logo/title colors in sidebar */
    .sidebar .stMarkdown h2, .sidebar .stMarkdown h3 { color: #ffd966 !important; }

    /* NAV buttons (sidebar) - transparent by default, golden on active */
    .stButton > button {
        background: transparent !important;
        color: #ffd966 !important;
        border: 1px solid rgba(255,217,102,0.12) !important;
        padding: 8px 14px !important;
        border-radius: 999px !important;
        font-weight:700;
        box-shadow: none !important;
        transition: all .15s ease;
    }
    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 6px 18px rgba(0,0,0,0.35) !important;
    }
    /* active nav style - we will add a small inline style when rendering the active button to make it golden */
    .nav-active {
        background: linear-gradient(90deg,#ffd966,#f4c430) !important;
        color: #081827 !important;
        border: 1px solid rgba(0,0,0,0.12) !important;
    }

    /* Inputs / select / multiselect / dropdowns: transparent + subtle golden outline */
    /* Generic container targeting - Streamlit creates many variations: this attempts to catch most */
    div[role="listbox"], .stMultiSelect, .stSelectbox, .stTextInput, .stDateInput, .stFileUploader {
        background: transparent !important;
        box-shadow: none !important;
        border-radius: 10px !important;
        border: 1px solid rgba(255,217,102,0.06) !important;
        padding: 6px 8px !important;
    }
    /* Make the selection panels/backgrounds dark & subtle */
    .stMultiSelect div[role="listbox"], .stSelectbox div[role="listbox"], .stSelectbox .css-1d391kg, .stMultiSelect .css-1d391kg {
        background: linear-gradient(180deg, rgba(255,255,255,0.01), rgba(0,0,0,0.07)) !important;
    }

    /* Multiselect chips / tags to look golden */
    /* Streamlit uses tag elements; this rule targets common patterns for tags */
    [data-baseweb="tag"], .css-1yi8z6s, .e16nr0p30 {
        background: linear-gradient(90deg,#ffd966,#f4c430) !important;
        color:#081827 !important;
        font-weight:700 !important;
        border-radius:8px !important;
        padding:4px 8px !important;
    }

    /* Download / link buttons (About page) - keep golden gradient */
    a[data-testid="stMarkdownLink"], .download-btn > button {
        background: linear-gradient(90deg,#ffd966,#f4c430) !important;
        color:#081827 !important;
        border-radius:10px !important;
        padding:8px 12px !important;
        font-weight:700 !important;
        border: none !important;
    }

    /* KPI card styling (keep the look but prefer golden label where previously grey) */
    .kpi-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:22px;margin:28px 0 36px 0;}
    .kpi-card{
        background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.005));
        border-radius:16px;padding:22px 22px;box-shadow:0 10px 30px rgba(2,8,18,0.6);
        border:1px solid rgba(255,255,255,0.02);min-height:110px;
    }
    .kpi-label{color:#ffd966;font-size:12px;font-weight:700;letter-spacing:1px;margin-bottom:8px;}
    .kpi-value{font-size:30px;font-weight:800;color:transparent;background:linear-gradient(135deg,#ffffff,#ffd966);-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
    .kpi-subtext{color:#dbeafb;font-size:13px;margin-top:6px;}

    /* Headline: golden clipped text */
    h1{font-size:48px;margin:8px 0 18px 0;color:transparent;background:linear-gradient(135deg,#ffffff,#ffd966);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:800;}

    .info-box{background:rgba(255,255,255,0.02);border-left:4px solid #ffd966;padding:14px;border-radius:8px;margin:18px 0;color:#dbeafb;}
    .about-box{background:rgba(255,255,255,0.02);padding:18px;border-radius:10px;color:#dbeafb;}

    .styled-table{width:100%;border-collapse:collapse;background:transparent;color:#fff;}
    .styled-table thead th{color:#ffd966;text-transform:uppercase;padding:10px 12px;font-weight:700;border-bottom:1px solid rgba(255,255,255,0.06);}
    .styled-table td{padding:12px;border-bottom:1px solid rgba(255,255,255,0.03);}

    .badge-high{background:#ff4757;color:#fff;padding:8px 14px;border-radius:14px;font-weight:700;}
    .badge-med{background:#ffd966;color:#082033;padding:8px 14px;border-radius:14px;font-weight:700;}
    .badge-low{background:#2ecc71;color:#082033;padding:8px 14px;border-radius:14px;font-weight:700;}

    footer { color: #9fb0bf; padding: 18px 0; text-align:center; }
    /* Fade-in animation for all main content */
    .main > div {
        animation: fadeIn 0.9s ease-in-out;
    }

    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(12px); }
        100% { opacity: 1; transform: translateY(0px); }
    }
    .kpi-card {
    transition: transform 0.25s ease, box-shadow 0.25s ease;
}

.kpi-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 12px 28px rgba(255,217,102,0.25);
}

    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------
# Data loader (robust month parsing)
# ------------------
@st.cache_data
def load_data(path="clean_case_study.csv"):
    df = pd.read_csv(path, low_memory=False)
    df.columns = [c.strip() for c in df.columns]

    # Try to robustly find a month/date column and parse it to month period
    # Support many formats: "2025-08-01", "Aug-25", "August 2025", "2025/08", "08-2025", "Aug 25", etc.
    month_col = None
    for cand in ["Month", "month", "Month_Year", "month_year", "DT", "Date", "date"]:
        if cand in df.columns:
            month_col = cand
            break

    def parse_to_month(s):
        # try a few parsing strategies
        try:
            return pd.to_datetime(s, errors="coerce")
        except Exception:
            return pd.NaT

    if month_col:
        # initial parse attempt
        df["month_year_raw"] = df[month_col].astype(str).fillna("")
        df["month_year_parsed"] = pd.to_datetime(df["month_year_raw"], errors="coerce")

        # If many failures, try cleaning strings and common formats
        if df["month_year_parsed"].isna().sum() > 0:
            # try format with abbreviated month+year (e.g., Aug-25 or Aug25 or Aug 2025)
            cleaned = df["month_year_raw"].astype(str).str.replace(r"(\b)([A-Za-z]{3,9})[^\d]*(\d{2,4})", r"\2 \3", regex=True)
            # second attempt
            df["month_year_parsed"] = pd.to_datetime(cleaned, errors="coerce", dayfirst=False)

        # final fallback: try extracting YYYY-MM or YYYY
        if df["month_year_parsed"].isna().sum() > 0:
            # remove non alnum and attempt to parse year-month numeric patterns
            numeric = df["month_year_raw"].astype(str).str.replace(r"[^0-9]", "", regex=True)
            parsed_numeric = pd.to_datetime(numeric, format="%Y%m", errors="coerce")
            # merge results where available
            df.loc[df["month_year_parsed"].isna(), "month_year_parsed"] = parsed_numeric[df["month_year_parsed"].isna()]

        df["month_year"] = df["month_year_parsed"].dt.to_period("M").dt.to_timestamp()
        df.drop(columns=["month_year_raw", "month_year_parsed"], inplace=True, errors="ignore")
    else:
        # no month-like column found, fallback to a default date
        df["month_year"] = pd.to_datetime("2025-01-01")

    # numeric columns fallback mapping
    for col in ["TOTAL_ORDERS", "Total Orders", "total_orders"]:
        if col in df.columns:
            df["TOTAL_ORDERS"] = pd.to_numeric(df[col], errors="coerce").fillna(0)
            break
    else:
        df["TOTAL_ORDERS"] = 0

    for col in ["GMV", "Total GMV", "total_gmv"]:
        if col in df.columns:
            df["GMV"] = pd.to_numeric(df[col], errors="coerce").fillna(0.0)
            break
    else:
        df["GMV"] = 0.0

    for col in ["MENU_SESSIONS", "MENU", "total_menu", "Menu Opens"]:
        if col in df.columns:
            df["MENU_SESSIONS"] = pd.to_numeric(df[col], errors="coerce").fillna(0)
            break
    else:
        df["MENU_SESSIONS"] = 0

    if "REST_NAME" not in df.columns and "Restaurant" in df.columns:
        df["REST_NAME"] = df["Restaurant"].astype(str)
    if "AREA" not in df.columns and "Area" in df.columns:
        df["AREA"] = df["Area"].astype(str)

    df["REST_NAME"] = df.get("REST_NAME", df.columns[0]).astype(str)
    df["AREA"] = df.get("AREA", "Unknown").astype(str)

    df["conversion_rate"] = df["TOTAL_ORDERS"] / df["MENU_SESSIONS"].replace({0: np.nan})

    return df

# load data
df = load_data("clean_case_study.csv")

# ------------------
# Sidebar content + Navigation
# ------------------
pages = ["Business Summary", "Restaurant Performance", "Area Insights", "Promo Strategy", "Conversion Strategy",
         "About"]

with st.sidebar:
    # try to show logo if present
    try:
        st.image("assets/logo.jpeg", width=200)
    except Exception:
        pass

    st.markdown(
        """
        <h1 style='color: goldenrod;'>F&B Insights Dashboard</h1>
        <h3 style='color: white;'>🎯 Navigation</h3>
        """,
        unsafe_allow_html=True
    )

    if "page" not in st.session_state:
        st.session_state.page = "Business Summary"

    for p in pages:
        if st.button(p, key=f"nav_{p}"):
            st.session_state.page = p

    st.markdown("---")
    st.markdown("<h2 style='color: white;'>🎯 Filters</h2>", unsafe_allow_html=True)

    brands = sorted(df["REST_NAME"].dropna().unique())
    selected_brands = st.multiselect("Brand", options=brands, default=brands[:3] if len(brands) > 0 else [])

    areas = sorted(df["AREA"].dropna().unique())
    selected_areas = st.multiselect("Area", options=areas, default=areas[:3] if len(areas) > 0 else [])

    # dynamic months (unique month periods)
    months = sorted(df["month_year"].dropna().unique())
    # ensure months are period-start timestamps (first of month)
    months = [pd.to_datetime(m).to_period("M").to_timestamp() for m in months]
    month_options = [None] + months

    def month_format(x):
        return "All Months" if x is None else pd.to_datetime(x).strftime("%b %Y")

    # selectbox default index 0 => All Months
    selected_month = st.selectbox("Month", options=month_options, format_func=month_format, index=0)

# set current page
page = st.session_state.page

# ------------------
# Apply filters
# ------------------
df_f = df.copy()

if selected_brands:
    df_f = df_f[df_f["REST_NAME"].isin(selected_brands)]
if selected_areas:
    df_f = df_f[df_f["AREA"].isin(selected_areas)]
if selected_month is not None:
    # selected_month is a Timestamp for the month start
    df_f = df_f[df_f["month_year"] == selected_month]

if df_f.shape[0] == 0:
    st.warning("⚠️ No data for selected filters. Showing full dataset.")
    df_f = df.copy()

# helpers
def fmt_gmv(n):
    try:
        n = float(n)
    except Exception:
        return "—"
    if abs(n) >= 1_000_000:
        return f"₹{n / 1_000_000:,.2f}M"
    if abs(n) >= 1000:
        return f"₹{n:,.0f}"
    return f"₹{n:.0f}"

def fmt_num(n):
    try:
        n = int(n)
        if abs(n) >= 1000:
            return f"{n:,}"
        return str(n)
    except Exception:
        return "—"

# compute KPIs
total_orders = int(df_f["TOTAL_ORDERS"].sum())
total_gmv = float(df_f["GMV"].sum())
avg_conversion = (df_f["conversion_rate"].mean() or 0) * 100
top_area = df_f.groupby("AREA")["TOTAL_ORDERS"].sum().idxmax() if len(df_f) > 0 else "—"
top_brand = df_f.groupby("REST_NAME")["GMV"].sum().idxmax() if len(df_f) > 0 else "—"

# KPI display
st.markdown(f"<h1>🍽️ {page}</h1>", unsafe_allow_html=True)
kpi_html = f"""
<div class="kpi-row">
  <div class="kpi-card">
    <div class="kpi-label">Total Orders</div>
    <div class="kpi-value">{total_orders:,}</div>
    <div class="kpi-subtext">📦 Delivered</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Total GMV</div>
    <div class="kpi-value">{fmt_gmv(total_gmv)}</div>
    <div class="kpi-subtext">💰 Revenue</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Avg Conversion</div>
    <div class="kpi-value">{avg_conversion:.2f}%</div>
    <div class="kpi-subtext">📈 Menu → Order</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Top Area</div>
    <div class="kpi-value" style="font-size:20px">{top_area}</div>
    <div class="kpi-subtext">📍 By Orders</div>
  </div>
  <div class="kpi-card">
    <div class="kpi-label">Top Brand</div>
    <div class="kpi-value" style="font-size:20px">{top_brand}</div>
    <div class="kpi-subtext">🏆 By GMV</div>
  </div>
</div>
"""
st.markdown(kpi_html, unsafe_allow_html=True)

# ------------------
# Plot helpers (fixed monthly_chart)
# ------------------
def monthly_chart(df_in):
    # drop rows without month info
    df_in = df_in.dropna(subset=["month_year"]).copy()

    # ensure month_year is normalized to period start (first of month)
    df_in["month_year"] = pd.to_datetime(df_in["month_year"]).dt.to_period("M").dt.to_timestamp()

    # aggregation: one row per month
    agg = df_in.groupby("month_year", as_index=False).agg(
        orders=("TOTAL_ORDERS", "sum"),
        gmv=("GMV", "sum")
    ).sort_values("month_year")

    # If there are expected months missing (e.g., you always want Jun/Jul/Aug), you can enforce them:
    # optional: create a full month index between min and max to ensure continuity
    agg = agg.sort_values("month_year").copy()
    x = agg["month_year"]

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Orders trace: show hovertemplate that only displays order info for this trace
    fig.add_trace(go.Scatter(
        x=x,
        y=agg["orders"],
        mode="lines+markers+text",
        name="Orders",
        marker=dict(size=10, color="#4da6ff"),
        line=dict(width=3, color="#4da6ff"),
        text=[f"{int(v):,}" if not pd.isna(v) else "" for v in agg["orders"]],
        textposition="top center",
        textfont=dict(color="white", size=12),
        hovertemplate="Orders: %{y:,}<extra></extra>"
    ), secondary_y=False)

    # GMV trace: secondary axis
    fig.add_trace(go.Scatter(
        x=x,
        y=agg["gmv"],
        mode="lines+markers+text",
        name="GMV",
        marker=dict(size=10, color="#ffd966"),
        line=dict(width=3, color="#ffd966"),
        text=[fmt_gmv(v) if not pd.isna(v) else "" for v in agg["gmv"]],
        textposition="bottom center",
        textfont=dict(color="white", size=11),
        hovertemplate="GMV: %{y:,.0f}<extra></extra>"
    ), secondary_y=True)

    # add small padding so markers/text don't overlap the edges
    if agg["orders"].notna().any():
        o_min = float(agg["orders"].min())
        o_max = float(agg["orders"].max())
        if o_min == o_max:
            fig.update_yaxes(range=[o_min * 0.95 - 1, o_max * 1.05 + 1], secondary_y=False)
        else:
            fig.update_yaxes(range=[o_min * 0.95, o_max * 1.05], secondary_y=False)

    if agg["gmv"].notna().any():
        g_min = float(agg["gmv"].min())
        g_max = float(agg["gmv"].max())
        if g_min == g_max:
            fig.update_yaxes(range=[g_min * 0.95 - 1, g_max * 1.05 + 1], secondary_y=True)
        else:
            fig.update_yaxes(range=[g_min * 0.95, g_max * 1.05], secondary_y=True)

    # layout
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#ffffff", family="Inter"),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color="white", size=14)
        ),
        margin=dict(t=30, b=40, l=60, r=60),
        height=520,
        hovermode="closest"  # important: show only the hovered trace, not all traces at that x
    )

    # X-axis: force monthly ticks
    fig.update_xaxes(
        tickmode="array",
        tickvals=agg["month_year"],
        ticktext=[d.strftime("%b %Y") for d in agg["month_year"]],
        title_text="<b>Month</b>",
        showgrid=False
    )

    fig.update_yaxes(title_text="<b>Orders</b>", secondary_y=False, showgrid=True,
                     gridcolor="rgba(255,255,255,0.04)")
    fig.update_yaxes(title_text="<b>GMV (₹)</b>", secondary_y=True, showgrid=False)
    fig.update_yaxes(tickformat=",", secondary_y=True)

    return fig

def funnel_chart(df_in):
    tm = int(df_in["MENU_SESSIONS"].sum() or 0)
    to = int(df_in["TOTAL_ORDERS"].sum() or 0)
    conv_percent = (to / tm * 100) if (tm > 0) else 0.0
    fig = go.Figure(go.Funnel(
        y=["Menu Opens", "Orders"],
        x=[tm, to],
        textinfo="value+percent initial",
        marker=dict(color=["#4da6ff", "#ffd966"], line=dict(color="rgba(0,0,0,0.15)"))
    ))
    fig.update_traces(hovertemplate="%{label}: %{value:,}<br>%{percentInitial:.1%} of initial")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#dbeafb"),
        height=420,
        margin=dict(t=20, b=20, l=60, r=60)
    )
    return fig, tm, to, conv_percent

def priority_table(df_in):
    s = df_in.groupby("REST_NAME").agg(orders=("TOTAL_ORDERS", "sum"), menu=("MENU_SESSIONS", "sum"),
                                       gmv=("GMV", "sum")).reset_index()
    s["conv"] = s["orders"] / s["menu"].replace({0: np.nan})

    def priority_fn(x):
        if pd.isna(x):
            return "High"
        if x < 0.10:
            return "High"
        if x < 0.14:
            return "Medium"
        return "Low"

    s["Priority"] = s["conv"].apply(priority_fn)
    s["Badge"] = s["Priority"].map({"High": '<span class="badge-high">High Priority</span>',
                                    "Medium": '<span class="badge-med">Medium Priority</span>',
                                    "Low": '<span class="badge-low">Low Priority</span>'})
    order_map = {"High": 0, "Medium": 1, "Low": 2}
    s["prio_order"] = s["Priority"].map(order_map)
    s = s.sort_values(["prio_order", "orders"], ascending=[True, False]).drop(columns=["prio_order"])
    return s

# ------------------
# Page content
# ------------------
if page == "Business Summary":
    st.markdown("### 📊 Monthly Trends")
    st.markdown(
        '<div class="info-box"><b>How we calculated:</b> Monthly aggregation of TOTAL_ORDERS and GMV. Hover the chart to see exact values.</div>',
        unsafe_allow_html=True)

    # DEBUG: show which months are present (remove later if desired)
    try:
        unique_months = sorted(df_f["month_year"].dropna().unique())
    except Exception:
        pass

    fig_month = monthly_chart(df_f)
    st.plotly_chart(fig_month, use_container_width=True)

    cols = st.columns((1, 1))
    with cols[0]:
        st.markdown("### 🔄 Conversion Funnel")
        fig_f, tm, to, conv_percent = funnel_chart(df_f)
        st.plotly_chart(fig_f, use_container_width=True)
        st.markdown(
            f'<div class="info-box">From <b>{tm:,}</b> menu opens → <b>{to:,}</b> orders = <b>{conv_percent:.2f}%</b> conversion</div>',
            unsafe_allow_html=True)
    with cols[1]:
        st.markdown("### 📈 Quick Insights")
        aov = (total_gmv / total_orders) if total_orders > 0 else 0
        st.markdown(f"""
            <div class="about-box">
            <b>Snapshot</b>
            <ul>
              <li>Sessions: <b>{int(df_f['MENU_SESSIONS'].sum()):,}</b></li>
              <li>Avg Conversion: <b>{avg_conversion:.2f}%</b></li>
              <li>Avg Order Value: <b>{fmt_gmv(aov)}</b></li>
            </ul>
            </div>
            """, unsafe_allow_html=True)

elif page == "Restaurant Performance":
    st.markdown("### 🏆 Top 5 Restaurants by GMV")
    if selected_month is not None:
        display_df = df_f
        title_range = selected_month.strftime("%b %Y")
    else:
        max_month = df["month_year"].max()
        three_months = (max_month - pd.offsets.MonthBegin(2))
        display_df = df[df["month_year"] >= three_months]
        title_range = "Last 3 Months"

    top5 = display_df.groupby("REST_NAME")["GMV"].sum().nlargest(5).reset_index()
    if top5.shape[0] == 0:
        st.info("No data to show for Top 5.")
    else:
        fig = go.Figure(go.Bar(
            x=top5["REST_NAME"], y=top5["GMV"],
            marker=dict(color=top5["GMV"], colorscale=[[0, "#ffd966"], [1, "#ff8c00"]]),
            text=[fmt_gmv(x) for x in top5["GMV"]],
            textposition='outside'
        ))
        fig.update_layout(title=f"{title_range}", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)",
                          font=dict(color="#dbeafb"), height=420, margin=dict(t=30))
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📋 Priority Matrix — How we decide")
    st.markdown(
        '<div class="info-box"><b>Rule:</b> High priority = conversion &lt; 10%. Medium = 10–14%. Low = 14%+</div>',
        unsafe_allow_html=True)

    tbl = priority_table(df)
    html_tbl = '<table class="styled-table"><thead><tr><th>Restaurant</th><th>Orders</th><th>Menu Opens</th><th>Conversion</th><th>Priority</th></tr></thead><tbody>'
    for _, r in tbl.head(10).iterrows():
        conv_disp = (f"{(r['conv'] * 100):.2f}%" if pd.notna(r["conv"]) else "—")
        html_tbl += f"<tr><td>{r['REST_NAME']}</td><td>{int(r['orders']):,}</td><td>{int(r['menu']):,}</td><td>{conv_disp}</td><td>{r['Badge']}</td></tr>"
    html_tbl += "</tbody></table>"
    st.markdown(html_tbl, unsafe_allow_html=True)
    csv_buf = io.StringIO()
    tbl.to_csv(csv_buf, index=False)
    st.download_button("📥 Download priority CSV", csv_buf.getvalue(), file_name="restaurant_priority.csv",
                       key="dl_priority", help="Download full priority table", )

elif page == "Area Insights":
    st.markdown("### 🗺️ Area Performance")
    st.markdown(
        '<div class="info-box"><b>How we calculated:</b> Area-level orders / menu opens → conversion percentage (converted to %).</div>',
        unsafe_allow_html=True)
    area_df = df_f.groupby("AREA").agg(orders=("TOTAL_ORDERS", "sum"), menu=("MENU_SESSIONS", "sum")).reset_index()
    area_df["conv"] = (area_df["orders"] / area_df["menu"]).fillna(0)
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Bar(x=area_df["AREA"], y=area_df["orders"], name="Orders", marker_color="#4da6ff"),
                  secondary_y=False)
    fig.add_trace(go.Scatter(x=area_df["AREA"], y=area_df["conv"] * 100, name="Conversion %", marker_color="#ffd966"),
                  secondary_y=True)
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", font=dict(color="#dbeafb"),
                      height=480)
    fig.update_yaxes(title_text="Orders", secondary_y=False)
    fig.update_yaxes(title_text="Conversion %", secondary_y=True)
    st.plotly_chart(fig, use_container_width=True)
    st.dataframe(area_df.style.format({"orders": "{:,}", "menu": "{:,}", "conv": "{:.2%}"}), height=320)

elif page == "Promo Strategy":
    st.markdown("### 🎯 Promo Recommendations")
    st.markdown(
        '<div class="info-box"><b>Goal:</b> Focus promotional tests on High priority restaurants (conversion <10%).</div>',
        unsafe_allow_html=True)
    tbl = priority_table(df)
    html_tbl = '<table class="styled-table"><thead><tr><th>Restaurant</th><th>Orders</th><th>Menu</th><th>Conversion</th><th>Priority</th></tr></thead><tbody>'
    for _, r in tbl.iterrows():
        conv_disp = (f"{(r['conv'] * 100):.2f}%" if pd.notna(r["conv"]) else "—")
        html_tbl += f"<tr><td>{r['REST_NAME']}</td><td>{int(r['orders']):,}</td><td>{int(r['menu']):,}</td><td>{conv_disp}</td><td>{r['Badge']}</td></tr>"
    html_tbl += "</tbody></table>"
    st.markdown(html_tbl, unsafe_allow_html=True)
    high_count = tbl[tbl["Priority"] == "High"].shape[0]
    st.markdown(
        f'<div class="about-box"><b>Action:</b> Run targeted promos for <b>{high_count}</b> high-priority outlets. Example plan: A/B discount test, 7-day uplift tracking, emphasize top items. </div>',
        unsafe_allow_html=True)

elif page == "Conversion Strategy":
    st.markdown("### 💡 Strategies to Increase Conversion (Menu → Order)")
    st.markdown("""
    <div class="about-box">
    <ol>
      <li><b>Menu Simplification & Highlight Top Items</b> — reduce choices, show 'Popular' badge and default combos.</li>
      <li><b>Targeted Discounts for Low-Conversion Outlets</b> — run a 10% A/B promo for High-priority restaurants and measure delta.</li>
      <li><b>Personalized Recommendations</b> — show area-specific top-sellers and time-limited offers (funnel urgency).</li>
    </ol>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### 🔄 Current Funnel")
    fig_f, tm, to, conv_percent = funnel_chart(df_f)
    st.plotly_chart(fig_f, use_container_width=True)
    st.markdown(
        f'<div class="info-box">Overall conversion for current filters: <b>{conv_percent:.2f}%</b> ({to:,} orders from {tm:,} opens)</div>',
        unsafe_allow_html=True)

elif page == "About":
    st.markdown("""
    <div class="about-box">
      <h3 style="color:#ffd966">Project Story</h3>
      <p><b>Author:</b> Veman Shrinivas Chippa</p>
      <p><b>What this dashboard does:</b> Identifies restaurants with low menu→order conversion, prioritizes promo opportunities, and shows top-line KPIs and trends.</p>
      <p><b>Tech:</b> Python (pandas, numpy), Streamlit, Plotly</p>
      <div style="margin-top:12px;">
        <a href="https://iveman.vercel.app/" target="_blank" style="margin-right:12px;color:#081827;background:linear-gradient(90deg,#ffd966,#f4c430);padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:700;">🌐 Portfolio</a>
        <a href="https://www.linkedin.com/in/veman-chippa" target="_blank" style="margin-right:12px;color:#081827;background:linear-gradient(90deg,#ffd966,#f4c430);padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:700;">💼 LinkedIn</a>
        <a href="https://github.com/iveman99" target="_blank" style="color:#081827;background:linear-gradient(90deg,#ffd966,#f4c430);padding:10px 14px;border-radius:8px;text-decoration:none;font-weight:700;">💻 GitHub</a>
      </div>
    </div>
    """, unsafe_allow_html=True)

# footer
st.markdown('<footer>© 2025 Veman Shrinivas Chippa • Created with passion — Making data speak 📊</footer>',
            unsafe_allow_html=True)
