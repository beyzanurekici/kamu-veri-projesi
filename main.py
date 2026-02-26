import pandas as pd

# veriyi oku
df = pd.read_excel("issizlik.xls", engine="xlrd", skiprows=4)

# sütun isimlerini basitleştir
df.columns = ["yil", "toplam", "issizlik"]

# ilk satır gereksiz (Toplam-Total) → sil
df = df.iloc[1:]

# sadece lazım olan sütunlar
df = df[["yil", "issizlik"]]

print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

# Grafik stilini ayarla
sns.set(style="whitegrid")

# Grafik oluştur
plt.figure(figsize=(10,6))
sns.lineplot(data=df, x="yil", y="issizlik", marker="o", color="blue")

plt.title("Türkiye İşsizlik Oranı (2014-2018)", fontsize=16)
plt.xlabel("Yıl", fontsize=12)
plt.ylabel("İşsizlik Oranı (%)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Grafiği kaydet
plt.savefig("issizlik_grafik.png")

# Göster
plt.show()