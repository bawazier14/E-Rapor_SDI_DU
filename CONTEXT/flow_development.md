# GITHUB DEVELOPMENT FLOW CONTEXT

Project ini WAJIB mengikuti workflow development GitHub yang rapi, modular, scalable, dan aman untuk development jangka panjang.

## Branch Strategy
Gunakan branch berikut secara konsisten:

- `main` = branch production / stable / siap deploy
- `develop` = branch pengembangan utama
- `feature/*` = branch untuk fitur baru
- `fix/*` = branch untuk bug di development
- `hotfix/*` = branch untuk bug darurat di production
- `release/*` = branch untuk persiapan rilis

## Aturan Branch
- DILARANG bekerja langsung di `main`
- Sebisa mungkin juga tidak bekerja langsung di `develop` untuk fitur besar
- Semua fitur baru HARUS dibuat di branch `feature/*`
- Semua bug development HARUS dibuat di branch `fix/*`
- Semua bug production HARUS dibuat di branch `hotfix/*`
- Setiap branch hanya boleh memiliki 1 fokus / 1 tujuan utama
- 1 branch = 1 fitur / 1 bug / 1 objective yang jelas

## Naming Convention Branch
Gunakan format penamaan branch berikut:

- `feature/auth-login`
- `feature/master-siswa`
- `feature/master-guru`
- `feature/input-nilai`
- `feature/generate-rapor`
- `fix/validasi-nisn`
- `hotfix/pdf-rapor-crash`
- `release/v1.0.0`

## Development Flow
Urutan kerja yang WAJIB diikuti:

1. Ambil update terbaru dari `develop`
2. Buat branch baru dari `develop`
3. Kerjakan hanya scope branch tersebut
4. Commit progress kecil dan jelas
5. Push branch ke GitHub
6. Buat Pull Request ke `develop`
7. Setelah review/testing aman, baru merge
8. Hapus branch jika sudah selesai

## Release Flow
Saat fitur-fitur utama sudah stabil:

1. Buat branch `release/*` dari `develop`
2. Fokus hanya pada:
   - bug fixing minor
   - validasi
   - test final
   - cleanup config
   - persiapan deploy
3. Setelah stabil, merge ke `main`
4. Setelah itu merge kembali ke `develop`

## Hotfix Flow
Jika ada bug di production:

1. Buat branch `hotfix/*` dari `main`
2. Perbaiki bug tersebut
3. Merge ke `main`
4. Merge juga kembali ke `develop`

## Pull Request Rules
Setiap perubahan sebaiknya diasumsikan melalui Pull Request.

Aturan PR:
- 1 PR = 1 tujuan yang jelas
- Jangan campur banyak fitur tidak terkait dalam 1 PR
- Jelaskan perubahan secara singkat dan teknis
- Sertakan testing notes jika relevan
- Hindari perubahan yang terlalu besar tanpa pemecahan scope

## Commit Convention
Gunakan format commit **Conventional Commits** berikut:

`type(scope): message`

Contoh:
- `feat(auth): add login endpoint`
- `feat(student): create student CRUD API`
- `fix(score): resolve final score calculation bug`
- `refactor(api): split service layer`
- `docs(readme): update setup instructions`
- `chore(docker): add nginx config`
- `test(auth): add login feature tests`

## Commit Types
Gunakan type berikut secara konsisten:

- `feat` = fitur baru
- `fix` = perbaikan bug
- `refactor` = perbaikan struktur internal tanpa mengubah behavior
- `docs` = dokumentasi
- `chore` = tooling / config / setup
- `test` = testing
- `style` = formatting / style code
- `perf` = optimasi performa

## Rules for AI Assistant
AI assistant HARUS mengikuti aturan berikut saat membantu development project ini:

### 1. Scope Awareness
AI harus selalu bekerja berdasarkan scope branch / task yang sedang dikerjakan.

Contoh:
- Jika branch aktif adalah `feature/master-siswa`, maka fokus hanya pada modul siswa
- Jangan menambahkan modul lain yang tidak diminta
- Jangan mencampur login, nilai, guru, rapor, dan fitur lain jika tidak diminta

### 2. Output Discipline
AI harus memberikan output yang:
- modular
- clean
- production-oriented
- maintainable
- tidak over-engineered
- sesuai arsitektur project

### 3. Code Change Discipline
Jika diminta mengubah code:
- ubah seminimal mungkin
- jangan merombak file yang tidak relevan
- jangan mengganti struktur project tanpa alasan jelas
- jangan membuat breaking change kecuali diminta

### 4. Git Awareness
Saat memberikan bantuan coding, AI harus berpikir seolah perubahan ini akan:
- dicommit
- dipush
- direview
- di-merge ke `develop`

Karena itu:
- output harus rapi
- perubahan harus terfokus
- struktur harus masuk akal untuk PR

### 5. Documentation Awareness
Jika membuat fitur baru, AI juga harus mempertimbangkan kebutuhan dokumentasi:
- route / endpoint
- request / response
- struktur database
- validasi
- dependensi antar modul

### 6. Backend-First Awareness
Project ini dikerjakan dengan pendekatan **backend-first**.

Artinya AI harus memprioritaskan urutan berikut:
1. database / schema
2. model
3. validation
4. service / business logic
5. controller / handler
6. API route
7. testing dasar
8. frontend integration

### 7. Response Style for Engineering Work
Saat diminta membuat fitur/modul, AI sebaiknya memberikan output dalam format:

- tujuan modul
- struktur file
- implementasi per file
- penjelasan singkat flow
- best practice / catatan penting
- potensi edge case (jika relevan)

## Module Development Philosophy
Project ini dikembangkan secara modular. Setiap modul harus:
- punya tanggung jawab jelas
- tidak terlalu tightly coupled
- mudah dites
- mudah dikembangkan bertahap
- mudah direview di GitHub

## Anti-Pattern yang Harus Dihindari
AI assistant dan development flow project ini HARUS menghindari hal berikut:

- bekerja langsung di `main`
- membuat fitur besar dalam satu commit raksasa
- membuat branch yang scope-nya campur aduk
- menggabungkan banyak modul berbeda dalam satu perubahan
- membuat code tanpa validasi
- membuat controller terlalu gemuk
- membuat logic bisnis bercampur dengan tampilan
- menambahkan dependency tanpa alasan jelas
- merombak arsitektur tanpa persetujuan
- menghasilkan output yang tidak siap untuk dimasukkan ke flow GitHub

## Goal Utama Workflow Ini
Workflow ini digunakan agar project:
- rapi
- scalable
- aman untuk development
- mudah dipelihara
- enak dikembangkan dengan AI assistant
- cocok untuk portfolio / skripsi / production-style project

Semua bantuan teknis, coding, refactor, dokumentasi, dan implementasi harus menghormati workflow GitHub ini.