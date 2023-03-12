def test_returu():
    return 1, 2

result = test_returu()
print(result, type(result))
x, y = result
print(x, y, type(x), type(y))
