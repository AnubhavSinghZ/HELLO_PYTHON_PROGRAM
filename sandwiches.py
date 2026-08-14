sandwiches_orders=['desert', 'raw', 'cold', 'warm']
finished_sandwiches=[]  # Empty list
while sandwiches_orders:
    orders=sandwiches_orders.pop()  # Will pop the sandwiches_orders and assign it to orders
    print(f"\nI made your {orders} sandwich")
    finished_sandwiches.append(orders)

for orders in finished_sandwiches:
    print(f"{orders} was made")