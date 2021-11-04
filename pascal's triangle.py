def choose(n, k): # note no dependencies on any of the prior code
     if k in (0, n):
         return 1
     return choose(n-1, k-1) + choose(n-1, k)

for row in range(40):
    for k in range(row + 1):
        # flush is a Python 3 only argument, you can leave it out,
        # but it lets us see each element print as it finishes calculating
        print(choose(row, k), end=' ') 
    print()