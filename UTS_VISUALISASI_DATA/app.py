from pathlib import Path

import streamlit as st
import pandas as pd
import plotly.express as px

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "dataset"

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Dashboard Penjualan",
    page_icon="📊",
    layout="wide"
)

# Satu palet warna untuk semua grafik (konsisten)
PALETTE = px.colors.qualitative.Set2

# JUDUL DASHBOARD
st.title("📊 Dashboard Analisis Penjualan")
st.caption("Visualisasi Data - Ujian Tengah Semester 2026/2027")


# MEMBACA & MEMBERSIHKAN DATASET
@st.cache_data
def load_data():
    # Cari file CSV di folder dataset (dari lokasi app.py, bukan lokasi cmd)
    candidates = sorted(DATA_DIR.glob("*.csv*"))
    if not candidates:
        raise FileNotFoundError(str(DATA_DIR))

    df = pd.read_csv(candidates[0], encoding="latin1")

    # Pembersihan data
    df.columns = df.columns.str.strip()
    df = df.drop_duplicates()

    df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    df["Sales"] = pd.to_numeric(df["Sales"], errors="coerce")
    df["Profit"] = pd.to_numeric(df["Profit"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

    df = df.dropna(subset=["Order Date", "Sales", "Profit", "Quantity"])

    return df


try:
    df = load_data()

    # SIDEBAR FILTER
    st.sidebar.header("🔎 Filter Data")

    regions = ["Semua"] + sorted(df["Region"].dropna().unique().tolist())
    selected_region = st.sidebar.selectbox("Pilih Wilayah", regions)

    categories = ["Semua"] + sorted(df["Category"].dropna().unique().tolist())
    selected_category = st.sidebar.selectbox("Pilih Kategori", categories)

    filtered = df.copy()

    if selected_region != "Semua":
        filtered = filtered[filtered["Region"] == selected_region]

    if selected_category != "Semua":
        filtered = filtered[filtered["Category"] == selected_category]

    if filtered.empty:
        st.warning("Tidak ada data untuk filter yang dipilih.")

    else:
        # KPI CARDS
        st.subheader("Ringkasan Penjualan")

        col1, col2, col3, col4 = st.columns(4)

        total_sales = filtered["Sales"].sum()
        total_profit = filtered["Profit"].sum()
        total_transactions = len(filtered)
        average_sales = filtered["Sales"].mean()

        col1.metric("Total Penjualan", f"${total_sales:,.2f}")
        col2.metric("Total Profit", f"${total_profit:,.2f}")
        col3.metric("Total Transaksi", f"{total_transactions:,}")
        col4.metric("Rata-rata Penjualan", f"${average_sales:,.2f}")

        st.divider()

        # GRAFIK 1: TREN PENJUALAN
        st.subheader("1. Tren Penjualan Berdasarkan Waktu")

        monthly = (
            filtered
            .set_index("Order Date")
            .resample("MS")["Sales"]
            .sum()
            .reset_index()
        )

        fig1 = px.line(
            monthly,
            x="Order Date",
            y="Sales",
            markers=True,
            title="Tren Penjualan Bulanan",
            color_discrete_sequence=PALETTE
        )
        fig1.update_layout(xaxis_title="Bulan", yaxis_title="Total Penjualan (USD)")
        st.plotly_chart(fig1, use_container_width=True)

        # GRAFIK 2: PENJUALAN PER KATEGORI
        st.subheader("2. Penjualan Berdasarkan Kategori")

        category_sales = (
            filtered.groupby("Category")["Sales"]
            .sum()
            .reset_index()
        )

        fig2 = px.bar(
            category_sales,
            x="Category",
            y="Sales",
            color="Category",
            title="Total Penjualan per Kategori",
            color_discrete_sequence=PALETTE
        )
        fig2.update_layout(
            xaxis_title="Kategori",
            yaxis_title="Total Penjualan (USD)",
            showlegend=False
        )
        st.plotly_chart(fig2, use_container_width=True)

        # GRAFIK 3: PROPORSI WILAYAH
        st.subheader("3. Kontribusi Penjualan per Wilayah")

        region_sales = (
            filtered.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig3 = px.pie(
            region_sales,
            names="Region",
            values="Sales",
            hole=0.4,
            title="Persentase Penjualan per Wilayah",
            color_discrete_sequence=PALETTE
        )
        st.plotly_chart(fig3, use_container_width=True)

        # GRAFIK 4: HUBUNGAN PENJUALAN DAN KEUNTUNGAN
        st.subheader("4. Hubungan Penjualan dan Keuntungan")

        fig4 = px.scatter(
            filtered,
            x="Sales",
            y="Profit",
            color="Category",
            opacity=0.6,
            hover_data=["Product Name"],
            title="Korelasi Penjualan dan Profit",
            color_discrete_sequence=PALETTE
        )
        fig4.update_layout(
            xaxis_title="Penjualan (USD)",
            yaxis_title="Profit (USD)"
        )
        st.plotly_chart(fig4, use_container_width=True)

        # INSIGHT
        st.divider()
        st.subheader("💡 Analisis dan Insight")

        best_category = category_sales.loc[
            category_sales["Sales"].idxmax(), "Category"
        ]
        best_region = region_sales.loc[
            region_sales["Sales"].idxmax(), "Region"
        ]

        profit_by_cat = filtered.groupby("Category")["Profit"].sum()
        most_profit_cat = profit_by_cat.idxmax()
        least_profit_cat = profit_by_cat.idxmin()

        margin = (total_profit / total_sales * 100) if total_sales else 0
        corr = filtered["Sales"].corr(filtered["Profit"])

        st.write(
            f"""
            - Kategori dengan total penjualan tertinggi adalah **{best_category}**.
            - Wilayah dengan total penjualan tertinggi adalah **{best_region}**.
            - Kategori paling menguntungkan adalah **{most_profit_cat}**, sedangkan
              keuntungan terendah ada pada **{least_profit_cat}**.
            - Margin profit pada filter ini sebesar **{margin:.1f}%** dari total
              penjualan **${total_sales:,.2f}**.
            - Korelasi penjualan dan profit sebesar **{corr:.2f}**: penjualan besar
              belum tentu menghasilkan profit besar (perlu cek diskon dan biaya).
            """
        )

        # TABEL DATA
        with st.expander("Lihat Data Penjualan"):
            st.dataframe(filtered)

except FileNotFoundError:
    st.error(
        "Dataset tidak ditemukan. Pastikan file CSV berada di folder: "
        f"{DATA_DIR}"
    )
    st.write("Isi folder tersebut saat ini:")
    st.write([p.name for p in DATA_DIR.glob("*")] if DATA_DIR.exists()
             else "Folder 'dataset' tidak ada di lokasi ini.")

except Exception as e:
    st.error(f"Terjadi kesalahan: {e}")
