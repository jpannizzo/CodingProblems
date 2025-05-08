def approaching_fibonacci(arr):
    # manually compute the sum
    total = 0
    for n in arr:
        total += n

    # find the smallest Fibonacci number ≥ total
    a, b = 0, 1
    while a < total:
        a, b = b, a + b

    # result to return
    result = a - total
    # formatted result
    formatted_result = f"Input: {arr}\nTotal Input: {total}\nOutput: {result}\nTotal Output: {total+result}\n"
    return formatted_result

print(approaching_fibonacci([1, 2, 3]))    # 6 → next Fib is 8 → 2
print(approaching_fibonacci([1, 1, 2]))    # 4 → next Fib is 5 → 1
print(approaching_fibonacci([2, 3, 5]))    # 10 → next Fib is 13 → 3
print(approaching_fibonacci([1, 1, 1, 2])) # 5 → already Fib → 0