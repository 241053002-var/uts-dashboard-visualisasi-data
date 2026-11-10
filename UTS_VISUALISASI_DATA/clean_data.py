"""Pra-pemrosesan data: baca data mentah Kaggle -> simpan data bersih."""
import pandas as pd

RAW_PATH = "data/raw.csv"          # taruh file hasil download Kaggle di sini
CLEAN_PATH = "data/clean_data.csv"
DATE_COL = "order_date"            # sesuaikan dengan nama kolom tanggal (setelah di-lowercase)

try:
    df = pd.read_csv(RAW_PATH)
except UnicodeDecodeError:
    df = pd.read_csv(RAW_PATH, encoding="latin-1")

print("Baris awal:", len(df))

# 1. Rapikan nama kolom: huruf kecil, spasi/strip -> underscore
df.columns = (
    df.columns.str.strip().str.lower()
    .str.replace(r"[\s\-]+", "_", regex=True)
)

# 2. Hapus duplikat
df = df.drop_duplicates()

# 3. Ubah tipe tanggal
if DATE_COL in df.columns:
    df[DATE_COL] = pd.to_datetime(df[DATE_COL], errors="coerce")

# 4. Tangani nilai kosong: angka -> median, kategori -> "Unknown", tanggal kosong -> dibuang
num_cols = df.select_dtypes(include="number").columns
df[num_cols] = df[num_cols].fillna(df[num_cols].median())
obj_cols = df.select_dtypes(include="object").columns
df[obj_cols] = df[obj_cols].fillna("Unknown")
if DATE_COL in df.columns:
    df = df.dropna(subset=[DATE_COL])

df.to_csv(CLEAN_PATH, index=False)
print("Baris bersih:", len(df))
print("Tersimpan di", CLEAN_PATH)
