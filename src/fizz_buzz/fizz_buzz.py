# def fizz_buzz(n):
#     result = []
#     i = 1
#     while i <= n:
#         answer = 'Fizz' if i % 3 == 0 else ''
#         answer += 'Buzz' if i % 5 == 0 else ''
#         result.append(answer if answer else str(i))
#         i += 1
#     return result


def fizz_buzz(n):
    result = []
    for i in range(1, n+1):
        answer = 'Fizz' if i % 3 == 0 else ''
        answer += 'Buzz' if i % 5 == 0 else ''
        result.append(answer if answer else str(i))
    return result
