import orbitmagic as om


def Faro_Out(n: int):
    if n % 2:
        return None
    return list(i // 2 + (i % 2) * n // 2 for i in range(2, n + 2))


def Faro_In(n: int):
    if n % 2:
        return None
    return list(i // 2 + (1 - i % 2) * n // 2 for i in range(2, n + 2))


def Monge_In(n: int):
    if n % 2:
        return list(range(n, -1, -2)) + list(range(2, n + 1, 2))
    return list(range(n - 1, 0, -2)) + list(range(2, n + 1, 2))


def Monge_Out(n: int):
    if n % 2:
        return list(range(n - 1, 0, -2)) + list(range(1, n + 1, 2))
    return list(range(n, 0, -2)) + list(range(1, n + 1, 2))


print(om.all_cases((Faro_In(4))))

print(om.all_cases((Faro_In(6))))

