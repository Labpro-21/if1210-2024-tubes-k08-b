#include <stdio.h>
#include <stdlib.h>
#include "masukdaftar.h"
#include "mesinkarakter.h"
#include "mesinkata.h"

// Fungsi untuk membandingkan 2 string
int compareStrings(const char *str1, const char *str2) {
    int i = 0;
    while (str1[i] != '\0' && str2[i] != '\0') {
        if (str1[i] != str2[i]) {
            return 0; // Tidak sama
        }
        i++;
    }
    return str1[i] == '\0' && str2[i] == '\0'; 
}

// Fungsi untuk menyalin string
void copyString(char *dest, const char *src) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0'; // Null terminator
}

// Data
User users[MAX_USERS];
int userCount = 0;
int loggedInUser = -1;

// Fungsi Register
void registerUser() {
    MesinKarakter mk;
    MesinKata usernameKata, passwordKata;

    printf(">> REGISTER\n");
    printf("Username: ");
    startMesinKarakter(&mk);
    startMesinKata(&mk, &usernameKata);

    for (int i = 0; i < userCount; i++) {
        if (compareStrings(users[i].username, usernameKata.currentWord)) {
            printf("Akun dengan username %s gagal dibuat. Silakan lakukan REGISTER ulang.\n", usernameKata.currentWord);
            return;
        }
    }

    printf("Password: ");
    startMesinKarakter(&mk);
    startMesinKata(&mk, &passwordKata);

    copyString(users[userCount].username, usernameKata.currentWord);
    copyString(users[userCount].password, passwordKata.currentWord);
    users[userCount].userID = userCount + 1;
    userCount++;

    printf("Akun dengan username %s telah berhasil dibuat. Silakan LOGIN untuk melanjutkan.\n", usernameKata.currentWord);
}

// Fungsi Login
void login() {
    MesinKarakter mk;
    MesinKata usernameKata, passwordKata;

    if (loggedInUser != -1) {
        printf("Anda masih tercatat sebagai %s. Silakan LOGOUT terlebih dahulu.\n", users[loggedInUser].username);
        return;
    }

    printf(">> LOGIN\n");
    printf("Username: ");
    startMesinKarakter(&mk);
    startMesinKata(&mk, &usernameKata);

    printf("Password: ");
    startMesinKarakter(&mk);
    startMesinKata(&mk, &passwordKata);

    for (int i = 0; i < userCount; i++) {
        if (compareStrings(users[i].username, usernameKata.currentWord) &&
            compareStrings(users[i].password, passwordKata.currentWord)) {
            loggedInUser = i;
            printf("Anda telah login ke PURRMART sebagai %s.\n", users[i].username);
            return;
        }
    }
    printf("Username atau password salah.\n");
}

// Fungsi Logout
void logout() {
    if (loggedInUser == -1) {
        printf("Tidak ada pengguna yang sedang login.\n");
        return;
    }
    printf("%s telah logout dari sistem PURRMART. Silakan REGISTER/LOGIN kembali untuk melanjutkan.\n", users[loggedInUser].username);
    loggedInUser = -1;
}

// Menu Utama
void mainMenu() {
    MesinKarakter mk;
    MesinKata choiceKata;

    do {
        printf("\n=== MENU UTAMA ===\n");
        printf("1. Register\n");
        printf("2. Login\n");
        printf("3. Logout\n");
        printf("4. Exit\n");
        printf("Pilihan: ");
        startMesinKarakter(&mk);
        startMesinKata(&mk, &choiceKata);

        if (compareStrings(choiceKata.currentWord, "1")) {
            registerUser();
        } else if (compareStrings(choiceKata.currentWord, "2")) {
            login();
        } else if (compareStrings(choiceKata.currentWord, "3")) {
            logout();
        } else if (compareStrings(choiceKata.currentWord, "4")) {
            printf("Terima kasih telah menggunakan aplikasi.\n");
            break;
        } else {
            printf("Pilihan tidak valid.\n");
        }
    } while (1);
}

int main() {
    mainMenu();
    return 0;
}