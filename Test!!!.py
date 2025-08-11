import matplotlib.pyplot as plt
import pandas as pd
import dataModule as dm

data = pd.read_csv("Big Mac.csv")

columnHeads = [list(data.columns.values)]
columnHeads["Price Difference"] = toNum(columnHeads["Price Difference"], "%")
columnHeads = columnHeads[0] #The function before returns a list in a list. 
settingsAvailable = {}
for i in columnHeads:
    settingsAvailable[i] = True

active = [k for k, v in settingsAvailable.items() if v and k in data.columns]
if not active:
    raise ValueError("No active series to plot.")

# Example: first half on left y-axis, second half on right y-axis.
# Adjust these lists to your needs (e.g., by units or magnitude).
mid = len(active) // 2 or 1
left_keys = active[:mid]
right_keys = active[mid:]

fig, ax = plt.subplots(figsize=(10, 5), constrained_layout=True)
x = data["Country"]

# Left axis
left_lines = []
for col in left_keys:
    ln, = ax.plot(x, data[col], marker='o', linewidth=1.8, label=col)
    left_lines.append(ln)

ax.set_xlabel("Country")
ax.set_ylabel(", ".join(left_keys))

# Right axis
ax2 = ax.twinx()
right_lines = []
for col in right_keys:
    ln, = ax2.plot(x, data[col], marker='s', linewidth=1.8, linestyle='--', label=col)
    right_lines.append(ln)

ax2.set_ylabel(", ".join(right_keys))

# Legend combining both axes
lines = left_lines + right_lines
labels = [l.get_label() for l in lines]
ax.legend(lines, labels, loc="best")

ax.grid(True, alpha=0.3)
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

plt.show()
