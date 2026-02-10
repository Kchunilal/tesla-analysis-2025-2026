import matplotlib.pyplot as plt

# Data (using midpoints for ranges: 180 for 175-185, 125 for 115-135, 20 for 20+)
companies = ['Alphabet', 'Amazon', 'Meta', 'Microsoft', 'Tesla', 'Apple']
capex_2026 = [180, 146, 125, 105, 20, 14]

# Create horizontal bar chart
plt.figure(figsize=(10, 6))
bars = plt.barh(companies, capex_2026, color='cornflowerblue')

# Add value labels on the bars
for bar in bars:
    width = bar.get_width()
    plt.text(width + 2, bar.get_y() + bar.get_height()/2,
             f'${width}B', va='center', fontsize=10, fontweight='bold')

plt.xlabel('Planned Capital Expenditures 2026 ($ billion)')
plt.title('2026 Planned CapEx – Big Tech & Tesla')
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()