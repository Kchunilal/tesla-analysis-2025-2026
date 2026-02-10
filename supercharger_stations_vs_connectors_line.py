# supercharger_stations_vs_connectors_line_improved_labels.py

import pandas as pd
import matplotlib.pyplot as plt

# Data from Tesla Q4 2025 Shareholder Deck (year-end)
data = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Supercharger Stations': [3476, 4678, 5952, 6975, 8182],
    'Supercharger Connectors (Stalls)': [31498, 42419, 54892, 65495, 77682]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

fig, ax1 = plt.subplots(figsize=(12, 7))  # Slightly wider/taller

# Stations (left axis)
ax1.plot(df.index, df['Supercharger Stations'], 
         marker='o', markersize=10, linewidth=2.8, 
         color='#1f77b4', label='Supercharger Stations')
ax1.set_ylabel('Number of Supercharger Stations', color='#1f77b4', fontsize=13)
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_ylim(0, 9500)   # Extra headroom
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Connectors (right axis)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Supercharger Connectors (Stalls)'], 
         marker='s', markersize=10, linewidth=2.8, linestyle='--',
         color='#ff7f0e', label='Connectors / Stalls')
ax2.set_ylabel('Number of Connectors (Stalls)', color='#ff7f0e', fontsize=13)
ax2.tick_params(axis='y', labelcolor='#ff7f0e')
ax2.set_ylim(0, 85000)

# Titles
fig.suptitle('Tesla Supercharger Network Growth\nStations vs Connectors (Year-End 2021–2025)', 
             fontsize=16, fontweight='bold', y=0.96)
ax1.set_xlabel('Year', fontsize=13)
ax1.set_xticks(df.index)
ax1.set_xticklabels(df.index.astype(int), fontsize=12)

# Improved, non-overlapping data labels
for year in df.index:
    val_st = df['Supercharger Stations'].loc[year]
    val_conn = df['Supercharger Connectors (Stalls)'].loc[year]
    
    # Stations label: above point, slight left nudge, larger offset
    ax1.text(year - 0.15, val_st + 350, f'{val_st:,}', 
             ha='center', va='bottom', fontsize=10, fontweight='bold', 
             color='#1f77b4', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))
    
    # Connectors label: above point, slight right nudge, much larger offset
    ax2.text(year + 0.15, val_conn + 2200, f'{val_conn:,}', 
             ha='center', va='bottom', fontsize=10, fontweight='bold', 
             color='#ff7f0e', bbox=dict(facecolor='white', alpha=0.7, edgecolor='none', pad=2))

# Legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, 
           loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=12)

plt.tight_layout(rect=[0, 0.08, 1, 0.92])
plt.show()

# Save
plt.savefig('tesla_supercharger_growth_readable_labels.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'tesla_supercharger_growth_readable_labels.png'")