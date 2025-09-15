def plus(num):
    result = num + 5
    return result

print(plus(5)) # => 10
print(plus()) # TypeError: plus() missing 1 required positional argument: 'num' ##값 한개는 있어야 하는데 왜 안넣었니
