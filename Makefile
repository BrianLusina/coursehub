# Installs dependencies
install:
	poetry install

# Runs course application
run-course:
	uvicorn course.main:app --reload --host 0.0.0.0 --port 5001

# Runs the application with reload flag set
run-reload:
	uvicorn app:app --port 5000 --reload

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
