# Get inputs from user
current = int(input())
total = int(input())
label = input() or "Loading"
filled = "#" * current
empty = "." * (total-current)
percentage = current *100/total
print(f"[{filled}{empty}] {round(percentage)}% - {label}")
# Calculate percentage and build progress bar
# Use input() to get current (int), total (int), and optional label (str, default 'Loading').
# Print: [{filled}{empty}] {percent}% - {label} where bar width=10.
# Filled=#, empty=., percent=(current*100)//total.
# TODO: Complete the implementation