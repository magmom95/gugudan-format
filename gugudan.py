n = int(input("숫자를 입력하세요 "))

for a in range(2, n+1):
    for b in range(1, 10):
        print('{0} x {1} = {2}'.format(a, b, a*b))
