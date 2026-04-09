# Get inputs from user
current_stock = int(input())
purchased = int(input())
low_stock_threshold = int(input())
remaining = current_stock - purchased 
low_stock_alert = remaining <= low_stock_threshold
a= {'remaining': remaining, 'low_stock_alert': low_stock_alert}
print(a)
# Calculate remaining stock
# Check if low stock alert is needed
# Print result
# Use input() to get current_stock (int), purchased (int), low_stock_threshold (int).
# Print {"remaining": new_stock, "low_stock_alert": bool}.
# Stock never goes negative. Alert if remaining <= threshold.
# TODO: Implement the solution based on the instructions above