from main import *
import matplotlib.pyplot as plt

open_browser()
accept_cookies()
prices = get_last_price(3)
calculate_mean(prices)
calculate_standard_deviation(prices)
calculate_mode(prices)
calculate_median(prices)
calculate_variance(prices)
calculate_skewness(prices)
calculate_kurtosis(prices)
calculate_range(prices)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

axes[0].hist(prices, bins=15, color='skyblue', edgecolor='black')
axes[0].set_title('Histogram')
axes[0].set_xlabel('Value')
axes[0].set_ylabel('Frequency')

# Scatterplot on the right subplot
axes[1].scatter(range(len(prices)), prices, color='orange', alpha=0.7)
axes[1].set_title('Scatterplot')
axes[1].set_xlabel('X values')
axes[1].set_ylabel('Y values')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()

