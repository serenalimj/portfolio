"""New teaching reconstruction inspired by Serena Li's 2024 project description.
This is not the original source code. All data are simulated.
Requires: numpy, pandas, matplotlib. Run: python econometrics-python.py
"""
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
fig, axes = plt.subplots(1, 3, figsize=(16, 5), layout="constrained")
fig.patch.set_facecolor("#f0f2f3")
ink, blue = "#263547", "#526b87"

# 1. Regression: Y = 2 + X + noise.
x = rng.uniform(0, 10, 80)
df = pd.DataFrame({"x": x, "y": 2 + x + rng.normal(0, 2, len(x))})
slope, intercept = np.polyfit(df["x"], df["y"], 1)
axes[0].scatter(df["x"], df["y"], color=blue, alpha=0.65)
axes[0].plot([0, 10], [intercept, intercept + 10 * slope], color=ink,
             label=f"OLS slope: {slope:.2f}")
axes[0].plot([0, 10], [2, 12], "--", color=blue, label="True relationship")
axes[0].set(xlabel="Explanatory variable X", ylabel="Outcome Y", title="Regression")
axes[0].legend()

# 2. Two-sided one-sample z-test, known population sigma = 1.
values = rng.normal(0.3, 1, 40)
mu0, sigma = 0, 1
se = sigma / math.sqrt(len(values))
z = (values.mean() - mu0) / se
p_value = math.erfc(abs(z) / math.sqrt(2))
grid = np.linspace(min(-4, z - 0.5), max(4, z + 0.5), 1000)
density = np.exp(-grid ** 2 / 2) / math.sqrt(2 * math.pi)
critical = 1.959963984540054  # two-sided alpha = 0.05
axes[1].plot(grid, density, color=blue)
axes[1].fill_between(grid, density, where=np.abs(grid) >= critical,
                     color=blue, alpha=0.3)
axes[1].axvline(z, color=ink, label=f"Observed z: {z:.2f}")
axes[1].set(xlabel="Z statistic under H0", ylabel="Density",
            title=f"Known-sigma z-test: p = {p_value:.4f}")
axes[1].legend()

# 3. Right-skewed exponential observations.
distribution = rng.exponential(1, 300)
axes[2].hist(distribution, bins=18, color=blue, edgecolor="#f0f2f3")
axes[2].axvline(distribution.mean(), color=ink, label="Sample mean")
axes[2].set(xlabel="Observed value", ylabel="Count", title="Data distributions")
axes[2].legend()
for ax in axes:
    ax.set_facecolor("#fafbfc")
    ax.spines[["top", "right"]].set_visible(False)
plt.show()
