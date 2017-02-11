def intr(p,r,t):
  n=r/t
  d=t*t
  i=(p*((1+n)**(d)))-p
  print n
  print d
  print i
a=float(raw_input("Principle="))
b=float(raw_input("Rate="))
c=int(raw_input("Time(in year)="))
intr(a,b,c)
