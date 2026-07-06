import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Product': ['Widget A', 'Widget B', 'Widget C', 'Widget D'],
    'Warehouse 1': [15, 30, 8, 45],
    'Warehouse 2': [3, 12, 6, 5],
    'Warehouse 3': [2, 7, 4, 10]
}

inventory_df = pd.DataFrame(data)

def analyze_inventory_health(df, threshold=20):
    df['Total Stock'] = df[['Warehouse 1', 'Warehouse 2', 'Warehouse 3']].sum(axis=1)
    low_stock = df[df['Total Stock'] <= threshold]
    # Visualization
    plt.figure(figsize=(6,4))
    plt.bar(low_stock['Product'], low_stock['Total Stock'], color='tomato')
    plt.xlabel('Product')
    plt.ylabel('Total Stock')
    plt.title('Low Inventory Products')
    plt.tight_layout()
    plt.show()
    # Summary
    urgent_products = low_stock['Product'].tolist()
    if urgent_products:
        summary = f"Products needing urgent restocking: {', '.join(urgent_products)}"
    else:
        summary = "No products require urgent restocking."
    print(summary)

analyze_inventory_health(inventory_df)
