"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million,
find the sum of the even-valued terms.
"""


def fibonacci_seq():
    yield 1
    yield 2
    nums = [1, 2]
    while True:
        next_fib_num = sum(nums)
        yield next_fib_num
        nums.append(next_fib_num)
        nums.pop(0)


def even_fibonacci_number(n):
    result = 0
    for fib_num in fibonacci_seq():
        if fib_num > n:
            break
        result += fib_num if fib_num % 2 == 0 else 0
    return result


if __name__ == "__main__":
    print(even_fibonacci_number(4000000))
