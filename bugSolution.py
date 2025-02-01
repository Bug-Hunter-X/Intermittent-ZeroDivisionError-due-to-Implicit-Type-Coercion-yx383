def function_with_uncommon_error_fixed(a, b):
    if a == 0 and b == 0:
        return 0  # Handle the case where both are zero explicitly
    elif a == 0:
        return b
    elif b == 0:
        return a
    else:
        return a / b

result = function_with_uncommon_error_fixed(0, 0)
print(result)  # This will always return 0