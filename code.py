from skyfield.api import Loader, load
import math

mu = 398600.44  # Gravitational parameter for Earth in km^3/s^2

load_file = Loader('~/skyfield-data')
ts = load_file.timescale()

stations_url = (
    'https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle'
)
satellites = load.tle_file(stations_url)
iss = satellites[0]
t = ts.now()
geocentric = iss.at(t)

position = list(geocentric.position.km)
velocity = list(geocentric.velocity.km_per_s)

# Time step in seconds
dt = 5

for step in range(5):  
    # 1. Calculate total distance magnitude (r) from Earth's center
    r = math.sqrt(position[0]**2 + position[1]**2 + position[2]**2)

    # 2. Calculate 3D acceleration vector components (a = -mu / r^3 * position)
    acc = [0, 0, 0]
    for i in range(3):
        acc[i] = -(mu / r**3) * position[i]
        velocity[i] += acc[i] * dt
        position[i] += velocity[i] * dt

    print(f"Step {step+1} -> New Position (X, Y, Z): {position[0]:.2f}, {position[1]:.2f}, {position[2]:.2f} km")