from math import log10, ceil, sqrt
phi = (1+sqrt(5))/2
t = int(input())
for a0 in range(t):
    d = int(input())
    term = ceil((log10(5)/2+d-1)/ log10(phi))
    print(term)