def recursive_nth_fibo(n):
    if n < 0:
        return None
    if n < 2:
        return n
    return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    print(recursive_nth_fibo(3))
    pass


if __name__ == "__main__":
    main()
