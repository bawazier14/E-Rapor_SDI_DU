.PHONY: build up down restart logs shell db-shell migrate upgrade downgrade test

# Docker commands
build:
	docker compose build

up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

logs:
	docker compose logs -f backend

# App CLI
shell:
	docker compose exec backend flask shell

db-shell:
	docker compose exec db mysql -u root -prootpassword erapor_sd

# Migrations
migrate:
	docker compose exec backend flask db migrate -m "$(m)"

upgrade:
	docker compose exec backend flask db upgrade

downgrade:
	docker compose exec backend flask db downgrade

# Testing
test:
	docker compose exec backend pytest
