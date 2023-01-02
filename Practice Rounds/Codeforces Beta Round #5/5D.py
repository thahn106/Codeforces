from math import sqrt
a,v = map(int, input().split())
l,d,w = map(int, input().split())

# a = acceleration/decceleration,
# l = length of road
# w = speed limit at point
# d = location of speed limit

mat = v/a # max_acceleration_time
mad = 0.5*a*mat*mat # max_acceleration_distance

lat = w/a # limit_acceleration_time
lad = 0.5*a*lat*lat # limit_acceleration_distance

dt = (v-w)/a #deccelerationtolimit_time
dd = -0.5*a*dt*dt+v*dt #deccelerationtolimit_distance

# Case 1: v <w, can fully accerlate or car does not reach speed limit by sign
if v<=w or lad > d:
    # Case 1-1: car does not reach top speed
    if mad > l:
        ans = sqrt(2*l/a)
    # Case 1-2: car reaches top speed
    else:
        msd = l-mad #max_speed_distance
        ans = mat+msd/v
# Case 2 car can reach top speed, cruise and decceerlate before sign: 
elif mad + dd <= d:
    cd = d-dd-mad
    ans = mat+(cd/v)+dt
    rd = l-d
    # Case 2-1
    if rd<dd:
        ans += (-w+sqrt(w*w+2*rd*a))/a
    else:
        ans += dt + (rd-dd)/v
else:
    x = sqrt(a*d+w*w/2)
    ans = (2*x-w)/a
    rd = l-d
    # Case 3-1
    if rd<dd:
        ans += (-w+sqrt(w*w+2*rd*a))/a
    else:
        ans += dt + (rd-dd)/v

print(f"{ans:.10f}")
