numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    num1 = numbers[0]
    for i in numbers:
        if i > num1:
            num1 = i

    num2 = numbers[0]
    for i in numbers:
        if i < num2:
            num2 = i

    list1 = []
    for total in range(0,10):
        if total not in numbers:
            list1.append(total)
            result = sum(list1)
            
    return result
print(solution(numbers))

