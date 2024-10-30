def square_series(limit):
    return [i ** 2 for i in range(1, limit + 1)]

def cube_series(limit):
    return [i ** 3 for i in range(1, limit + 1)]

print("Square Series:", square_series(10))
print("Cube Series:", cube_series(10))
