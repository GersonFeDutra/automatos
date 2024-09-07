#include <stdio.h>

int estado = 0;

//aceitar a expressão regular (ccd u ccdcd)*(cd u cddc)*

void q0 (char c) { //estado inicial e de aceitação
    if (c == 'c') {
        estado = 1;
    } else {
        estado = -1;
    }
}

void q1 (char c) {
    if (c == 'c') {
        estado = 2;
    } else {
        estado = 6;
    }
}

void q2 (char c) {
    if (c == 'd') {
        estado = 3;
    } else {
        estado = -1;
    }
}

void q3 (char c) { // estado de aceitação
    if (c == 'c') {
        estado = 4;
    } else {
        estado = -1;
    }
}

void q4 (char c) {
    if (c == 'c') {
        estado = 2;
    } else {
        estado = 5;
    }
}

void q5 (char c) { // estado de aceitação
    if (c == 'c') {
        estado = 1;
    } else {
        estado = 7;
    }
}

void q6 (char c) { // estado de aceitação
    if (c == 'c') {
        estado = 9;
    } else {
        estado = 7;
    }
}

void q7 (char c) {
    if (c == 'c') {
        estado = 8;
    } else {
        estado = -1;
    }
}

void q8 (char c) {
    if (c == 'c') {
        estado = 9;
    } else {
        estado = -1;
    }
}

void q9 (char c) {
    if (c == 'd') {
        estado = 6;
    } else {
        estado = -1;
    }
}

int aceitacao(char str[], int n) {
    for (int i=0; i<n; i++) {
            switch(estado) {
                case 0:
                    q0(str[i]);
                    break;
                case 1:
                    q1(str[i]);
                    break;
                case 2:
                    q2(str[i]);
                    break;
                case 3:
                    q3(str[i]);
                    break;
                case 4:
                    q4(str[i]);
                    break;
                case 5:
                    q5(str[i]);
                    break;
                case 6:
                    q6(str[i]);
                    break;
                case 7:
                    q7(str[i]);
                    break;
                case 8:
                    q8(str[i]);
                    break;
                case 9:
                    q9(str[i]);
                    break;
                default:
                    return 0;
            }
    }
    if (estado == 0 || estado == 3 || estado == 5 || estado == 6 || estado == 8) { // Estado 0 = cadeia vazia
        return 1;
    } else {
        return 0;
    }
}

int main () {
    char string[51];
    int n = 0;

    fgets(string, sizeof(string), stdin);

    for (int i=0;i<=50;i++) {
        if (string[i] == '\n' || string[i] == '\0') {
            n=i;
            break;
        }
    }

    if (aceitacao(string, n)) {
        printf("sim\n");
    } else {
        printf("nao\n");
    }

    return 0;
}