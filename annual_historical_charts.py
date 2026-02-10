# annual_historical_charts.py
# Plots Tesla annual historical data (2021–2025) from tesla_annual_historical.csv
# Run this in VS Code after opening your project folder

import pandas as pd
import matplotlib.pyplot as plt

# ── 1. Load the data ─────────────────────────────────────────────────────
df = pd.read_csv('tesla_annual_historical.csv')

# Set Year as index (makes plotting easier)
df.set_index('Year', inplace=True)

# Quick check: print the loaded data
print("Annual historical data loaded:")
print(df)
print("\nColumns:", df.columns.tolist())

# ── Helper function to save charts ───────────────────────────────────────
def save_chart(fig, filename):
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved: {filename}")

# ── Chart 1: Deliveries vs Revenues (Dual Axis) – Fixed layout ───────────
fig1, ax1 = plt.subplots(figsize=(12, 7))  # Wider + taller for breathing room

# Bars: Deliveries
ax1.bar(df.index, df['Total Deliveries (millions)'], 
        color='teal', alpha=0.75, label='Deliveries (millions)', width=0.6)
ax1.set_ylabel('Deliveries (millions)', color='teal', fontsize=12)
ax1.tick_params(axis='y', labelcolor='teal')
ax1.set_ylim(0, 2.0)  # Adjust if needed
ax1.grid(axis='y', linestyle='--', alpha=0.4)

# Line: Revenues (right axis)
ax2 = ax1.twinx()
ax2.plot(df.index, df['Total Revenues ($B)'], 
         marker='o', color='blue', linewidth=3, markersize=8, 
         label='Revenues ($B)')
ax2.set_ylabel('Revenues ($B)', color='blue', fontsize=12)
ax2.tick_params(axis='y', labelcolor='blue')
ax2.set_ylim(0, 110)  # Give headroom

# Titles and legend – no overlap
fig1.suptitle('Tesla Annual Performance: Deliveries vs Revenues (2021–2025)', 
              fontsize=16, fontweight='bold', y=0.96)
ax1.set_title('First revenue decline in 2025', fontsize=11, color='gray', pad=10)

# Legend at bottom center
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
fig1.legend(lines1 + lines2, labels1 + labels2, 
            loc='lower center', bbox_to_anchor=(0.5, -0.14), 
            ncol=2, fontsize=11, frameon=True)

# Final layout adjustments
plt.xticks(df.index.astype(int), rotation=0, fontsize=11)
plt.tight_layout(rect=[0, 0.10, 1, 0.92])  # Extra bottom space for legend
plt.show(block=False)
save_chart(fig1, 'tesla_deliveries_vs_revenues_2021-2025.png')

# ── Chart 2: Energy Storage Deployed (Bar) ───────────────────────────────
fig2 = plt.figure(figsize=(10, 6))
plt.bar(df.index, df['Energy Storage Deployed (GWh)'], 
        color='orange', alpha=0.85, width=0.6)
plt.title('Annual Energy Storage Deployed (GWh)', fontsize=15, pad=15)
plt.ylabel('GWh Deployed', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(df.index.astype(int))
plt.tight_layout()
plt.show(block=False)
save_chart(fig2, 'tesla_energy_storage_annual.png')

# ── Chart 3: Gross Margin % Trend (Line) ─────────────────────────────────
fig3 = plt.figure(figsize=(10, 6))
plt.plot(df.index, df['Total GAAP Gross Margin %'], 
         marker='s', color='green', linewidth=2.5, markersize=8, 
         label='GAAP Gross Margin %')
plt.title('Annual GAAP Gross Margin %', fontsize=15, pad=15)
plt.ylabel('Gross Margin %', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.4)
plt.ylim(0, 30)
plt.xticks(df.index.astype(int))
plt.legend(fontsize=11)
plt.tight_layout()
plt.show(block=False)
save_chart(fig3, 'tesla_gross_margin_annual.png')

# ── Chart 4: Free Cash Flow (Bar) ────────────────────────────────────────
fig4 = plt.figure(figsize=(10, 6))
plt.bar(df.index, df['Free Cash Flow ($B)'], 
        color='gold', alpha=0.8, width=0.6)
plt.title('Annual Free Cash Flow ($B)', fontsize=15, pad=15)
plt.ylabel('Free Cash Flow ($B)', fontsize=12)
plt.xlabel('Year', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.4)
plt.xticks(df.index.astype(int))
plt.tight_layout()
plt.show(block=False)
save_chart(fig4, 'tesla_free_cash_flow_annual.png')

print("\nAll charts displayed (arrange windows as needed).")
print("High-resolution PNG files saved in your project folder:")
print(" - tesla_deliveries_vs_revenues_2021-2025.png")
print(" - tesla_energy_storage_annual.png")
print(" - tesla_gross_margin_annual.png")
print(" - tesla_free_cash_flow_annual.png")