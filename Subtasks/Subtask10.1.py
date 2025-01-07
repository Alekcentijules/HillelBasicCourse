def counter(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Count of function: {count}")
        func(*args, **kwargs)
        return count

    # wrapper.count = lambda: count
    return wrapper

@counter
def example_function(x, pow=2, **kwargs):
    print("Inside the function")
    print(f"Additional kwargs: {kwargs}")
    return x ** pow


print(f"Result: {example_function(1)}")
print(f"Result: {example_function(6)}")
print(f"Result: {example_function(7, key="V")}")








