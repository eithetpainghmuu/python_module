numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    list1 = []
    for total in range(0,10):
        if total not in numbers:
            list1.append(total)
            result = sum(list1)
            
    return result
print(solution(numbers))

