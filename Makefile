# Installs dependencies
install:
	poetry install

# Runs course application
run-course:
	uvicorn apps.course.main:app --reload --host 0.0.0.0 --port 5001

# Runs user application
run-user:
	uvicorn apps.users.main:app --reload --host 0.0.0.0 --port 5002

# Runs tests
test:
	pytest

# Runs tests with coverage
test-cover:
	pytest --cov=app tests/

format:
	black app

lint:
	pylint app

load-test:
	locust --config .locust.conf

migrate-up: ## migrate schema up
	alembic upgrade head
.PHONY: migrate-up

migrate-down: ## migrate schema down
	alembic downgrade base
.PHONY: migrate-down

migrate-revision: ## Adds a revision to a migration
	alembic revision --autogenerate -m "$(ARGS)"
.PHONY: migrate-revision
