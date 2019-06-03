def multiply_down(n):
    number = []
    for i in str(n):
        number.append(int(i))

    counter = 0
    while(len(number) > 1):
        counter += 1
        placehold = 1
        for i in number:
            placehold *= i
        number = []
        for i in str(placehold):
            number.append(int(i))
    return counter

def number_to_base(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def add_six(n):
    return n + 6

def array_to_int(arr):
    s = [str(i) for i in arr]
    res = int("".join(s))
    return res

base_4_iterator = 4 ** 229
max_num = 0
max_per = 0
while(True):
    base_4_iterator += 1
    num_tail = list(map(add_six, number_to_base(base_4_iterator, 4)))
    for i in [0,2,3,4]:
        number = array_to_int([i] + num_tail)
        per = multiply_down(number)
        if per > max_per:
            max_per = per
            max_num = number
            print('New max: {a}\nPersistence: {b}\n\n'.format(a=number, b=per))









#Just one 2
#Just one 3
#No 4,2
#No 4,3 - can be 2,6
#no 4,4 - can be 2, 8
#No