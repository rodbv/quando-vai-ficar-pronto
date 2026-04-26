import matplotlib.pyplot as plt
import numpy as np

# Exemplo de dados fictícios para SLE
cycle_times = np.array(
    [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
)

plt.figure(figsize=(10, 2))
plt.scatter(cycle_times, np.ones_like(cycle_times), color="#0050b0", s=80, alpha=0.7)

# Linhas verticais para percentis
for p, color in zip([50, 85, 95], ["#00b050", "#ff9900", "#d62728"]):
    perc = np.percentile(cycle_times, p)
    plt.axvline(perc, color=color, linestyle="--", lw=2, label=f"P{p}")

plt.yticks([])
plt.xlabel("Dias para concluir um item")
plt.title("Distribuição dos Cycle Times (SLE)")
plt.legend()
plt.tight_layout()
plt.show()
