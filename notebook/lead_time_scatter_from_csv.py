import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lê o CSV diretamente
csv_path = "../data/lead_time_data_clean_2026.csv"
df = pd.read_csv(
    csv_path, header=None, names=["started_at", "finished_at", "_"], usecols=[0, 1]
)

df["started_at"] = pd.to_datetime(df["started_at"])
df["finished_at"] = pd.to_datetime(df["finished_at"])

# Calcula o lead time em dias
lead_time = (df["finished_at"] - df["started_at"]).dt.days + 1
finished_dates = df["finished_at"].dt.normalize()

# Percentis
p50 = np.percentile(lead_time, 50)
p85 = np.percentile(lead_time, 85)

plt.figure(figsize=(12, 5))
plt.scatter(finished_dates, lead_time, color="#27ae60", alpha=0.6)
plt.axhline(p50, color="#00b050", linestyle="--", lw=2, label=f"P50: {int(p50)} dias")
plt.axhline(p85, color="#0050b0", linestyle="--", lw=2, label=f"P85: {int(p85)} dias")
plt.xlabel("Data de entrega")
plt.ylabel("Lead time (dias)")
plt.title("Lead Time Scatterplot (dados reais de 2026)")
plt.legend()
plt.tight_layout()
plt.show()
