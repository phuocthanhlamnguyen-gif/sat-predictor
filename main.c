#include <math.h>
#include <stdio.h>

#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#elif defined(__linux__)
    #define EXPORT __attribute__((visibility("default")))
#else
    #define EXPORT
#endif

EXPORT void pre_orb(double pos[3], double vel[3], double mu, double dt) {
    double r = sqrt(pos[0]*pos[0] + pos[1]*pos[1] + pos[2]*pos[2]);
    double r3 = r * r * r;

    for (int i = 0; i < 3; i++) {
        double acc = -(mu / r3) * pos[i];
        vel[i] += acc * dt;
        pos[i] += vel[i] * dt; 
    }
}

EXPORT void print_output(double pos[3], int step) {
    printf("Ship: ISS, Step %d -> Position (X, Y, Z): %.2f, %.2f, %.2f km\n", step, pos[0], pos[1], pos[2]);
}