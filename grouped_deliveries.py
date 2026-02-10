# grouped_deliveries_readable.py
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Data from your table
data = {
    'Quarter': ['Q4-2024', 'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025'],
    'Model 3/Y Deliveries': [471930, 323800, 373728, 481166, 406585],
    'Total Deliveries': [495570, 336681, 384122, 497099, 418227]
}

df = pd.DataFrame(data)

# Chart setup
quarters = df['Quarter']
x = np.arange(len(quarters))          # positions: 0,1,2,3,4
width = 0.35                          # bar width

fig, ax = plt.subplots(figsize=(12, 7.5))  # wider and taller for clarity

# Model 3/Y bars (left)
ax.bar(x - width/2, df['Model 3/Y Deliveries'], width, 
       label='Model 3/Y', color='#1f77b4')  # distinct blue

# Total bars (right)
ax.bar(x + width/2, df['Total Deliveries'], width, 
       label='Total', color='#ff7f0e')      # distinct orange

# ── Labels & styling ────────────────────────────────────────────────────
ax.set_title('Tesla Quarterly Vehicle Deliveries\nModel 3/Y vs Total', 
             fontsize=18, fontweight='bold', pad=20)

ax.set_xlabel('Quarter', fontsize=14)
ax.set_ylabel('Number of Vehicles Delivered', fontsize=14)

ax.set_xticks(x)
ax.set_xticklabels(quarters, rotation=0, fontsize=13)  # no rotation = easier to read

ax.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.set_axisbelow(True)

# Larger, bolder value labels on top of bars
for i in range(len(quarters)):
    # Model 3/Y
    val_m3y = df['Model 3/Y Deliveries'][i]
    ax.text(x[i] - width/2, val_m3y + 10000, f'{val_m3y:,}', 
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#1f77b4')
    
    # Total
    val_total = df['Total Deliveries'][i]
    ax.text(x[i] + width/2, val_total + 10000, f'{val_total:,}', 
            ha='center', va='bottom', fontsize=11, fontweight='bold', color='#ff7f0e')

# Legend below chart
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), 
          ncol=2, fontsize=13, frameon=True, title='Category', title_fontsize=13)

plt.tight_layout(rect=[0, 0.10, 1, 0.94])  # extra bottom space for legend
plt.show()

# Save to folder
plt.savefig('tesla_deliveries_grouped_readable.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'tesla_deliveries_grouped_readable.png'")