import matplotlib.pyplot as plt
import numpy as np

companies = ['Alphabet', 'Amazon', 'Meta', 'Microsoft', 'Tesla', 'Apple']
capex = [180, 146, 125, 105, 20, 14]           # midpoints for ranges
growth = [102, 18, 93, 64, 135, 10]            # YoY %

x = np.arange(len(companies))
width = 0.35

fig, ax1 = plt.subplots(figsize=(11, 6))

# Bar for CapEx
bars = ax1.bar(x - width/2, capex, width, label='CapEx 2026 ($B)', color='skyblue')
ax1.set_xlabel('Company')
ax1.set_ylabel('CapEx 2026 ($ billion)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticks(x)
ax1.set_xticklabels(companies, rotation=45, ha='right')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'${height}B', ha='center', va='bottom', fontsize=9)

# Second axis for YoY growth
ax2 = ax1.twinx()
ax2.plot(x + width/2, growth, color='darkred', marker='o', linewidth=2.5, label='YoY Growth (%)')
ax2.set_ylabel('YoY Growth (%)', color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Add % labels above points
for i, val in enumerate(growth):
    ax2.text(x[i] + width/2, val + 4 if val > 50 else val - 10,
             f'{val}%', ha='center', va='bottom' if val > 50 else 'top',
             color='darkred', fontsize=9, fontweight='bold')

fig.suptitle('2026 Planned Capital Expenditures & YoY Growth', fontsize=14)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.02), ncol=2)
plt.tight_layout()
plt.show()