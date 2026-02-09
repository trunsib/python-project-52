install:
	uv sync

migrate:
	python3 manage.py migrate

collectstatic:
	python3 manage.py collectstatic --noinput

render-start:
	gunicorn task_manager.wsgi

build:
	./build.sh
	