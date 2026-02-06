def count_change(change: list) -> str:
    total_change = 0.00
    for i in change:
        total_change += i/100
    return f"${total_change:.2f}"