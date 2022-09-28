


def freefall(x0, v0, t):
    return - 0.5 * 9.81 * t ** 2 + v0 * t + x0


x0 = 10.0 # [m]
v0 = 0.0  # [m/s]
t = 1.0
print(f"An object starting at height {x0} m with {v0} m/s after {t} seconds of freefall is at {freefall(x0,v0,t)} m")