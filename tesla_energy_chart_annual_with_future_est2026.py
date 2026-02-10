import matplotlib.pyplot as plt

# Historical actual data (GWh) - from Tesla official reports
years = [2021, 2022, 2023, 2024, 2025]
deployments = [4.0, 6.5, 14.7, 31.4, 46.7]

# Projection lines starting from 2025 actual
years_proj = [2025, 2026]
bear_case   = [46.7, 60]   # Lower / conservative estimate
base_case   = [46.7, 65]   # Mid-range / consensus estimate
bull_case   = [46.7, 80]   # Higher / optimistic estimate

# Create the plot
plt.figure(figsize=(10, 6))  # Nice size for viewing

# Plot historical data as solid line with markers
plt.plot(years, deployments, marker='o', color='blue', linewidth=2.5, 
         markersize=8, label='Actual Deployments (2021–2025)')

# Plot projection scenarios as dashed lines
plt.plot(years_proj, bear_case, linestyle='--', color='red', marker='o', 
         markersize=8, label='Bear Case 2026: 60 GWh')
plt.plot(years_proj, base_case, linestyle='--', color='green', marker='o', 
         markersize=8, label='Base Case 2026: 65 GWh')
plt.plot(years_proj, bull_case, linestyle='--', color='orange', marker='o', 
         markersize=8, label='Bull Case 2026: 80 GWh')

# Customize the chart
plt.title('Tesla Annual Energy Storage Deployments (GWh)\nwith 2026 Estimates', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Deployments (GWh)', fontsize=12)
plt.xticks(range(2021, 2027))  # Show every year clearly
plt.ylim(0, 90)                # Give headroom for the bull case
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper left', fontsize=10, frameon=True)

# Add a note about sources
plt.figtext(0.01, 0.01, 'Data 2021–2025: Tesla official reports | 2026 estimates: analyst consensus & growth scenarios', 
            ha='left', fontsize=9, color='gray')

plt.tight_layout()
plt.show()