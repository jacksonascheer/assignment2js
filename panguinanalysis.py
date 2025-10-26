"""penguin_analysis.py
Performs basic descriptive analysis of the penguins dataset.
"""

import pandas as pd

# Load dataset
data = pd.read_csv("penguins.csv")

# Display basic info
print("Dataset summary:")
print(data.info())

# Descriptive statistics
desc = data.describe()
desc.to_csv("penguins_summary.csv")
print("Summary statistics saved as penguins_summary.csv")

# Example plot
import matplotlib.pyplot as plt
plt.figure()
data["species"].value_counts().plot(kind="bar", title="Count of Penguins by Species")
plt.xlabel("Species")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("species_count.png")
print("Plot saved as species_count.png")
