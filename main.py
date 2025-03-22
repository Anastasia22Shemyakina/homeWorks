def power_numbers(*numbers):
    my_list=[]     
    for item in numbers:  
        if type(item) == int:
            my_list.append(item ** 2) 
      
    return my_list  


ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_numbers (numbers,filter_type):
    if filter_type == EVEN:
       return list(filter(lambda x: x % 2 == 0, numbers))
                
    if filter_type == ODD :
        return list(filter(lambda x: x % 2 != 0, numbers))
                
    if filter_type == PRIME:
        return list(filter(lambda x: is_prime(x), numbers))