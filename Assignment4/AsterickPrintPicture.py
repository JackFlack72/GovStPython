rows = 7

# Outer Loop Handles Each Row
for i in range(rows, 0, -1):
    # Inner loop prints stars across the column
    for j in range(i):
        print("*", end=" ")
    # Move To The Next Line After Completing A Row
    print()