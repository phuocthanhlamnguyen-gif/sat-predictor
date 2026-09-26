import ctypes
import sys
import numpy as np
from skyfield.api import Loader, load

# Check for OS compatibility and load binary
if sys.platform.startswith('win'):
    bin_path = './binary/mathlib.dll'
elif sys.platform.startswith('linux'):
    bin_path = './binary/mathlib.so'
else:
    print('Unsupported operating system!')
    sys.exit(1)

lib = ctypes.CDLL(bin_path)

# Define C function signatures for ctypes safety
lib.pre_orb.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_double,
    ctypes.c_double,
]

lib.print_output.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_int,
]

# Initialize Skyfield timescale and satellite data
load_file = Loader('~/skyfield-data')
ts = load_file.timescale()

stations_url = (
    'https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=tle'
)
satellites = load.tle_file(stations_url)
iss = satellites[0]

t = ts.now()
geocentric = iss.at(t)

position = np.array(geocentric.position.km, dtype=np.float64)
velocity = np.array(geocentric.velocity.km_per_s, dtype=np.float64)
mu = 398600.44

# Get time-step dynamically from user input
try:
    dt = float(input('Enter time step dt (seconds, e.g., 10): ') or 10.0)
except ValueError:
    dt = 10.0
    print('Invalid input, defaulting dt to 10.0 seconds.')

print('\n--- Starting Simulation Loop ---')
for step in range(10):
    lib.pre_orb(position, velocity, mu, dt)
    lib.print_output(position, step + 1)

print('\nSimulation complete. Press Enter to exit.')
input()