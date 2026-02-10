import matplotlib.pyplot as plt

# Data from Tesla Q4 2025 Shareholder Deck: Annual Energy Storage Deployments (GWh)
years = [2021, 2022, 2023, 2024, 2025]
deployments = [4.0, 6.5, 14.7, 31.4, 46.7]

# Create the line chart
plt.figure(figsize=(10, 6))
plt.plot(years, deployments, marker='o', linestyle='-', color='b', linewidth=2)

# Add labels and title
plt.title('Tesla Annual Energy Storage Deployments (GWh)', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deployments (GWh)', fontsize=12)
plt.xticks(years)  # Show each year on x-axis
plt.grid(True, linestyle='--', alpha=0.7)

# Annotate data points
for year, dep in zip(years, deployments):
    plt.text(year, dep + 1, f'{dep}', ha='center', fontsize=10)

# Show the plot
plt.tight_layout()
plt.show()