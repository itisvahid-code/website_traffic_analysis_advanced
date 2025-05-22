
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
date_range = pd.date_range(start="2024-01-01", periods=30, freq="D")
page_views = np.random.randint(150, 400, size=30)
unique_visitors = page_views - np.random.randint(10, 70, size=30)
bounce_rate = np.round(np.random.uniform(0.3, 0.6, size=30), 2)
avg_session_duration = np.round(np.random.uniform(1.5, 6.0, size=30), 2)  # in minutes
conversions = np.random.randint(5, 30, size=30)

# Create DataFrame
df = pd.DataFrame({
    "Date": date_range,
    "PageViews": page_views,
    "UniqueVisitors": unique_visitors,
    "BounceRate": bounce_rate,
    "AvgSessionDuration": avg_session_duration,
    "Conversions": conversions
})

# Save dataset to CSV
df.to_csv("advanced_website_traffic_data.csv", index=False)
print("✅ Dataset saved as 'advanced_website_traffic_data.csv'")

# Create output folder for charts
os.makedirs("charts", exist_ok=True)

# Plot 1: Page Views vs Unique Visitors
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["PageViews"], label="Page Views", marker="o")
plt.plot(df["Date"], df["UniqueVisitors"], label="Unique Visitors", marker="s")
plt.title("Page Views vs Unique Visitors Over Time")
plt.xlabel("Date")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/pageviews_vs_visitors.png")
plt.close()

# Plot 2: Bounce Rate & Session Duration
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["BounceRate"], label="Bounce Rate", color="orange", marker="x")
plt.plot(df["Date"], df["AvgSessionDuration"], label="Avg. Session Duration (min)", color="green", marker="^")
plt.title("Engagement Metrics Over Time")
plt.xlabel("Date")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/engagement_metrics.png")
plt.close()

# Plot 3: Daily Conversions
plt.figure(figsize=(10, 5))
plt.bar(df["Date"], df["Conversions"], color="purple")
plt.title("Daily Conversions")
plt.xlabel("Date")
plt.ylabel("Conversions")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("charts/daily_conversions.png")
plt.close()

print("📊 Charts saved in the 'charts' folder.")
