# Type hints
def add_two_numbers(a: int, b: int) -> int:
    return a + b

# Note coloured bar in right hand side of screen indicating type problem
# May miss this if not cleaning up the PEP 8 warnings
print(add_two_numbers(1.1, 2.3))
