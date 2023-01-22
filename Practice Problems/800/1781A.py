for t in range(int(input())):
    w, d, h = map(int, input().split())
    a, b, f, g = map(int, input().split())
    ans = min(b+g+abs(a-f), abs(a-f)+2*d-g-b, abs(b-g)+a+f, abs(b-g)+2*w-a-f)
    print(ans+h)
