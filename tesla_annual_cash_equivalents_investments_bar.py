# tesla_annual_cash_equivalents_investments_bar.py
# Bar chart: Tesla Cash, Cash Equivalents & Investments (Year-End 2021–2025)

import pandas as pd
import matplotlib.pyplot as plt

# Data from Tesla Q4 2025 Shareholder Update & historical reports
data = {
    'Year': [2021, 2022, 2023, 2024, 2025],
    'Cash, Cash Equivalents & Investments ($B)': [17.7, 22.2, 29.1, 36.6, 44.1]
}

df = pd.DataFrame(data)

# Create the bar chart
fig, ax = plt.subplots(figsize=(10, 6.5))

bars = ax.bar(df['Year'], df['Cash, Cash Equivalents & Investments ($B)'], 
              color=['#1f77b4', '#1f77b4', '#1f77b4', '#1f77b4', '#2ca02c'],  # Highlight 2025
              alpha=0.85, width=0.65)

# Styling
ax.set_title('Tesla Cash, Cash Equivalents & Investments\n(Year-End 2021–2025)', 
             fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Year', fontsize=13)
ax.set_ylabel('$ Billions', fontsize=13)
ax.set_xticks(df['Year'])
ax.set_xticklabels(df['Year'].astype(int), fontsize=12)
ax.set_ylim(0, 50)  # Headroom for labels
ax.grid(axis='y', linestyle='--', alpha=0.5, zorder=0)
ax.set_axisbelow(True)

# Add value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 0.8, 
            f'${height:.1f}B', 
            ha='center', va='bottom', fontsize=12, fontweight='bold', color='black')

# Note / subtitle
ax.text(0.5, -0.12, 'Source: Tesla Q4 2025 Shareholder Update\n2025: ~$44.1B (+21% YoY)', 
        ha='center', va='top', fontsize=10, color='gray', transform=ax.transAxes)

plt.tight_layout()
plt.show()

# Save high-res PNG to your folder
plt.savefig('tesla_annual_cash_equivalents_investments_2021-2025.png', 
            dpi=300, bbox_inches='tight')
print("Chart saved as 'tesla_annual_cash_equivalents_investments_2021-2025.png'")