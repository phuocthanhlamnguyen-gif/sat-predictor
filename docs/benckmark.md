# The benchmark

I think it's pretty fast, while not the fastest ever (maybe because of the python code), but it's still fast 
enough to be good, but here's the benchmarks, but it varies, for my test, it's around 400ms-100ms which
is fast, but if you need very fast enterprise machine, this is not for you, still it's still good, but
here's the benchmarks:

```bash
(venv) admin_123@DESKTOP-3OKNDEQ:/mnt/c/Users/Admin/space-tracker$ time python3 code.py

--- Starting Simulation Loop ---
Ship: ISS, Step 1 -> Position (X, Y, Z): 4291.19, -4327.73, 2996.11 km
Ship: ISS, Step 2 -> Position (X, Y, Z): 4291.24, -4327.71, 2996.06 km
Ship: ISS, Step 3 -> Position (X, Y, Z): 4291.30, -4327.69, 2996.01 km
Ship: ISS, Step 4 -> Position (X, Y, Z): 4291.35, -4327.67, 2995.96 km
Ship: ISS, Step 5 -> Position (X, Y, Z): 4291.41, -4327.65, 2995.91 km
Ship: ISS, Step 6 -> Position (X, Y, Z): 4291.46, -4327.63, 2995.86 km
Ship: ISS, Step 7 -> Position (X, Y, Z): 4291.51, -4327.61, 2995.81 km
Ship: ISS, Step 8 -> Position (X, Y, Z): 4291.57, -4327.59, 2995.76 km
Ship: ISS, Step 9 -> Position (X, Y, Z): 4291.62, -4327.57, 2995.71 km
Ship: ISS, Step 10 -> Position (X, Y, Z): 4291.68, -4327.55, 2995.66 km
Ship: ISS, Step 11 -> Position (X, Y, Z): 4291.73, -4327.53, 2995.61 km
Ship: ISS, Step 12 -> Position (X, Y, Z): 4291.79, -4327.51, 2995.56 km
Ship: ISS, Step 13 -> Position (X, Y, Z): 4291.84, -4327.49, 2995.51 km
Ship: ISS, Step 14 -> Position (X, Y, Z): 4291.90, -4327.47, 2995.46 km
Ship: ISS, Step 15 -> Position (X, Y, Z): 4291.95, -4327.45, 2995.41 km
Ship: ISS, Step 16 -> Position (X, Y, Z): 4292.01, -4327.43, 2995.36 km
Ship: ISS, Step 17 -> Position (X, Y, Z): 4292.06, -4327.41, 2995.31 km
Ship: ISS, Step 18 -> Position (X, Y, Z): 4292.12, -4327.39, 2995.26 km
Ship: ISS, Step 19 -> Position (X, Y, Z): 4292.17, -4327.37, 2995.21 km
Ship: ISS, Step 20 -> Position (X, Y, Z): 4292.23, -4327.35, 2995.16 km
Ship: ISS, Step 21 -> Position (X, Y, Z): 4292.28, -4327.33, 2995.11 km
Ship: ISS, Step 22 -> Position (X, Y, Z): 4292.34, -4327.31, 2995.06 km
Ship: ISS, Step 23 -> Position (X, Y, Z): 4292.39, -4327.29, 2995.01 km
Ship: ISS, Step 24 -> Position (X, Y, Z): 4292.45, -4327.27, 2994.96 km
Ship: ISS, Step 25 -> Position (X, Y, Z): 4292.50, -4327.25, 2994.91 km
Ship: ISS, Step 26 -> Position (X, Y, Z): 4292.56, -4327.23, 2994.86 km
Ship: ISS, Step 27 -> Position (X, Y, Z): 4292.61, -4327.21, 2994.81 km
Ship: ISS, Step 28 -> Position (X, Y, Z): 4292.67, -4327.19, 2994.76 km
Ship: ISS, Step 29 -> Position (X, Y, Z): 4292.72, -4327.17, 2994.71 km
Ship: ISS, Step 30 -> Position (X, Y, Z): 4292.78, -4327.15, 2994.66 km
Ship: ISS, Step 31 -> Position (X, Y, Z): 4292.83, -4327.13, 2994.61 km
Ship: ISS, Step 32 -> Position (X, Y, Z): 4292.89, -4327.11, 2994.56 km
Ship: ISS, Step 33 -> Position (X, Y, Z): 4292.94, -4327.09, 2994.51 km
Ship: ISS, Step 34 -> Position (X, Y, Z): 4293.00, -4327.07, 2994.46 km
Ship: ISS, Step 35 -> Position (X, Y, Z): 4293.05, -4327.05, 2994.41 km
Ship: ISS, Step 36 -> Position (X, Y, Z): 4293.11, -4327.03, 2994.37 km
Ship: ISS, Step 37 -> Position (X, Y, Z): 4293.16, -4327.01, 2994.32 km
Ship: ISS, Step 38 -> Position (X, Y, Z): 4293.21, -4326.99, 2994.27 km
Ship: ISS, Step 39 -> Position (X, Y, Z): 4293.27, -4326.97, 2994.22 km
Ship: ISS, Step 40 -> Position (X, Y, Z): 4293.32, -4326.95, 2994.17 km
Ship: ISS, Step 41 -> Position (X, Y, Z): 4293.38, -4326.93, 2994.12 km
Ship: ISS, Step 42 -> Position (X, Y, Z): 4293.43, -4326.91, 2994.07 km
Ship: ISS, Step 43 -> Position (X, Y, Z): 4293.49, -4326.89, 2994.02 km
Ship: ISS, Step 44 -> Position (X, Y, Z): 4293.54, -4326.87, 2993.97 km
Ship: ISS, Step 45 -> Position (X, Y, Z): 4293.60, -4326.85, 2993.92 km
Ship: ISS, Step 46 -> Position (X, Y, Z): 4293.65, -4326.83, 2993.87 km
Ship: ISS, Step 47 -> Position (X, Y, Z): 4293.71, -4326.81, 2993.82 km
Ship: ISS, Step 48 -> Position (X, Y, Z): 4293.76, -4326.79, 2993.77 km
Ship: ISS, Step 49 -> Position (X, Y, Z): 4293.82, -4326.77, 2993.72 km
Ship: ISS, Step 50 -> Position (X, Y, Z): 4293.87, -4326.75, 2993.67 km

real    0m0.286s
user    0m1.000s
sys     0m0.281s
```

And here's the json stats:

```js
{
    "time_stamp": 0.01,
    "step_max": 50
}
```