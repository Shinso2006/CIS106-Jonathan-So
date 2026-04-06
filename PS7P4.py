# Assuming 'orders.txt' exists with format: Item \n Qty \n Price
total_ext_price = 0
order_count = 0

try:
    with open("orders.txt", "r") as f:
        while True:
            item = f.readline().strip()
            if not item: break
            qty = int(f.readline().strip())
            price = float(f.readline().strip())
            
            ext_price = qty * price
            total_ext_price += ext_price
            order_count += 1
            
            print(f"Item: {item} | Qty: {qty} | Price: ${price:.2f} | Ext: ${ext_price:.2f}")
            
    avg_order = total_ext_price / order_count if order_count > 0 else 0
    print(f"\nTotal: ${total_ext_price:.2f} | Count: {order_count} | Average: ${avg_order:.2f}")
except FileNotFoundError:
    print("Please create 'orders.txt' first.")
