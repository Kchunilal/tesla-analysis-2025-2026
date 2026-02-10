# cumulative_deliveries_vs_fsd_line.py
import pandas as pd
import matplotlib.pyplot as plt

# Data directly from the shareholder deck (year-end values)
data = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Cumulative Deliveries (mil)': [2.3, 3.7, 5.5, 7.3, 8.9],
    'Active FSD Subscriptions (mil)': [0.4, 0.5, 0.6, 0.8, 1.1]
}

df = pd.DataFrame(data)
df.set_index('Year', inplace=True)

# Create the figure
fig, ax1 = plt.subplots(figsize=(11, 6.5))

# Left axis: Cumulative Deliveries (solid line with markers)
ax1.plot(df.index, df['Cumulative Deliveries (mil)'], 
         marker='o', markersize=9, linewidth=2.8, 
         color='#1f77b4', label='Cumulative Deliveries (millions)')
ax1.set_ylabel('Cumulative Deliveries (millions)', color='#1f77b4', fontsize=13)
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_ylim(0, 10)
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Right axis: Active FSD Subscriptions (dashed line with markers)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Active FSD Subscriptions (mil)'], 
         marker='s', markersize=9, linewidth=2.8, linestyle='--',
         color='#ff7f0e', label='Active FSD Subscriptions (millions)')
ax2.set_ylabel('Active FSD Subscriptions (millions)', color='#ff7f0e', fontsize=13)
ax2.tick_params(axis='y', labelcolor='#ff7f0e')
ax2.set_ylim(0, 1.3)

# Titles and styling
fig.suptitle('Tesla: Cumulative Vehicle Deliveries vs Active FSD Subscriptions\nYear-End 2021–2025', 
             fontsize=16, fontweight='bold', y=0.96)

ax1.set_xlabel('Year', fontsize=13)
ax1.set_xticks(df.index)
ax1.set_xticklabels(df.index.astype(int), fontsize=12)

# Combined legend below the plot
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig.legend(lines1 + lines2, labels1 + labels2, 
           loc='upper center', bbox_to_anchor=(0.5, -0.05), ncol=2, fontsize=12)

plt.tight_layout(rect=[0, 0.08, 1, 0.92])
plt.show()

# Save high-res PNG to your project folder
plt.savefig('tesla_cumulative_deliveries_vs_fsd_2021-2025.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'tesla_cumulative_deliveries_vs_fsd_2021-2025.png'")