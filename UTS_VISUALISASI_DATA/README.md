# Dashboard Analisis Penjualan

**Nama:** Vio Amar Wiguna  
**NPM:** 241053002  
**Mata Kuliah:** Visualisasi Data – UTS Ganjil 2026/2027

## 🔗 Tautan
- **Live Dashboard:** [tempel link Streamlit Community Cloud]
- **Dataset Kaggle:** [tempel link dataset]

## Latar Belakang
Dataset Superstore dipilih karena memiliki lebih dari 1.000 data transaksi dengan berbagai informasi, seperti tanggal pemesanan, kategori produk, wilayah penjualan, jumlah penjualan, dan keuntungan. Dataset ini digunakan untuk menganalisis kategori produk dan wilayah mana yang menghasilkan penjualan serta keuntungan tertinggi, sehingga dapat membantu mengetahui strategi penjualan yang lebih efektif.

## Key Insights
1. Kategori produk dengan kontribusi penjualan tertinggi menunjukkan bahwa kategori tersebut memiliki permintaan pasar yang lebih besar dibandingkan kategori lainnya.
2. Tren penjualan bulanan menunjukkan adanya perubahan jumlah penjualan dari waktu ke waktu, sehingga dapat diketahui bulan dengan aktivitas penjualan tertinggi.
3. Wilayah dengan keuntungan terendah perlu mendapatkan perhatian karena tingginya penjualan belum tentu menghasilkan keuntungan yang besar.
4. Terdapat hubungan antara jumlah penjualan (Sales) dan keuntungan (Profit), tetapi penjualan yang tinggi tidak selalu menghasilkan keuntungan yang tinggi.
5. Hasil analisis dapat digunakan sebagai bahan pertimbangan dalam menentukan strategi penjualan, pengelolaan produk, dan pengembangan wilayah pemasaran.

## Fitur Dashboard
- 4 KPI card (penjualan, profit, transaksi, margin)
- 5 jenis chart: line, bar, donut, scatter, heatmap
- 3 filter interaktif: rentang tanggal, kategori, wilayah
- Insight otomatis yang ikut berubah mengikuti filter

## Struktur Repositori
```
├── app.py
├── clean_data.py
├── requirements.txt
├── README.md
└── data/
    └── clean_data.csv
```

## Menjalankan Secara Lokal
```bash
pip install -r requirements.txt
python clean_data.py      # opsional: bersihkan data mentah (data/raw.csv)
streamlit run app.py
```

## Pra-pemrosesan Data
Rapikan nama kolom, hapus duplikat, ubah tipe tanggal, isi nilai kosong
(median untuk angka, "Unknown" untuk kategori). Lihat `clean_data.py`.
