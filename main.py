#import my_module

#print(my_module.add(1,4))
#print(my_module.subtract(5,2))
#print(my_module.test(5,5))

from my_module import add,test

print(add(1,5))
print(test(5,5))

