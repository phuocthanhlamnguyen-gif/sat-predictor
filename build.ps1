Write-Host "Building code..."
gcc -shared -o binary/mathlib.dll main.c -lm 
Write-Host "Done building, now running..."
./code.py