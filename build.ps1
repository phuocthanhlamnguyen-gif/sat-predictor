Write-Host "Building code..."
gcc -shared -o mathlib.dll main.c -lm 
Write-Host "Done building, now running..."
./code.py