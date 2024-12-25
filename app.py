import pandas as pd

# Load the diamonds dataset
csv_url = "https://raw.githubusercontent.com/dev-area/DS/master/diamonds.csv"
diamonds_df = pd.read_csv(csv_url)

# 1. Highest diamond price
highest_price = diamonds_df['price'].max()

# 2. Average diamond price
average_price = diamonds_df['price'].mean()

# 3. Number of diamonds with "Ideal" cut
ideal_count = diamonds_df[diamonds_df['cut'] == 'Ideal'].shape[0]

# 4. Count and list of unique diamond colors
unique_colors = diamonds_df['color'].unique()
color_count = len(unique_colors)

# 5. Highest carat for diamonds of type "Premium"
highest_premium_carat = diamonds_df[diamonds_df['cut'] == 'Premium']['carat'].max()

# 6. Average carat for each cut
average_carat_by_cut = diamonds_df.groupby('cut')['carat'].mean()

# 7. Average price for each color
average_price_by_color = diamonds_df.groupby('color')['price'].mean()

# Display Results
print(f"1. Highest diamond price: ${highest_price}")
print(f"2. Average diamond price: ${average_price:.2f}")
print(f"3. Number of 'Ideal' cut diamonds: {ideal_count}")
print(f"4. Number of unique colors: {color_count}")
print(f"   Colors: {list(unique_colors)}")
print(f"5. Highest carat for 'Premium' cut: {highest_premium_carat}")
print(f"6. Average carat for each cut:\n{average_carat_by_cut}")
print(f"7. Average price for each color:\n{average_price_by_color}")