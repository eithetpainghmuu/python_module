numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    list = []
    for total in range(0,10):
        if total not in numbers:
            list.append(total)
            result = sum(list)
            
    return result
print(solution(numbers))

