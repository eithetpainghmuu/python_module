numbers = [1,2,3,4,6,7,8,0]

def solution(numbers):
    list = []
    for total in range(0,10):
        if total not in numbers:
            list.append(total)
            result = sum(list)
            
    return result
print(solution(numbers))

#####################################################

n = 10

def solution(n):
    for x in range(0,11):
        x += 1
        if (n % x) == 1:         
         return x


print(solution(n))

#####################################################

num_list = [1, 2, 3, 4, 5, 6, 7, 8]
n = 2

###### 変更箇所 ##########
def solution(num_list, n):
    result = [num_list[i:i+n] for i in range(0, len(num_list), n)]
    return result

###### 変更箇所 ##########

print(solution(num_list, n))