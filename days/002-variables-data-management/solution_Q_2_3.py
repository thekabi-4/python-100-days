# Get inputs from user
value = float(input())
min_val = float(input())
max_val = float(input())
if max_val==min_val:
    print("50.0")
else:
    print(round(((value-min_val)/(max_val-min_val))*100,1))
# Normalize sensor reading
# Use input() to get value, min_val, max_val (all float).
# Print ((value - min_val) / (max_val - min_val)) * 100, rounded to 1 decimal.
# If max_val == min_val, print 50.0.
# TODO: Implement the solution based on the instructions above