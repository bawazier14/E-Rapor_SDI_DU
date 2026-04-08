E-Rapor SDI DU/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── extensions.py
│   │   │
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   ├── default.py
│   │   │   ├── development.py
│   │   │   ├── testing.py
│   │   │   └── production.py
│   │   │
│   │   ├── common/
│   │   │   ├── decorators.py
│   │   │   ├── permissions.py
│   │   │   ├── constants.py
│   │   │   ├── enums.py
│   │   │   ├── helpers.py
│   │   │   ├── validators.py
│   │   │   ├── exceptions.py
│   │   │   └── responses.py
│   │   │
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── user.py
│   │   │   ├── role.py
│   │   │   ├── sekolah.py
│   │   │   ├── guru.py
│   │   │   ├── siswa.py
│   │   │   ├── kelas.py
│   │   │   ├── mapel.py
│   │   │   ├── tahun_ajaran.py
│   │   │   ├── semester.py
│   │   │   ├── rombel.py
│   │   │   ├── mengajar.py
│   │   │   ├── nilai.py
│   │   │   ├── absensi.py
│   │   │   ├── ekstrakurikuler.py
│   │   │   ├── catatan.py
│   │   │   ├── rapor.py
│   │   │   ├── setting.py
│   │   │   └── audit_log.py
│   │   │
│   │   ├── repositories/
│   │   │   ├── __init__.py
│   │   │   ├── user_repository.py
│   │   │   ├── siswa_repository.py
│   │   │   ├── guru_repository.py
│   │   │   ├── kelas_repository.py
│   │   │   ├── mapel_repository.py
│   │   │   ├── nilai_repository.py
│   │   │   └── rapor_repository.py
│   │   │
│   │   ├── modules/
│   │   │   ├── auth/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── auth/
│   │   │   │           ├── login.html
│   │   │   │           └── forgot_password.html
│   │   │   │
│   │   │   ├── dashboard/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── dashboard/
│   │   │   │           └── index.html
│   │   │   │
│   │   │   ├── users/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── users/
│   │   │   │
│   │   │   ├── sekolah/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── sekolah/
│   │   │   │
│   │   │   ├── guru/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── guru/
│   │   │   │
│   │   │   ├── siswa/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── siswa/
│   │   │   │
│   │   │   ├── kelas/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── kelas/
│   │   │   │
│   │   │   ├── mapel/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── mapel/
│   │   │   │
│   │   │   ├── akademik/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── akademik/
│   │   │   │
│   │   │   ├── nilai/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   ├── calculators.py
│   │   │   │   ├── rules.py
│   │   │   │   └── templates/
│   │   │   │       └── nilai/
│   │   │   │
│   │   │   ├── absensi/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── absensi/
│   │   │   │
│   │   │   ├── ekskul/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── forms.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   └── templates/
│   │   │   │       └── ekskul/
│   │   │   │
│   │   │   ├── rapor/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   ├── pdf_service.py
│   │   │   │   └── templates/
│   │   │   │       └── rapor/
│   │   │   │           ├── preview.html
│   │   │   │           ├── print.html
│   │   │   │           └── pdf_template.html
│   │   │   │
│   │   │   ├── import_export/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── routes.py
│   │   │   │   ├── schemas.py
│   │   │   │   ├── services.py
│   │   │   │   ├── excel_importer.py
│   │   │   │   ├── excel_exporter.py
│   │   │   │   └── templates/
│   │   │   │       └── import_export/
│   │   │   │
│   │   │   └── settings/
│   │   │       ├── __init__.py
│   │   │       ├── routes.py
│   │   │       ├── forms.py
│   │   │       ├── schemas.py
│   │   │       ├── services.py
│   │   │       └── templates/
│   │   │           └── settings/
│   │   │
│   │   ├── templates/
│   │   │   ├── base.html
│   │   │   ├── layouts/
│   │   │   │   ├── app.html
│   │   │   │   └── auth.html
│   │   │   ├── partials/
│   │   │   │   ├── navbar.html
│   │   │   │   ├── sidebar.html
│   │   │   │   ├── footer.html
│   │   │   │   ├── flash_messages.html
│   │   │   │   └── breadcrumbs.html
│   │   │   └── components/
│   │   │       ├── form_field.html
│   │   │       ├── table_actions.html
│   │   │       └── modal_confirm.html
│   │   │
│   │   ├── static/
│   │   │   ├── css/
│   │   │   │   ├── app.css
│   │   │   │   ├── auth.css
│   │   │   │   └── pdf.css
│   │   │   ├── js/
│   │   │   │   ├── app.js
│   │   │   │   ├── datatables.js
│   │   │   │   ├── forms.js
│   │   │   │   └── rapor.js
│   │   │   ├── img/
│   │   │   │   ├── logo.png
│   │   │   │   └── default-avatar.png
│   │   │   ├── vendor/
│   │   │   └── uploads/
│   │   │       ├── sekolah/
│   │   │       ├── siswa/
│   │   │       └── temp/
│   │   │
│   │   └── cli/
│   │       ├── __init__.py
│   │       ├── commands.py
│   │       └── seed.py
│   │
│   ├── migrations/
│   │   ├── versions/
│   │   └── env.py
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── unit/
│   │   │   ├── test_auth_service.py
│   │   │   ├── test_nilai_calculator.py
│   │   │   └── test_rapor_service.py
│   │   ├── integration/
│   │   │   ├── test_auth_routes.py
│   │   │   ├── test_siswa_routes.py
│   │   │   └── test_rapor_routes.py
│   │   └── fixtures/
│   │       ├── users.json
│   │       ├── siswa.json
│   │       └── guru.json
│   │
│   ├── scripts/
│   │   ├── wait-for-db.sh
│   │   ├── dev-entrypoint.sh
│   │   └── prod-entrypoint.sh
│   │
│   ├── requirements/
│   │   ├── base.txt
│   │   ├── dev.txt
│   │   ├── test.txt
│   │   └── prod.txt
│   │
│   ├── .env.example
│   ├── manage.py
│   ├── wsgi.py
│   ├── pytest.ini
│   ├── pyproject.toml
│   └── alembic.ini
│
├── frontend/
│   ├── assets/
│   │   ├── ui-kit/
│   │   ├── mockups/
│   │   └── icons/
│   │
│   ├── templates-reference/
│   │   ├── dashboard/
│   │   ├── auth/
│   │   ├── siswa/
│   │   ├── guru/
│   │   ├── nilai/
│   │   └── rapor/
│   │
│   └── README.md
│
├── infra/
│   ├── nginx/
│   │   ├── default.conf
│   │   ├── production.conf
│   │   └── ssl/
│   │
│   ├── mysql/
│   │   ├── init/
│   │   │   ├── 01-create-db.sql
│   │   │   └── 02-charset.sql
│   │   ├── conf.d/
│   │   │   └── my.cnf
│   │   └── backups/
│   │
│   └── docker/
│       ├── backend/
│       │   ├── Dockerfile
│       │   └── Dockerfile.prod
│       ├── nginx/
│       │   └── Dockerfile
│       └── mysql/
│           └── Dockerfile
│
├── docs/
│   ├── architecture/
│   │   ├── system-overview.md
│   │   ├── backend-structure.md
│   │   ├── folder-structure.md
│   │   └── deployment-architecture.md
│   │
│   ├── database/
│   │   ├── erd.md
│   │   ├── schema.md
│   │   ├── migration-strategy.md
│   │   └── seed-data.md
│   │
│   ├── api/
│   │   ├── internal-routes.md
│   │   └── module-contracts.md
│   │
│   ├── modules/
│   │   ├── auth.md
│   │   ├── users.md
│   │   ├── guru.md
│   │   ├── siswa.md
│   │   ├── kelas.md
│   │   ├── mapel.md
│   │   ├── akademik.md
│   │   ├── nilai.md
│   │   ├── absensi.md
│   │   ├── ekskul.md
│   │   ├── rapor.md
│   │   └── import-export.md
│   │
│   ├── setup/
│   │   ├── local-development.md
│   │   ├── docker-setup.md
│   │   ├── environment-variables.md
│   │   └── deployment.md
│   │
│   └── ai-workflow/
│       ├── prompting-guide.md
│       ├── coding-rules.md
│       ├── module-by-module-plan.md
│       └── assistant-context.md
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md
│   │   ├── feature_request.md
│   │   └── task.md
│   │
│   ├── workflows/
│   │   ├── ci.yml
│   │   ├── lint.yml
│   │   └── test.yml
│   │
│   └── pull_request_template.md
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── docker-compose.prod.yml
├── Makefile
├── README.md
├── CONTRIBUTING.md
└── CHANGELOG.md