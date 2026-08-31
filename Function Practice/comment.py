# This is a single-line comment describing the code block below
def calculate_total(price, tax_rate):
    """
    This multi-line string is a 'docstring'.
    It documents what the function does.
    
    Args:
        price (float): The base cost of the item.
        tax_rate (float): The tax percentage (e.g., 0.05 for 5%).
    Returns:
        float: The final total cost including tax.
    """
    tax_amount = price * tax_rate  # This is an inline comment explaining this specific line
    
    # Calculate and return the final result
    total = price + tax_amount
    return total

# Call the function and print the result
final_price = calculate_total(100, 0.08)
print(final_price)