# Get inputs from user
level = input()
message = input()
line_num = int(input())
print(f"[{level}] Line {line_num}: {message}")
# Print the formatted log entry
# Use input() to get level (str), message (str), and line_num (int).
# Print: [{level}] Line {line_num}: {message}
# Convert line_num to string via f-string or str().
# TODO: Implement the solution based on the instructions above