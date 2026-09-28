import ctypes
import json
import sys
import numpy as np

# Load C Binary (Windows / Linux support)
if sys.platform.startswith('win'):
    bin_path = './binary/mathlib.dll'
elif sys.platform.startswith('linux'):
    bin_path = './binary/mathlib.so'
else:
    print('Unsupported operating system!')
    sys.exit(1)

lib = ctypes.CDLL(bin_path)

lib.pre_orb.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
]

lib.print_output.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.float64, ndim=1, flags='C_CONTIGUOUS'),
    ctypes.c_int,
    ctypes.c_char_p,
]

with open('config/config.json', 'r') as f:
    config = json.load(f)

position = np.array(config['position'], dtype=np.float64)  
velocity = np.array(config['velocity'], dtype=np.float64)  
mu = config['mu']
dt = config['time_stamp']
max_step = config['step_max']
RE = config['Re']
J2 = config['J2']
filename = config['file']

print('\n--- Simulation: v0.0.1-alpha ---')
open(filename, "w").close()
for step in range(max_step):
    lib.pre_orb(position, velocity, mu, dt, RE, J2)
    lib.print_output(position, step + 1, b"filename")