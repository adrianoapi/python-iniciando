def call_numbers():
    for number in range(0, 10):
        print(number)

def call_numbers_with_limit(limit):
    list = range(0, 10)
    for number in list[0:limit]:
        print(number)


def calculator(x=10, y=2):
    return(x-y)
    
result = calculator(y=5, x=10)
print("Resultado ",result)