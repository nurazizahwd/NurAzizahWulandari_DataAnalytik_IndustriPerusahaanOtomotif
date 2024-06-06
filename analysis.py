import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template

# 1. Pembacaan Data
df_model = pd.read_csv("data/model_mobil.csv")
df_production = pd.read_csv("data/produksi_tahunan.csv")
df_sales = pd.read_csv("data/penjualan_tahunan.csv")
df_inventory = pd.read_csv("data/persediaan_mobil.csv")

# 2. Penggabungan Data
df_merged = pd.merge(df_model, df_production, on="Model")
df_merged = pd.merge(df_merged, df_sales, on=["Model", "Year"])
df_merged = pd.merge(df_merged, df_inventory, on="Model")

# 3. EDA (Exploratory Data Analysis)
print("Informasi Data Gabungan:")
print(df_merged.info())
print("\nData Gabungan:")
print(df_merged.head())

# 4. Analisis Data
# Menghitung jumlah produksi, penjualan, dan persediaan untuk setiap merek
df_brand_analysis = df_merged.groupby("Brand").agg({
    "Production": "sum",
    "Sales": "sum",
    "Inventory": "sum"
}).reset_index()

# 5. Inisialisasi Aplikasi Flask
app = Flask(__name__)

@app.route('/')
def index():
    # Visualisasi 3D menggunakan Plotly
    data_3d = [
        go.Scatter3d(
            x=df_merged['Production'],
            y=df_merged['Sales'],
            z=df_merged['Inventory'],
            mode='markers',
            marker=dict(
                size=5,
                color=df_merged['Production'],  # Warna berdasarkan nilai produksi
                colorscale='Viridis',
                opacity=0.8
            )
        )
    ]

    layout_3d = go.Layout(
        title='3D Scatter Plot Produksi vs Penjualan vs Persediaan',
        scene=dict(
            xaxis=dict(title='Production'),
            yaxis=dict(title='Sales'),
            zaxis=dict(title='Inventory')
        )
    )

    fig_3d = go.Figure(data=data_3d, layout=layout_3d)
    plot_div_3d = fig_3d.to_html(full_html=False)

    # Bar Chart Penjualan berdasarkan Merek
    bar_chart = go.Figure(data=[
        go.Bar(name='Sales', x=df_brand_analysis['Brand'], y=df_brand_analysis['Sales'])
    ])
    bar_chart.update_layout(title='Penjualan Mobil per Merek', xaxis_title='Merek', yaxis_title='Penjualan')
    plot_div_bar = bar_chart.to_html(full_html=False)

    # Pie Chart Penjualan berdasarkan Merek
    pie_chart = go.Figure(data=[
        go.Pie(labels=df_brand_analysis['Brand'], values=df_brand_analysis['Sales'], hole=.3)
    ])
    pie_chart.update_layout(title='Persentase Penjualan Mobil berdasarkan Merek')
    plot_div_pie = pie_chart.to_html(full_html=False)

    return render_template('index.html', plot_div_3d=plot_div_3d, plot_div_bar=plot_div_bar, plot_div_pie=plot_div_pie)

if __name__ == '__main__':
    app.run(debug=True)
