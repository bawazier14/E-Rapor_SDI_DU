# Project Context — E-Rapor SD

## 1. Project Name
**E-Rapor SD**  
Sistem informasi berbasis web untuk pengelolaan data akademik dan pembuatan rapor siswa Sekolah Dasar (SD).

---

## 2. Project Goal
Membangun sistem **E-Rapor SD berbasis web** yang dapat membantu sekolah dalam:

- mengelola data siswa, guru, kelas, dan mata pelajaran
- mengatur struktur akademik per tahun ajaran dan semester
- menginput nilai siswa
- mengelola absensi, ekstrakurikuler, dan catatan wali kelas
- menghasilkan rapor siswa secara otomatis
- mencetak rapor ke PDF
- mempermudah administrasi akademik sekolah secara digital

Sistem ini dirancang agar:
- mudah digunakan oleh admin dan guru
- maintainable untuk pengembangan jangka panjang
- mudah dijalankan secara lokal maupun production menggunakan Docker
- mudah dikembangkan secara bertahap dengan bantuan AI assistant

---

## 3. Scope of System

### Included in Scope
Sistem mencakup modul berikut:

1. Authentication & Authorization
2. User Management
3. Profil Sekolah
4. Data Guru
5. Data Siswa
6. Data Kelas
7. Data Mata Pelajaran
8. Tahun Ajaran & Semester
9. Struktur Akademik (rombel, wali kelas, pengampu)
10. Input Nilai
11. Rekap Nilai
12. Absensi
13. Ekstrakurikuler
14. Catatan Wali Kelas
15. Generate Rapor
16. Export PDF
17. Import/Export Excel
18. Dashboard Ringan
19. Settings dasar sistem

### Out of Scope (for MVP)
Fitur berikut **tidak menjadi prioritas awal**:

- aplikasi mobile native
- sistem pembayaran
- integrasi WhatsApp
- integrasi Dapodik resmi
- multi-sekolah (multi-tenant)
- API publik
- machine learning / analytics kompleks
- portal orang tua versi penuh
- tanda tangan digital bersertifikat
- sinkronisasi real-time lintas instansi

---

## 4. Target Users

### 1. Admin
Bertanggung jawab mengelola sistem secara penuh:
- akun user
- data master
- konfigurasi akademik
- import/export data
- monitoring sistem

### 2. Guru Kelas / Wali Kelas
Bertanggung jawab pada:
- data siswa di kelasnya
- absensi
- catatan wali kelas
- finalisasi rapor kelas

### 3. Guru Mata Pelajaran
Bertanggung jawab pada:
- input nilai siswa
- rekap nilai per kelas/mapel
- deskripsi pembelajaran (jika digunakan)

### 4. Kepala Sekolah (opsional)
Bertanggung jawab pada:
- monitoring hasil rapor
- approval / validasi akhir (opsional)

### 5. Siswa / Orang Tua (opsional fase akhir)
Dapat:
- melihat rapor
- mengunduh PDF rapor
- melihat perkembangan akademik sederhana

---

## 5. School Context / Business Assumption
Sistem ini dirancang untuk konteks **Sekolah Dasar (SD)** dengan karakteristik:

- struktur kelas per tingkat (contoh: 1A, 1B, 2A, dst)
- sistem semester (ganjil / genap)
- rapor berbasis nilai akademik dan non-akademik
- adanya wali kelas
- data siswa dikelompokkan per kelas dan tahun ajaran
- nilai dapat dihitung berdasarkan komponen yang disesuaikan sekolah
- rapor dicetak per siswa per semester

### Assumptions
- sekolah menggunakan sistem penilaian yang masih bisa disederhanakan secara digital
- sekolah memiliki admin/operator untuk mengelola data master
- guru dapat menginput data melalui browser
- sistem digunakan terutama melalui desktop/laptop
- internet tidak harus selalu publik, sistem bisa berjalan lokal/intranet

---

## 6. Product Vision
Membangun **sistem E-Rapor SD yang praktis, stabil, dan realistis dipakai sekolah**, bukan sekadar demo CRUD.

Fokus utama:
- **fungsi**
- **akurasi data**
- **kemudahan operasional**
- **konsistensi arsitektur**
- **siap dikembangkan**

---

## 7. Engineering Philosophy
Project ini dibangun dengan prinsip:

- **Backend-first**
- **Modular Monolith**
- **Maintainable over trendy**
- **Business logic must be explicit**
- **AI-friendly codebase**
- **Production-minded from the start**
- **Incremental development (phase by phase)**

### Core Engineering Principles
- jangan menulis business logic berat di route/controller
- pisahkan query, service, dan template
- schema database harus konsisten sejak awal
- semua perubahan database harus lewat migration
- setiap modul harus berdiri jelas secara domain
- naming harus konsisten dan mudah dibaca manusia maupun AI

---

## 8. Final Tech Stack

### Backend
- Python 3.12
- Flask
- Flask Blueprints
- SQLAlchemy
- Flask-Migrate
- Flask-Login
- Flask-WTF
- Jinja2

### Database
- MySQL 8 / MariaDB 11

### Frontend (SSR)
- HTML
- Bootstrap 5
- JavaScript
- DataTables
- Select2
- SweetAlert2
- Chart.js (opsional)

### Reporting / File
- WeasyPrint (PDF)
- openpyxl (Excel)
- Pillow (image handling ringan)

### Infra / Deployment
- Docker
- Docker Compose
- Gunicorn
- Nginx
- Ubuntu VPS

### Dev Tools
- pytest
- black
- isort
- flake8
- pre-commit (opsional)

---

## 9. Project Architecture

### Architecture Style
**Modular Monolith**

Sistem dibangun sebagai satu aplikasi utama Flask, namun dipisah menjadi beberapa modul domain.

### Why this architecture?
Karena sistem E-Rapor:
- banyak CRUD
- banyak relasi database
- banyak aturan bisnis internal
- lebih cocok dijaga dalam satu codebase yang modular

### Avoid
Jangan ubah sistem menjadi:
- microservices
- SPA/API-first berlebihan
- event-driven complexity
- frontend-heavy architecture

Karena itu hanya menambah kompleksitas tanpa manfaat nyata untuk scope project ini.

---

## 10. Folder Strategy

### Root Structure
Project dibagi ke dalam folder utama berikut:

- `backend/` → source code aplikasi
- `frontend/` → asset desain, mockup, referensi UI
- `infra/` → Docker, Nginx, MySQL config
- `docs/` → dokumentasi arsitektur, modul, database, AI workflow

### Important Rule
**Template produksi aplikasi tetap berada di backend**, bukan di folder frontend.

---

## 11. Backend Structure Philosophy

### Layered Responsibility
Backend mengikuti pola berikut:

#### `models/`
Merepresentasikan tabel dan relasi database.

#### `modules/`
Setiap fitur/domain punya modul sendiri, misalnya:
- auth
- siswa
- guru
- nilai
- rapor

#### `services.py`
Tempat business logic utama.

#### `repositories/`
Tempat query database yang kompleks atau reusable.

#### `forms.py`
Untuk validasi form berbasis Flask-WTF.

#### `schemas.py`
Untuk struktur data internal, import/export, dan validasi payload.

### Golden Rule
> **Routes only orchestrate. Services execute business logic. Models represent data.**

---

## 12. Core Modules
Berikut modul inti sistem:

1. `auth`
2. `dashboard`
3. `users`
4. `sekolah`
5. `guru`
6. `siswa`
7. `kelas`
8. `mapel`
9. `akademik`
10. `nilai`
11. `absensi`
12. `ekskul`
13. `rapor`
14. `import_export`
15. `settings`

---

## 13. Module Responsibilities

### `auth`
Menangani:
- login
- logout
- session auth
- proteksi route dasar

### `users`
Menangani:
- manajemen akun user
- reset password
- aktivasi/nonaktif akun
- relasi user dengan role

### `sekolah`
Menangani:
- identitas sekolah
- kepala sekolah
- logo sekolah
- metadata rapor

### `guru`
Menangani:
- CRUD guru
- data guru aktif/nonaktif

### `siswa`
Menangani:
- CRUD siswa
- status siswa
- identitas siswa

### `kelas`
Menangani:
- kelas per tingkat
- pembagian kelas

### `mapel`
Menangani:
- data mata pelajaran
- pengelompokan mapel

### `akademik`
Menangani:
- tahun ajaran
- semester
- rombel
- wali kelas
- pengampu / mengajar

### `nilai`
Menangani:
- input nilai
- perhitungan nilai akhir
- predikat
- deskripsi nilai
- lock/finalisasi nilai

### `absensi`
Menangani:
- sakit
- izin
- alfa
- rekap kehadiran

### `ekskul`
Menangani:
- data ekstrakurikuler
- nilai/predikat ekskul
- deskripsi kegiatan

### `rapor`
Menangani:
- preview rapor
- generate rapor
- PDF rapor
- finalisasi rapor

### `import_export`
Menangani:
- import Excel
- export data
- template upload

### `settings`
Menangani:
- pengaturan sistem dasar
- parameter akademik ringan

---

## 14. Database Design Principles

### Database Type
**Relational database** (MySQL / MariaDB)

### Why?
Karena domain E-Rapor memiliki relasi kuat antara:
- siswa
- kelas
- guru
- mapel
- tahun ajaran
- nilai
- rapor

### Design Rules
- semua tabel harus punya primary key yang jelas
- foreign key harus eksplisit
- gunakan migration untuk setiap perubahan schema
- hindari duplicate source of truth
- jangan simpan data turunan jika bisa dihitung secara aman
- data historis akademik harus tetap bisa ditelusuri

### Important Note
Desain tabel harus mendukung **riwayat per semester dan per tahun ajaran**, bukan hanya data “saat ini”.

---

## 15. Security Rules

### Required Security Baseline
- authentication wajib untuk semua halaman internal
- role-based access control wajib
- CSRF protection aktif
- password wajib di-hash
- validasi server-side wajib
- file upload harus dibatasi dan divalidasi
- session harus aman
- route sensitif tidak boleh diakses tanpa role yang sesuai

### Never Do
- jangan simpan password plain text
- jangan percaya validasi frontend saja
- jangan expose admin routes tanpa proteksi
- jangan izinkan guru melihat/edit data di luar hak aksesnya

---

## 16. Coding Rules

### Naming Convention
- file Python: `snake_case`
- variable/function: `snake_case`
- class/model: `PascalCase`
- constants: `UPPER_CASE`

### Route Rules
- gunakan Blueprint per modul
- route harus ringkas
- route tidak boleh berisi business logic kompleks

### Service Rules
- service harus menangani proses bisnis utama
- service harus reusable
- service tidak boleh berisi rendering template

### Template Rules
- gunakan template inheritance
- pecah partial untuk navbar/sidebar/form components
- hindari copy-paste layout besar

### Database Rules
- jangan ubah tabel manual langsung di DB
- gunakan migration untuk perubahan schema
- seed data penting harus terdokumentasi

---

## 17. AI Assistant Working Rules
Project ini akan dikembangkan dengan bantuan AI assistant. Karena itu, AI harus mengikuti aturan berikut:

### AI Must Do
- bekerja per modul
- menjaga konsistensi struktur folder
- mengikuti arsitektur yang sudah ditentukan
- menjaga naming tetap konsisten
- memisahkan route, service, model, dan template
- menulis kode yang modular dan maintainable

### AI Must Not Do
- jangan membuat seluruh project sekaligus dalam satu output besar
- jangan mencampur business logic ke route
- jangan membuat arsitektur frontend SPA jika tidak diminta
- jangan mengganti stack atau pola arsitektur tanpa alasan jelas
- jangan menambahkan dependency berat tanpa kebutuhan nyata

### Preferred AI Workflow
AI diminta bekerja dalam unit kecil seperti:
- buat model tertentu
- buat blueprint modul tertentu
- buat service tertentu
- buat template halaman tertentu
- buat migration tertentu
- buat Docker config tertentu

---

## 18. Development Strategy

### Development Style
Project dibangun **bertahap**, bukan sekaligus.

### Recommended Build Order
1. Foundation Setup
2. Authentication & RBAC
3. Master Data
4. Struktur Akademik
5. Nilai
6. Absensi & Ekskul
7. Rapor
8. Dashboard
9. Import/Export
10. Hardening
11. Deployment

### Important Rule
> Jangan mulai frontend cantik sebelum backend dan data model stabil.

---

## 19. MVP Definition
Versi MVP sistem dianggap selesai jika sudah memiliki:

- login
- role access
- data guru
- data siswa
- data kelas
- data mapel
- tahun ajaran & semester
- rombel / wali kelas / pengampu
- input nilai
- absensi
- generate rapor
- export PDF

Fitur di luar itu boleh ditambahkan setelah MVP stabil.

---

## 20. Definition of Done (DoD)
Sebuah modul dianggap selesai jika:

- route berfungsi
- form validasi berjalan
- business logic utama sudah ada
- database terhubung benar
- template halaman dapat dipakai
- akses role aman
- error handling dasar ada
- minimal test relevan tersedia (jika applicable)

---

## 21. Long-Term Goal
Setelah MVP selesai, sistem dapat dikembangkan lebih lanjut menjadi:

- sistem rapor yang lebih lengkap
- portal orang tua
- approval kepala sekolah
- import massal yang lebih canggih
- dashboard analitik
- deployment sekolah/intranet
- versi production yang lebih stabil

---

## 22. Final Engineering Position
Project ini **bukan eksperimen stack modern**, melainkan sistem akademik yang harus:

- stabil
- jelas
- maintainable
- realistis
- dapat dijelaskan secara teknis
- dapat dikembangkan secara bertahap

### Final Position
> Build boring, clear, correct software first. Then improve it.