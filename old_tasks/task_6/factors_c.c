#include <stdio.h>

void factors(int n) {
    for (int f = 1; f <= n; f++) {
        if (n % f == 0) {
            printf("%d ", f);
        }
    }
}

int main() {
    int n = 12;
    printf("Factors of %d: ", n);
    factors(n);
    printf("\n");
    return 0;
}
