# Drakoo – cara membuat APK

## Cara A: tanpa laptop (lewat GitHub, gratis)
1. Buat akun di github.com, lalu buat repository baru (nama bebas).
2. Upload semua isi folder ini (termasuk folder .github dan www).
3. Buka tab Actions, pilih "Build APK", tekan Run workflow.
4. Tunggu sekitar 5-8 menit. Buka run yang selesai, unduh "drakoo-apk" di bagian Artifacts.
5. Ekstrak zip, pasang app-debug.apk di HP (izinkan "pasang dari sumber tidak dikenal").

## Cara B: di laptop
Butuh Node.js 20, Java 17, dan Android Studio.
    npm install
    npx cap add android
    npx cap sync android
    npx cap open android
Lalu di Android Studio: Build > Build APK(s).

## Mengubah tampilan
Edit www/index.html, lalu jalankan ulang build.

## Catatan
APK ini berjenis debug, cukup untuk dicoba. Untuk rilis ke Play Store perlu APK/AAB yang ditandatangani (signed).
