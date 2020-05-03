
def factorial(n):
    answer=1
    while n>0:
        answer *= n
        n -= 1
    return answer

def fact(n):
    if n==0:
        return 1
    else:
        return n *fact(n-1)

print (factorial(7))
print (fact(7))
