import matplotlib.pyplot as plt
import numpy as np

# Data (in $B)
years = ['2024', '2025']
ford_revenue = [185, 187.3]
tesla_revenue = [97.7, 94.8]
ford_net_income = [5.9, -8.2]
tesla_net_income = [7.1, 3.8]

# Bar chart for Total Revenue
x = np.arange(len(years))  # Label locations
width = 0.35  # Bar width

fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, ford_revenue, width, label='Ford', color='blue')
rects2 = ax.bar(x + width/2, tesla_revenue, width, label='Tesla', color='green')

ax.set_xlabel('Year')
ax.set_ylabel('Revenue ($B)')
ax.set_title('Full-Year Revenue Comparison (2024-2025)')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
plt.show()

# Bar chart for GAAP Net Income/Loss
fig, ax = plt.subplots(figsize=(8, 5))
rects1 = ax.bar(x - width/2, ford_net_income, width, label='Ford', color='blue')
rects2 = ax.bar(x + width/2, tesla_net_income, width, label='Tesla', color='green')

ax.set_xlabel('Year')
ax.set_ylabel('Net Income ($B)')
ax.set_title('Full-Year GAAP Net Income Comparison (2024-2025)')
ax.set_xticks(x)
ax.set_xticklabels(years)
ax.legend()
plt.show()