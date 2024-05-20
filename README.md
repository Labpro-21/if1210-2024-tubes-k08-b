# IF1210 - Dasar Pemrograman 2024
> Tugas Besar - IF1210 Dasar Pemrograman 2024

# About
Pada tugas besar Dasar Pemrograman IF1210 2024 ini kami membuat program sebuah permainan bertipe turn-based berdasarkan cerita Purry the Platypus, atau dikenal juga dengan Agent P,  yang ingin menyelamatkan kota Danville dari Dr. Asep Spakbor. Karena monster-monster yang dimiliki Dr. Asep Spakbor terlalu kuat, maka Agent P membutuhkan bantuan Agent O.W.C.A. (para player) untuk mencari dan melatih para monster yang kuat di hutan terpencil yang diyakini menjadi tempat tinggal banyak monster-monster kuat. Adapun program dapat di-run melalui file main.py pada terminal.

# Contributors
- Abu Dzar Al-Ghifari (16523058)       
- Muhammad Refino Ramadhan (19623028)
- Darren Mansyl (19623168)
- Favian Rafi Laftiyanto (19623238)
- Mahesa Satria Prayata (19623278)

# Features
Sesuai dengan background cerita di atas, program dapat diurai menjadi fungsional-fungsional sebagai berikut,
1. Fungsi-fungsi penyimpanan akun dan data dan fungsi RNG,
> F00 - Random Number Generator, untuk menghasilkan bilangan acak menggunakan algoritma Linear Congruential Generator (LCG).
> F01 - Register, untuk memasukkan username dan password dari akun yang akan digunakan untuk memulai permainan. Username hanya dapat mengandung alfabet A-Z, a-z, underscore “_”, strip “-”, dan angka 0-9. Bila username belum terdaftar, maka akun diharuskan untuk memilih 1 monster starter, 0 O.W.C.A. coin, dan terdaftar sebagai agent.
> F02 - Login, untuk login ke akun yang sudah didaftar sebelumnya.
> F03 - Logout, untuk keluar dari akun yang sedang digunakan.
> F04 - Menu dan Help, untuk mengingatkan dan menuntun pengguna dan mengingatkan untuk melakukan validasi input dalam bentuk footnote.
> F05 - Monster, file yang menyimpan data monster dengan format “monster.csv”. File tersebut berisi statistik monster berupa,
Type, nama dari monster yang bersifat unik.
> ATK Power, Kekuatan serangan setiap monster. Ketika monster melakukan serangan, nilai kekuatan serangannya diambil secara acak dengan rentang ±30% dari ATK Power. Contoh untuk ATK Power = 500, rentang nilai serangannya adalah 350 - 850.
> DEF Power, Kekuatan pertahanan setiap monster dari serangan. DEF digunakan sebagai faktor pengali untuk mengurangi serangan musuh. Rentang nilainya adalah 0 - 50. Contoh untuk DEF Power = 50, maka monster dapat menurunkan serangan musuh sebesar 50%.
> HP, jumlah darah yang dimiliki para monster
> F06 - Potion, untuk membantu player dalam battle. Berikut adalah jenis-jenis potion serta efeknya,
> Healing Potion, Mengisi darah sebanyak 25% dari Base HP. Pastikan HP tidak melebihi dari maksimal HP.
> Resilience Potion, Meningkatkan DEF Power sebanyak 5% dari DEF Power.
> Strength Potion, Meningkatkan ATK Power sebanyak 5% dari ATK Power.
> ATK Power, DEF Power, dan HP mengikuti level Monster dari player, Masing-masing potion hanya dapat digunakan sekali dalam 1 battle dan efeknya hanya berlaku hingga battle itu selesai. 
> F14 - Load, untuk masuk kembali ke akun yang sudah terdaftar.
> F15 - Save, untuk menyimpan progress akun ke dalam folder yang ditentukan.
> F16 - Exit, untuk keluar dari program. Ada juga fitur untuk save terlebih dahulu sebelum melakukan exit.
2. Fungsi-fungsi yang dapat diakses oleh agent,
> F07 - Inventory, berupa file untuk menyimpan item yang dimiliki oleh player seperti potion, monster, dan monster ball. Terdapat format file yang berbeda untuk item (item_inventory.csv) dan monster (monster_inventory.csv).
> F08 - Battle, fitur utama dalam game ini untuk melawan monster-monster liar yang dipilih secara random. berikut adalah mekanismenya,
Muncul monster (musuh) secara random (RNG) database Monster; Agent memilih monster (agent) yang ingin dipertarungkan.
> Setiap putaran Agent memiliki pilihan untuk “Attack”, “Use Potion”, atau “Quit”; Monster (musuh) hanya bisa “Attack”.
> Kondisi kemenangan adalah saat nyawa monster (musuh) habis; Agent mendapatkan OC (OC yang diterima random (RNG), misal 5-30).
> Kondisi kekalahan adalah saat nyawa monster (agent) habis; Agent keluar dari pertempuran, nyawa monster yang dipertarungkan kembali penuh (tidak hilang dari inventory).
> F09 - Arena, fitur latihan agar player dapat terbiasa dengan mekanisme battle. Mekanismenya sama seperti fitur battle. Player akan mendapatkan hadiah setara dengan jumlah stage yang berhasil dilewati. (OC = O.W.C.A. Coin)
Stage 1: 50 OC
Stage 2: 100 OC
Stage 3: 150 OC
Stage 4: 200 OC
stage 5: 250 OC
> F10 - Shop & Currency, tempat player membeli monster dan potion tambahan. Terdapat format file khusus item (item_shop.csv) dan monster (monster_shop.csv).
> F11 - Laboratory, fitur untuk meng-upgrade level monster yang dimiliki oleh player. Untuk melakukan upgrade diperlukan OC. Berikut adalah harganya,
Level 1 - 2: 100,
Level 2 - 3: 200,
Level 3 - 4: 400,
Level 4 - 5: 700
Fungsi-fungsi yang dapat diakses oleh admin,
> F12 - Shop Management, untuk mengubah dan menghapus item dalam shop
> F13 - Monster Management, untuk menampilkan seluruh monster dalam program dan menambah monster ke program.

# How to Run 
Program dapat di-run dengan cara membuka terminal pada file "main.py" kemudian mengetik "python main.py data1" pada terminal. *Note: data1 bisa diubah menjadi data yang lain yang tersedia pada folder data.
Setelah memulai program, user dapat menggunakan fitur "Help" untuk melihat fitur apa saja yang dapat dilakukan.
Sebelum login, terdapat 4 fitur yang dapat dilakukan: login, register, save, dan exit.
Setelah register dan/atau login, terdapat 7 fitur yang dapat dilakukan, yaitu: battle, arena, shop, inventory, laboratory, jackpot, dan logout.
Ada pula fitur khusus yang hanya bisa diakses oleh user dengan role "Admin" (tidak ada cara untuk register sebagai "Admin", yaitu: monster management, shop management, dan logout.

Selamat bermain! ^-^
