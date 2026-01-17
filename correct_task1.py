def calculate_average_order_value(orders):
    if not orders:
        raise ValueError("Cannot calculate average: orders list is empty")
    
    total = 0
    valid_count = 0
    
    for order in orders:
        if order["status"] != "cancelled":
            total += order["amount"]
            valid_count += 1
    
    if valid_count == 0:
        raise ValueError("Cannot calculate average: no non-cancelled orders")
    
    return total / valid_count
