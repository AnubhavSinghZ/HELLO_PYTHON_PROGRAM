sandwiches_orders=['desert', 'raw', 'cold', 'warm']
finished_sandwiches=[]
while sandwiches_orders:
    orders=sandwiches_orders.pop()
    print(f"\nI made your {orders} sandwich")
    finished_sandwiches.append(orders)

for orders in finished_sandwiches:
    print(f"{orders} was made")