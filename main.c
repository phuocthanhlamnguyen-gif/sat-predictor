#include <math.h>
#include <stdio.h>

#ifdef _WIN32
    #define EXPORT __declspec(dllexport)
#elif defined(__linux__)
    #define EXPORT __attribute__((visibility("default")))
#else
    #define EXPORT
#endif

EXPORT void pre_orb(double pos[3], double vel[3], double mu, double dt, double Re, double J2) {
    // Some contants
    double x = pos[0], y = pos[1], z = pos[2];
    double r2 = x*x + y*y + z*z;
    double r = sqrt(r2);
    double r3 = r2 * r;
    double r5 = r3 * r2;
    // 1. Central gravity acceleration
    double ax = -mu * x / r3;
    double ay = -mu * y / r3;
    double az = -mu * z / r3;
    // 2. J2 Oblateness perturbation
    double j2_factor = 1.5 * J2 * mu * (Re * Re) / r5;
    double z_ratio2 = 5.0 * (z * z) / r2;
    ax += j2_factor * x * (z_ratio2 - 1.0);
    ay += j2_factor * y * (z_ratio2 - 1.0);
    az += j2_factor * z * (z_ratio2 - 3.0);
    // Simple forward Euler integration step
    pos[0] += vel[0] * dt;
    pos[1] += vel[1] * dt;
    pos[2] += vel[2] * dt;
    vel[0] += ax * dt;
    vel[1] += ay * dt;
    vel[2] += az * dt;
}

EXPORT void print_output(double pos[3], int step) {
    char buff[128];
    FILE *file = fopen("report.sp", "a");
    if (file == NULL) {
        perror("Failed to open file");
        return; 
    }
    printf("Step %d -> Position (X, Y, Z): %.2f, %.2f, %.2f km\n", step, pos[0], pos[1], pos[2]);
    int len = snprintf(buff, sizeof(buff), "Step %d -> Position (X, Y, Z): %.2f, %.2f, %.2f km\n", step, pos[0], pos[1], pos[2]);
    if (len > 0) {
        fputs(buff, file); 
    }
    fclose(file);
}