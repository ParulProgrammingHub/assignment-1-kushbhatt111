def simple_interest(p,t,i):
    a=p*t*i*0.01
    return a
p=input("Enter the principal amount:")
t=input("Enter the time per year:")
i=input("Enter the interest of loan percentage:")
print simple_interest(p,t,i)
