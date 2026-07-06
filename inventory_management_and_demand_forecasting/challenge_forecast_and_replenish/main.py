import matplotlib.pyplot as plt

daily_demand = [
    20, 22, 19, 23, 25, 18, 20, 24, 21, 19, 22, 20, 23, 21, 18,
    20, 25, 22, 19, 21, 24, 23, 22, 20, 18, 19, 21, 23, 20, 22
]
initial_stock = 50
replenishment_quantity = 40
window_size = 3

def moving_average_forecast(demand_list, window):
    forecasts = [None] * window
    for i in range(window, len(demand_list)):
        avg = sum(demand_list[i-window:i]) / window
        forecasts.append(avg)
    return forecasts

def calculate_reorder_point(demand_list, window):
    avg_demand = sum(demand_list[:window]) / window
    return avg_demand * window

def simulate_inventory(demand_list, forecast_list, initial_stock, reorder_qty, reorder_point):
    inventory = []
    stockouts = []
    stock = initial_stock
    for i, demand in enumerate(demand_list):
        stock -= demand
        if stock < 0:
            stockouts.append(i)
        if stock < reorder_point:
            stock += reorder_qty
        inventory.append(stock)
    return inventory, stockouts

# 1. 予測の計算
forecasted_demand = moving_average_forecast(daily_demand, window_size)

# 2. 発注点の計算
reorder_point = calculate_reorder_point(daily_demand, window_size)

# 3. 在庫シミュレーション
inventory_levels, stockout_days = simulate_inventory(
    daily_demand, forecasted_demand, initial_stock, replenishment_quantity, reorder_point
)

# 4. 可視化
days = list(range(1, len(daily_demand) + 1))
plt.figure(figsize=(12,6))
plt.plot(days, daily_demand, label="Actual Demand", marker="o")
plt.plot(days, forecasted_demand, label="Forecasted Demand (Moving Avg)", linestyle="--", marker="x")
plt.plot(days, inventory_levels, label="Inventory Level", marker="s")
plt.xlabel("Day")
plt.ylabel("Units")
plt.title("Inventory Simulation and Demand Forecasting")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# 5. 欠品日の出力
if stockout_days:
    print("Stockouts occurred on days:", ', '.join(str(d+1) for d in stockout_days))
else:
    print("No stockouts occurred during the period.")