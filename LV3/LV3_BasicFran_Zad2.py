import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("mtcars.csv")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle("Mtcars grafovi", fontsize=16, fontweight="bold", y=1)

#1
ax1 = axes[0, 0]

cyl_groups = [4, 6, 8]
avg_mpg = [df[df["cyl"] == cyl]["mpg"].mean() for cyl in cyl_groups]

ax1.bar(cyl_groups, avg_mpg, width=1)

ax1.set_title("Prosjecna potrosnja po broju cilindara", fontweight="bold")
ax1.set_xlabel("Broj cilindara")
ax1.set_ylabel("Potrosnja")
ax1.set_xticks(cyl_groups)
ax1.grid(axis="y", alpha=0.3)

#2
ax2 = axes[0, 1]
data_by_cyl = [df[df["cyl"] == cyl]["wt"] * 1000 for cyl in cyl_groups]

bp = ax2.boxplot(data_by_cyl, patch_artist=True, notch=False,
medianprops=dict(color="black", linewidth=2))

ax2.set_title("Distribucija tezine automobila po broju cilindara", fontweight="bold")
ax2.set_xlabel("Broj cilindara")
ax2.set_ylabel("Tezina u lbs")
ax2.set_xticklabels([f"{c} cil." for c in cyl_groups])
ax2.grid(axis="y", alpha=0.3)

#3
ax3 = axes[1, 0]
auto_mpg = df[df["am"] == 0]["mpg"]
manual_mpg = df[df["am"] == 1]["mpg"]

bp3 = ax3.boxplot([auto_mpg, manual_mpg], patch_artist=True,
medianprops=dict(color="black", linewidth=2))
labels = ["Automatski", "Rucni"]



means = [auto_mpg.mean(), manual_mpg.mean()]
ax3.plot([1, 2], means, "D", color="blue", markersize=5,
zorder=5, label=f"Srednja vrijednost: auto={means[0]:.1f}, rucni={means[1]:.1f}")

ax3.set_title("Potrosnja rucnog i automatskog mjenjaca", fontweight="bold")
ax3.set_xlabel("Mjenjac")
ax3.set_ylabel("Potrosnja")
ax3.set_xticklabels(labels)
ax3.grid(axis="y", alpha=0.3)

#4
ax4 = axes[1, 1]

for am_val, label, color in [(0, "Automatski", "red"), (1, "Rucni", "blue")]:
    subset = df[df["am"] == am_val]
    ax4.scatter(subset["hp"], subset["qsec"],
    c=color, label=label, alpha=0.8,
    s=80, edgecolors="white", linewidth=0.8)

ax4.set_title("Ubrzanje i snaga po mjenjacu", fontweight="bold")
ax4.set_xlabel("Snaga")
ax4.set_ylabel("Ubrzanje")
ax4.legend(title="Mjenjac")
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("mtcars_analiza.png", dpi=150, bbox_inches="tight")
plt.show()
print("mtcars_analiza.png")