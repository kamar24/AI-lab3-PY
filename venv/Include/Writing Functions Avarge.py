def average(*n):
    if n:
        return sum(n) / n.__len__();
    else:
        return None


print(average())
print(average(5))
print(average(6, 8, 9, 11))