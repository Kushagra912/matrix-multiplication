from operator import mul
X=[[1,2,3], [4,5,6], [7,8,9]]
Y=[[10,11,12], [13,14,15], [16,17,18]]
R = [[sum(mul(*es) for es in zip(r, c)) for c in zip(*Y)] for r in X]
print("======Multiplied matrix====== \n")
for r in R: print(r)
