import pandas as pd
import matplotlib.pyplot as plt

# Data from your table
data = {
    'Quarter': ['Q4-2024', 'Q1-2025', 'Q2-2025', 'Q3-2025', 'Q4-2025'],
    'Total Deliveries': [495570, 336681, 384122, 497099, 418227],
    'Active FSD Subscriptions (mil)': [0.8, 0.8, 0.9, 1.0, 1.1]
}

df = pd.DataFrame(data)
df.set_index('Quarter', inplace=True)

# Create the chart
fig, ax1 = plt.subplots(figsize=(11, 6.5))

# Left axis: Deliveries (bars)
ax1.bar(df.index, df['Total Deliveries'], color='teal', alpha=0.75, width=0.6, label='Total Deliveries')
ax1.set_ylabel('Total Vehicle Deliveries', color='teal', fontsize=12)
ax1.tick_params(axis='y', labelcolor='teal')
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# Right axis: FSD Subscriptions (line)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Active FSD Subscriptions (mil)'], 
         marker='o', color='purple', linewidth=2.8, markersize=9, 
         label='Active FSD Subscriptions (millions)')
ax2.set_ylabel('Active FSD Subscriptions (millions)', color='purple', fontsize=12)
ax2.tick_params(axis='y', labelcolor='purple')

# Titles and layout
fig.suptitle('Tesla: Quarterly Total Deliveries vs Active FSD Subscriptions\nQ4 2024 – Q4 2025', 
             fontsize=15, fontweight='bold', y=0.96)
fig.legend(loc='upper center', bbox_to_anchor=(0.5, -0.04), ncol=2, fontsize=11)

plt.xticks(rotation=30)
plt.tight_layout(rect=[0, 0.08, 1, 0.92])
plt.show()

# Optional: Save as PNG
plt.savefig('tesla_quarterly_deliveries_vs_fsd.png', dpi=300, bbox_inches='tight')
print("Chart saved as 'tesla_quarterly_deliveries_vs_fsd.png'")