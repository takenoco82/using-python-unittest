def fizzbuzz_list(n: int) -> list:
    return list(fizzbuzz_gen(n))


def fizzbuzz_gen(n: int):
    if type(n) != int:
        message = "`{}` is invalid value. must be type `int`.".format(n)
        raise TypeError(message)
    if n < 1:
        message = "`{}` is invalid value. must be larger than `0`.".format(n)
        raise ValueError(message)

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
