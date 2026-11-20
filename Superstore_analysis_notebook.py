import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
from IPython.display import display, HTML
import webbrowser
df = pd.read_csv("Superstore_Modified.csv")

print(df.shape)

print(df.describe())

print(df.columns)

#total Sales
total_sales = df["Sales"].sum()
print(total_sales)

#total customers
total_customers = df["Customer ID"].nunique()
print(total_customers)

#total profit
total_profit = df["Profit"].sum()
print(total_profit)

#Total products
total_product = df["Product ID"].nunique()
print(total_product)

#total orders
total_orders = df["Order ID"].nunique()
print(total_orders)

#profit margin
profit_margin = (df["Profit"].sum()/df["Sales"].sum())*100
print(f"{profit_margin:.2f}%")

#Average order value
AOV = df["Sales"].sum()/df["Order ID"].nunique()
print(AOV)

#displaying kpi cards using html and css


html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">

<style>

/* MAIN PAGE */
body {{
    background-color: #0B1628;
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 25px;
    color: white;
    box-sizing: border-box;
}}

/* DASHBOARD HEADING */
.dashboard-title {{
    color: #00D4FF;
    font-size: 28px;
    margin-bottom: 25px;
}}

/* KPI SECTION */
.kpi-grid {{
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 18px;
    margin-bottom: 35px;
}}

.kpi-card {{
    padding: 22px;
    border-radius: 14px;
    color: white;
    min-height: 115px;
    box-sizing: border-box;
    overflow-wrap: anywhere;
}}

.kpi-card p {{
    font-size: 14px;
    margin: 0 0 18px 0;
}}

.kpi-card h2 {{
    font-size: 23px;
    margin: 0;
}}

/* DASHBOARD SECTIONS */
.dashboard-section {{
    margin-top: 35px;
    margin-bottom: 30px;
}}

/* SECTION HEADINGS */
.section-title {{
    color: #00D4FF;
    font-size: 23px;
    font-weight: bold;
    margin-bottom: 20px;
    padding-bottom: 10px;
    border-bottom: 1px solid #405675;
}}

/* CHART GRID */
.chart-grid {{
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 22px;
    align-items: stretch;
}}

/* CHART CARDS */
.chart-card {{
    background: #142D4E;
    border: 1px solid #405675;
    border-radius: 14px;
    padding: 16px;
    box-sizing: border-box;
    width: 100%;
    min-width: 0;
    overflow: hidden;
    transition: transform 0.2s ease;
}}

.chart-card:hover {{
    transform: translateY(-3px);
}}

/* CHART TITLES */
.chart-card h3 {{
    color: #FFFFFF;
    font-size: 16px;
    font-weight: bold;
    text-align: center;
    margin: 5px 0 15px 0;
    min-height: 22px;
}}

/* ALL CHART IMAGES */
.chart-card img {{
    display: block;
    width: 100%;
    height: 280px;
    max-width: 100%;
    object-fit: contain;
    object-position: center;
    border-radius: 8px;
    margin: auto;
}}

/* RESPONSIVE TABLET */
@media (max-width: 900px) {{
    .kpi-grid {{
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }}

    .chart-grid {{
        grid-template-columns: 1fr;
    }}

    .chart-card img {{
        height: 300px;
    }}
}}

/* RESPONSIVE MOBILE */
@media (max-width: 550px) {{
    body {{
        padding: 12px;
    }}

    .kpi-grid {{
        grid-template-columns: 1fr;
    }}

    .chart-card {{
        padding: 10px;
    }}

    .chart-card img {{
        height: 220px;
    }}

    .chart-card h3 {{
        font-size: 14px;
    }}
}}


</style>
</head>

<body>

<h1 class="dashboard-title">Superstore Business Dashboard</h1>

<!-- KPI SECTION -->
<div class="kpi-grid">

    <div class="kpi-card" style="background:#142D4E;">
        <p style="color:#A9C9ED;">TOTAL SALES</p>
        <h2>${total_sales:,.2f}</h2>
    </div>

    <div class="kpi-card" style="background:#17465A;">
        <p style="color:#A9E1E8;">TOTAL PROFIT</p>
        <h2>${total_profit:,.2f}</h2>
    </div>

    <div class="kpi-card" style="background:#263B68;">
        <p style="color:#B8CCFF;">TOTAL ORDERS</p>
        <h2>{total_orders:,}</h2>
    </div>

    <div class="kpi-card" style="background:#49345F;">
        <p style="color:#E0C5FF;">TOTAL CUSTOMERS</p>
        <h2>{total_customers:,}</h2>
    </div>

    <div class="kpi-card" style="background:#17534D;">
        <p style="color:#A9E8D7;">TOTAL PRODUCTS</p>
        <h2>{total_product:,}</h2>
    </div>

    <div class="kpi-card" style="background:#59432C;">
        <p style="color:#F5D5A6;">PROFIT MARGIN</p>
        <h2>{profit_margin:.2f}%</h2>
    </div>

    <div class="kpi-card" style="background:#34445B;">
        <p style="color:#C6D9F1;">AVERAGE ORDER VALUE</p>
        <h2>${AOV:,.2f}</h2>
    </div>

</div>

<!-- SALES ANALYSIS SECTION -->
<div class="dashboard-section">

    <h2 class="section-title">Sales Analysis</h2>

    <div class="chart-grid">

        <div class="chart-card">
            <h3>Monthly Sales Trend</h3>
            <img src="output/monthly_sales_linechart.png">
        </div>

        <div class="chart-card">
            <h3>Sales by Region</h3>
            <img src="output/Sales_by_region.png">
        </div>

        <div class="chart-card">
            <h3>Sales by Category</h3>
            <img src="output/Sales_by_category.png">
        </div>


<!-- CUSTOMER ANALYSIS -->
<div class="dashboard-section">

    <h2 class="section-title">Customer Analysis</h2>

    <div class="chart-grid">

        <div class="chart-card">
            <h3>Top 10 Customers by Sales</h3>
            <img src="output/Top10_customers_bargraph.png">
        </div>

    </div>

</div>


<!-- PRODUCT PERFORMANCE -->
<div class="dashboard-section">

    <h2 class="section-title">Product Performance</h2>

    <div class="chart-grid">

        <div class="chart-card">
            <h3>Top 10 Products by Sales</h3>
            <img src="output/Top10_product.png">
        </div>

    </div>

</div>


<!-- PROFIT ANALYSIS -->
<div class="dashboard-section">

    <h2 class="section-title">Profit Analysis</h2>

    <div class="chart-grid">

        <div class="chart-card">
            <h3>Profit by Category</h3>
            <img src="output/Profit_by_Category.png">
        </div>

    </div>

</div>

<!-- Correlation heatmap -->
<div class ="dashboard-section">

    <h2 class ="Section-title">Correlation heatmap</h2>

    <div class ="chart-grid">

        <div class = "chart-card">
            <h3>correlation heatmap</h3>
            <img src="output/correlation_heatmap.png">
        </div>
    </div>
</div>
</body>
</html>
"""

# SAVE HTML FILE
with open("KPI_Dashboard.html", "w", encoding="utf-8") as f:
    f.write(html)

# OPEN DASHBOARD IN BROWSER
webbrowser.open(os.path.abspath("KPI_Dashboard.html"))


#Number of Products solds
product_sold = df["Quantity"].sum()
print("Total Number of Products sold:- ",product_sold)

#Best selling Product
Best_selling_product = df.groupby("Category")["Quantity"].sum()
print("Best Selling Product:- ",Best_selling_product)

#Heighest  revenue Category
Highest_category_sales = df.groupby("Category")["Sales"].sum()
Highest_category = Highest_category_sales.idxmax()
print("Highest revenue Category:- ",Highest_category)

#converting datatyoe from string to date
df["Order Date"] = pd.to_datetime(df["Order Date"],errors="coerce")
df["Ship Date"]  = pd.to_datetime(df["Ship Date"],errors="coerce")
#Top10 customers by sales
Top10_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)
print("Top10 Customers by sales:- ",Top10_customers)

#top5 cities
top5_cities = df.groupby("City")["Sales"].sum().sort_values(ascending=False).head()
print("Top5 cities:- ",top5_cities)




#Display Total Sales by Region
Sales_region = df.groupby("Region")["Sales"].sum()
print("Total Sales by Regions:- ",Sales_region)

#Display Total Profit by category
profit_category = df.groupby("Category")["Profit"].sum()
print("Total Profit by category:- ",profit_category)
print(df.dtypes)

#Montly Sales
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum()
print("Monthly Sales:- ",monthly_sales)

#Customer Wise revenue
customer_revenue = df.groupby("Customer Name")["Sales"].sum()
print("Customer wise Revenue:- ",customer_revenue)

#Top10 Products by Sales
Top10_Products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
print(Top10_Products)

""" #Monthly Sales Trend
monthly_sales.index = monthly_sales.index.to_timestamp()
plt.figure(figsize=(8,5))
plt.plot(monthly_sales.index,monthly_sales.values,
         color ="#35B6F6",
         linewidth =2.8,
         marker = "o",
         markersize =5,
         markerfacecolor = "#20D6B0",
         markeredgecolor = "white",
         label = "Monthly Sales")
         
plt.title("Monthly Sales Trend",fontsize=16,fontweight="bold")
plt.xlabel("Months",fontsize=12,fontweight="bold")
plt.ylabel("Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)

plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")


plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.tick_params(colors="#DCEBFA")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Sales by Category bar chart
Sales_category = df.groupby("Category")["Sales"].sum()
plt.bar(Sales_category.index,
        Sales_category.values,
         color="#4C78A8",
         edgecolor="#3A3A3A",
         linewidth=1.2)
 
plt.title("Total Sales by Category",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Category",fontsize=12,fontweight="bold")
plt.ylabel("Total Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
 
plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)



plt.xlabel("Months", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Top10 customers by sales
plt.figure(figsize=(12, 7))

bars = plt.barh(
    Top10_customers.index,
    Top10_customers.values,
    color="#A78BFA",
    height=0.65,
    edgecolor="white",
    linewidth=0.7
)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("TOP 10 CUSTOMERS BY SALES",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Total Sales (USD)", fontsize=12, color="#38BDF8",
           fontweight="bold")
plt.ylabel("Customer Name", fontsize=12, color="#38BDF8",
           fontweight="bold")


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2,
             f"${width:,.0f}",
             va="center", ha="left",
             color="white", fontsize=9, fontweight="bold")


plt.grid(axis="x", color="#64748B",
         linestyle="--", linewidth=0.7, alpha=0.25)

plt.gca().set_axisbelow(True)
plt.gca().set_xlim(0, Top10_customers.max() * 1.18)

plt.tick_params(colors="#DCEBFA")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#3B82F6")
plt.gca().spines["bottom"].set_color("#3B82F6")

plt.tight_layout()
plt.show() 

#Region wise sales
plt.bar(Sales_region.index,
        Sales_region.values,
         color="#4C78A8",
         edgecolor="#3A3A3A",
         linewidth=1.2)

plt.title("Total Sales by Region",
          fontsize=16,
          fontweight="bold",
          pad=15,
          color="white")
plt.xlabel("Region",fontsize=12,fontweight="bold")
plt.ylabel("Sales",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)

plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.grid(axis="y", color="#64748B", linestyle="--", linewidth=0.7, alpha=0.25)

#plt.title("Monthly Sales Trend", color="white", fontsize=16, fontweight="bold")
plt.xlabel("Region", color="#38BDF8")
plt.ylabel("Sales", color="#38BDF8")
plt.tick_params(colors="#DCEBFA")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Profit by category

plt.bar(profit_category.index,
        profit_category.values,
         color="#06B6D4",
         edgecolor="#A5F3FC",
         linewidth=1.2)

plt.title("Total Profit by Category",
          fontsize=16,
          fontweight="bold",
          pad=15)
plt.xlabel("Category",fontsize=12,fontweight="bold")
plt.ylabel("Total Profit",fontsize=12,fontweight="bold")
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)

plt.gcf().set_facecolor("#080F1E")
plt.gca().set_facecolor("#14243D")

plt.grid(axis="y", color="#38BDF8", linestyle="--", linewidth=0.7, alpha=0.25)

plt.title("Profit by Category", color="#FFFFFF", fontsize=16, fontweight="bold")
plt.xlabel("Category", color="#22D3EE")
plt.ylabel("Profit", color="#22D3EE")
plt.tick_params(colors="#E0F2FE")
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show()

#Top10 products by Sales
plt.figure(figsize=(12, 7))

bars = plt.barh(
    Top10_Products.index,
    Top10_Products.values,
    color="#A78BFA",
    height=0.65,
    edgecolor="white",
    linewidth=0.7
)


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("TOP 10 Product BY SALES",
          fontsize=16, fontweight="bold", color="white", pad=20)

plt.xlabel("Total Sales (USD)", fontsize=12, color="#38BDF8",
           fontweight="bold")
plt.ylabel("Customer Name", fontsize=12, color="#38BDF8",
           fontweight="bold")


for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2,
             f"${width:,.0f}",
             va="center", ha="left",
             color="white", fontsize=9, fontweight="bold")


plt.grid(axis="x", color="#64748B",
         linestyle="--", linewidth=0.7, alpha=0.25)

plt.gca().set_axisbelow(True)
plt.gca().set_xlim(0, Top10_Products.max() * 1.18)

plt.tick_params(colors="#DCEBFA")

plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.gca().spines["left"].set_color("#3B82F6")
plt.gca().spines["bottom"].set_color("#3B82F6")

plt.tight_layout()
plt.show()

#Distribution of Sales Histogram

plt.figure(figsize=(12,7))
plt.hist(df["Sales"],
         edgecolor ="#283618",
         color="#6A994E",
         linewidth = 1.2,
        )


plt.gcf().set_facecolor("#0B1120")
plt.gca().set_facecolor("#172B45")


plt.title("Distribution Of sales by Histogram",
          fontsize = 16,
          fontweight ="bold",
          color = "#7DFFB6")

plt.xlabel("Sales",fontsize=12,fontweight="bold", color = "#35E4FF")
plt.ylabel("Frequency",fontsize=12,fontweight="bold",color="#35E4FF")
plt.tick_params(axis="both", colors="#E2E8F0", labelsize=11)
plt.grid(axis="y",
         linestyle="--",
         linewidth=0.7,
         alpha=0.35)
plt.grid(axis="x",visible=False)
plt.tight_layout()
plt.show() 

#profit distribution by boxplot
plt.figure(figsize=(10, 6), facecolor="#0B1530")

ax = plt.gca()
ax.set_facecolor("#111F3D")

plt.boxplot(
    df["Profit"].dropna(),
    patch_artist=True,
    widths=0.4,

    boxprops=dict(
        facecolor="#00B4D8",
        edgecolor="#FFFFFF",
        linewidth=1.5
    ),

    medianprops=dict(
        color="#FFD700",
        linewidth=2.5
    ),

    whiskerprops=dict(
        color="#FFFFFF",
        linewidth=1.5
    ),

    capprops=dict(
        color="#FFFFFF",
        linewidth=1.5
    ),

    flierprops=dict(
        marker="o",
        markerfacecolor="#FF4B5C",
        markeredgecolor="#FFFFFF",
        markersize=5,
        alpha=0.8
    )
)

# Title
plt.title(
    "Profit Distribution by Box Plot",
    fontsize=17,
    fontweight="bold",
    color="#FFFFFF",
    pad=18
)

# Axis Labels
plt.xlabel("Profit", fontsize=12, color="#FFFFFF", labelpad=10)
plt.ylabel("Profit Amount", fontsize=12, color="#FFFFFF", labelpad=10)

#plt.xticks([1], ["Profit"], color="white", fontsize=11)
plt.yticks(color="white", fontsize=10)

# Grid
plt.grid(
    axis="y",
    linestyle="--",
    linewidth=0.7,
    color="#8FAADC",
    alpha=0.25
)

# Axis borders
for spine in ax.spines.values():
    spine.set_color("#8FAADC")
    spine.set_linewidth(1)

ax.tick_params(axis="both", colors="white")

plt.tight_layout()
plt.show()

#correlation of all numeric columns by Heatmap
new_numeric_cols = [
    'Sales',
    'Quantity',
    'Discount',
    'Profit',
    'Unit Price',
    'Total Sales',
    'Profit Margin(%)',
    'Discount Amount',
    'Net Sales'
]

#correlation matrix
correlation_matrix = df[new_numeric_cols].corr()
print("Correlation of matrix:- ",correlation_matrix)
plt.figure(figsize=(12, 8), facecolor="#0B1530")

ax = plt.gca()
ax.set_facecolor("#111F3D")

sns.heatmap(
    correlation_matrix,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    center=0,
    linewidths=1.5,
    linecolor="#0B1530",
    square=True,
    annot_kws={
        "size": 11,
        "weight": "bold",
        "color": "white"
    },
    cbar_kws={
        "shrink": 0.85,
        "label": "Correlation Strength"
    }
)

plt.title(
    "Correlation Heatmap",
    fontsize=19,
    fontweight="bold",
    color="white",
    pad=20
)

plt.xticks(
    rotation=35,
    ha="right",
    fontsize=10,
    color="white",
    fontweight="bold"
)

plt.yticks(
    rotation=0,
    fontsize=10,
    color="white",
    fontweight="bold"
)

# Colorbar styling
cbar = ax.collections[0].colorbar
cbar.ax.yaxis.label.set_color("white")
cbar.ax.tick_params(colors="white")
cbar.ax.yaxis.label.set_size(11)

plt.tight_layout()
plt.show()


# Create figure
plt.figure(figsize=(10, 7), facecolor="#0B1530")

# Plot area
ax = plt.gca()
ax.set_facecolor("#111F3D")

# Pie Chart
wedges, texts, autotexts = plt.pie(
    Sales_category,
    labels=Sales_category.index,
    autopct='%1.1f%%',
    startangle=140,
    explode=(0.05, 0.05, 0.05),
    shadow=True,
    colors=["#00B4D8", "#FFD166", "#FF4B5C"],
    wedgeprops=dict(edgecolor="#0B1530", linewidth=2),
    textprops=dict(color="white", fontsize=12, fontweight="bold"),
    pctdistance=0.65,
    labeldistance=1.12
)

# Percentage styling
for autotext in autotexts:
    autotext.set_color("#0B1530")
    autotext.set_fontsize(11)
    autotext.set_fontweight("bold")

# Title
plt.title(
    "Sales Distribution by Product Category",
    fontsize=17,
    fontweight="bold",
    color="white",
    pad=20
)

plt.tight_layout()
plt.show()

#pair plot
sns.set_theme(style="darkgrid")

pair = sns.pairplot(
    df[["Sales","Profit","Quantity","Discount"]].sample(
        2000, random_state=42
    ),
    diag_kind="kde",
    plot_kws={"color": "#00B4D8", "alpha": 0.5},
    diag_kws={"color": "#00D4FF", "fill": True}
)

pair.fig.set_facecolor("#0B1628")

for ax in pair.axes.flat:
    if ax is not None:
        ax.set_facecolor("#142D4E")
        ax.tick_params(colors="white")
        ax.xaxis.label.set_color("white")
        ax.yaxis.label.set_color("white")

pair.fig.suptitle(
    "Pair Plot - Numerical Variables",
    color="white",
    fontsize=17,
    fontweight="bold",
    y=1.02
)

plt.show()

#violin plot
plt.figure(figsize=(11, 6), facecolor="#0B1628")

ax = sns.violinplot(
    data=df,
    x="Category",
    y="Profit",
    palette=["#00B4D8", "#5865F2", "#A855F7"],
    inner="quartile",
    linewidth=1.5
)

ax.set_facecolor("#142D4E")

ax.set_title(
    "Profit Distribution by Product Category",
    color="white",
    fontsize=16,
    fontweight="bold",
    pad=20
)

ax.set_xlabel("Product Category", color="white", fontsize=12)
ax.set_ylabel("Profit", color="white", fontsize=12)

ax.tick_params(axis="both", colors="white")

ax.grid(axis="y", alpha=0.2, linestyle="--")

for spine in ax.spines.values():
    spine.set_color("#405675")

plt.tight_layout()
plt.show() """