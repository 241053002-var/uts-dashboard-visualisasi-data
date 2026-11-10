# Dashboard Analisis Penjualan

**Nama:** [Nama Lengkap]  
**NPM:** [NPM]  
**Mata Kuliah:** Visualisasi Data – UTS Ganjil 2026/2027

## 🔗 Tautan
- **Live Dashboard:** [tempel link Streamlit Community Cloud]
- **Dataset Kaggle:** [tempel link dataset]

## Latar Belakang
Jelaskan 2–3 kalimat: kenapa dataset ini dipilih, masalah apa yang ingin dijawab
(misal: kategori & wilayah mana yang paling menguntungkan?).

## Key Insights
1. [Temuan 1, misal: kategori X menyumbang Y% penjualan]
2. [Temuan 2, misal: penjualan memuncak di bulan ...]
3. [Temuan 3, misal: wilayah Z punya margin terendah]
4. [Temuan 4 (opsional)]
5. [Temuan 5 (opsional)]

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
