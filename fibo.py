def recursive_nth_fibo(n):
    if n < 0:
        return None
    if n < 2:
        return n
    return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)


def main():
    n = int(input("Zadejete požadovaný počet členů Fibo. poslopnosti:"))
    seq = [recursive_nth_fibo(i) for i in range(n)]
    print(seq)
    pass


if __name__ == "__main__":
    main()
