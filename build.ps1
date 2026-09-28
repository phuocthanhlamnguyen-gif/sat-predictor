Write-Host "Building code..."
New-Item report.sat -type file
mkdir -p binary
gcc -shared -o binary/mathlib.dll main.c -lm 
Write-Host "Done building, now need to get all the imports..."
pip install numpy skyfield
Write-Host "Done, now just need to run code..."
./main.py