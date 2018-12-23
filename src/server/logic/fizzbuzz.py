def fizzbuzz_gen(n: int):
    if type(n) != int:
        raise TypeError
    if n < 1:
        raise ValueError

    for i in range(1, n + 1):
        yield fizzbuzz(i)


def fizzbuzz(n: int) -> str:
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
