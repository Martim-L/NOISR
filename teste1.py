nums = input("(a b c):")
numslist = nums.strip().split()
a = int(numslist[0])
b = int(numslist[1])
c = int(numslist[3])
if a+b <= c or a+c <= b or b+c <= a:
    print("n é triangulo")
else:
    print("é triangulo")


