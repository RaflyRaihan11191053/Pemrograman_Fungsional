#No. 1 sum_square list int 1, 2, 3

list_int = (1,2,3)

def sum_quares(t):
  return sum([i*i for i in list_int])

print(sum_quares(list_int))

#No. 2 triangular number of 5

def triangular_number(n):
  return sum(range(1, n+1))
print(triangular_number(5))

#No. 3 perpangkatan tanpa menggunakan **

def square_number(number, square):
  if square > 1:
    return number * square_number(number, square - 1)
  return number

print(square_number(3, 2))

#No. 4 palindrome word checker

def isPalindrome(str):
    x=list(str)
    y=[]
    y.extend(x)
    x.reverse()
    if(x==y):
        return True
    return False
 
str = "rotator"
chk = isPalindrome(str)
 
if chk:
    print("True")
 
else:
    print("False")

