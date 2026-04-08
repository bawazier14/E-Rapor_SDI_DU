# Task: Project Dependency Setup

**Objective**: Menyiapkan dan mengonfigurasi seluruh dependensi Python yang diperlukan untuk pengembangan, pengujian, dan produksi aplikasi "E-Rapor SD".

Tujuan dari tugas ini adalah mengisi file-file `requirements/*.txt` dengan *library* yang sesuai dengan spesifikasi teknologi proyek. Instruksi ini bersifat *high-level*; implementor diharapkan memilih versi yang stabil dan kompatibel untuk Python 3.12.

---

## Referensi Wajib
1. `CONTEXT/context_project.md` (Bagian: Final Tech Stack)
2. `CONTEXT/Structure.md` (Bagian: `backend/requirements/`)

---

## High-Level Instructions

### 1. Dasar Pemisahan Dependensi
Gunakan pola modular untuk dependensi di dalam folder `backend/requirements/`:
- **`base.txt`**: Library inti aplikasi (Flask, ORM, Validation, Reporting).
- **`dev.txt`**: Tools untuk pengembangan (Linters, formatters). Harus menyertakan `-r base.txt`.
- **`test.txt`**: Framework pengujian. Harus menyertakan `-r base.txt`.
- **`prod.txt`**: Server produksi dan library spesifik deployment. Harus menyertakan `-r base.txt`.

### 2. Kategori Dependensi Inti (`base.txt`)
Identifikasi dan tambahkan library untuk fungsi berikut:
- **Web Framework & App**: Flask dan ekstensi dasarnya (Login, WTF, Session).
- **Database & Migration**: SQLAlchemy, Flask-Migrate, dan driver MySQL yang sesuai.
- **Reporting & File Handling**: Library untuk pembuatan PDF (WeasyPrint) dan Excel (openpyxl).
- **Utility**: Library pendukung seperti Pillow untuk pengolahan gambar ringan.

### 3. Tooling Pengembangan & Testing (`dev.txt` & `test.txt`)
Siapkan ekosistem pengerjaan yang rapi:
- Tambahkan library untuk *code quality* (Black, Isort, Flake8).
- Tambahkan framework pengujian (Pytest).

### 4. Produksi (`prod.txt`)
- Tambahkan WSGI HTTP Server yang direkomendasikan (Gunicorn).

### 5. Verifikasi Instalasi
- Pastikan semua dependensi dapat diinstal dalam *virtual environment* Python 3.12 tanpa konflik versi yang besar.

---

## Acceptance Criteria
- [ ] File `base.txt`, `dev.txt`, `test.txt`, dan `prod.txt` terisi dengan daftar library yang relevan.
- [ ] Tidak ada dependensi yang saling bertabrakan (conflict).
- [ ] Seluruh library yang disebutkan di `context_project.md` sudah terakomodasi.
- [ ] Struktur `-r base.txt` pada file dependensi lainnya sudah diterapkan dengan benar.
