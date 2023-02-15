def calculate(s: str, n: int, i: int = 1):
    if i == len(s) - 1:
        if eval(s) == n:
            print(s, "=", eval(s))
        return
    for op in ['', '+', '-']:
        new_s = s[:i] + op + s[i:]
        calculate(new_s, n, i + 1 if op == '' else i + 2)

s = '9876543210'
n = 200

calculate(s, n)
