def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    def breakfirst(a, b):
        return a
    return pair(breakfirst)


    


def cdr(pair):
    def breaksecound(a,b):
        return b
    return pair(breaksecound)
    

# create a pair
pair = cons(3, 4)

# get the first element of the pair
first_element = car(pair)  # returns 3

# get the second element of the pair
second_element = cdr(pair)  # returns 4

# print the values
print(first_element)    # prints 3
print(second_element)   # prints 4
