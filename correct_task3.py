def average_valid_measurements(values):
    if not values:
        raise ValueError("Cannot calculate average: values list is empty")
    
    total = 0
    valid_count = 0
    
    for v in values:
        if v is not None:
            try:
                total += float(v)
                valid_count += 1
            except (ValueError, TypeError):
                continue
    
    if valid_count == 0:
        raise ValueError("Cannot calculate average: no valid measurements")
    
    return total / valid_count
