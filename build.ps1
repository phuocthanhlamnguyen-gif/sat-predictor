Write-Host "Building code..."
gcc -shared -o binary/mathlib.dll main.c -lm 
Write-Host "Done building, now need to get all the imports..."
pip install numpy skyfield
Write-Host "Done, now just need to run code..."
./code.py