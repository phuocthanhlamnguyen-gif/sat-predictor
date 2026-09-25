import ctypes
import numpy as np
from skyfield.api import Loader, load
import sys

# Check for the OS compatability
if sys.platform.startswith('win'):
    bin = "./binary/mathlib.dll"
elif sys.platform.startswith('linux'):
    bin = './binary/mathlib.so'
else:
    print("Unsupported")
    exit(1)

# Load the binary
lib = ctypes.CDLL(bin)

# Get all the C stuff to support python basic stuff
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

# To load to start the skyfield
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
dt = 10

for step in range(10):
    lib.pre_orb(position, velocity, mu, dt)
    lib.print_output(position, step + 1)

input()