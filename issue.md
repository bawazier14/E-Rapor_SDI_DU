# Task: Project Scaffold & Initial Folder Structure

**Objective**: Membangun fondasi awal dan struktur direktori untuk project "E-Rapor SD" sesuai dengan guidelines arsitektur yang sudah ditentukan.

Dokumen ini adalah instruksi tahap awal (scaffolding). Fokus utama pekerjaan ini HANYA membuat struktur folder dan file-file *placeholder* (file kosong / inisiasi awal). **Dilarang keras** mengimplementasikan *business logic*, skema database, atau routing yang rumit pada tahap ini.

---

## Referensi Wajib
Silakan baca dan pahami struktur yang diharapkan dari dokumen berikut sebelum memulai:
1. `CONTEXT/context_project.md` (Untuk memahami bahwa ini adalah Modular Monolith dengan Backend-First)
2. `CONTEXT/Structure.md` (Untuk melihat *blueprint* pohon direktori secara keseluruhan)

---

## High-Level Instructions

### 1. Inisialisasi Direktori Root Utama
Di *root directory* proyek, buat direktori utama berikut ini:
- `backend/`: Tempat untuk seluruh sistem aplikasi (Flask), direktori static, templates, requirement, dan test.
- `frontend/`: Tempat untuk menyimpan aset-aset desain, mockups UI, dan icon secara mentah (bukan logic frontend).
- `infra/`: Tempat untuk konfigurasi infrastruktur (Docker files, konfigurasi Nginx, dan inisialisasi MySQL).
- `docs/`: Tempat penyimpanan segala file dokumentasi teknis project.
- `.github/`: Konfigurasi *GitHub Actions* dan template *pull request* / *issue*.

### 2. Scaffold `backend/` (Flask Monolith)
Di dalam direktori `backend/`, pastikan Anda:
- Membuat folder utama `app/` dan file inisiasinya (`__init__.py`, `extensions.py`).
- Membuat sub-folder inti di dalam `app/`:
  - `config/`, `common/`, `models/`, `repositories/`, `templates/`, `static/`, dan `cli/`.
- Membangun struktur **Modular**: Di dalam folder `app/modules/`, buat masing-masing sub-folder untuk setiap domain, yaitu: `auth`, `dashboard`, `users`, `sekolah`, `guru`, `siswa`, `kelas`, `mapel`, `akademik`, `nilai`, `absensi`, `ekskul`, `rapor`, `import_export`, dan `settings`.
- Menyediakan file-file *placeholder* Python seperti `__init__.py`, `routes.py`, `services.py` secara general pada modul tanpa mengisinya.
- Membuat file inisiasi dan script *entry-point* standar seperti `manage.py`, `wsgi.py`, `pytest.ini`, dan *folder* `requirements/`.

### 3. Scaffold `infra/` (Deployment / Docker)
Sediakan kerangka file pengaturan untuk infrastruktur:
- Buat folder `nginx/` beserta file *placeholder* `default.conf`.
- Buat folder `mysql/` beserta subdirektori inisiasi `init/` dan `conf.d/`.
- Buat folder `docker/` dengan subdirektori `backend/`, `nginx/`, dan `mysql/`, dan isi dengan file `Dockerfile` kosong.

### 4. Kerangka Root File Non-Kode
Berdasarkan dokumen struktur, siapkan file-file standar repository di folder root project:
- `.env.example`
- `.gitignore` (sesuaikan dengan standar Python/Flask)
- `docker-compose.yml` (kosong / komentar awal)
- `docker-compose.prod.yml`
- `Makefile`
- `README.md` (Beri judul "E-Rapor SD")

---

## Acceptance Criteria
- [ ] Folder dan file terstruktur sama persis (*1-to-1 match*) dengan *tree layout* yang ada pada `CONTEXT/Structure.md`.
- [ ] File konfigurasi penting (seperti `docker-compose.yml`, `wsgi.py`, `__init__.py`) siap diedit untuk langkah selanjutnya.
- [ ] **Tidak ada kode implentasi fungsional** yang dimasukkan; murni inisialisasi struktur.
- [ ] Perubahan dibungkus secara rapi dalam satu commit awal (atau satu *Pull Request* jika Anda mengerjakan di branch `feature/scaffold`).
