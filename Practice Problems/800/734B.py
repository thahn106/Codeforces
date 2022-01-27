k2,k3,k5,k6 = map(int,input().split())
s = min(k2,k5,k6)
print(s*256+min(k2-s,k3)*32)
