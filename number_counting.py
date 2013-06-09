def no_sevens(n):
    total = 0
    for i in range(1, n+1):
        if "7" not in str(i):
            total += 1
    return total
