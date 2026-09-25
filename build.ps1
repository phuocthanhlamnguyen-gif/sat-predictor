Write-Host "Building code!" -ForegroundColor Green
gcc -shared -o mathlib.dll main.c -lm
Write-Host "Done building code, now start running!" -ForegroundColor Green
./code.py