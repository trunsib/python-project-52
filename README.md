### Hexlet tests and linter status:
[![Actions Status](https://github.com/trunsib/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/trunsib/python-project-52/actions)

# Hexlet Task Manager

Простой менеджер задач на Django для учебного проекта Hexlet.

## Ссылка на задеплоенное приложение

[Открыть приложение в браузере](https://python-project-52-k2nz.onrender.com)

## Локальный запуск

1. Клонируем репозиторий:

```bash
git clone <ссылка-на-твой-репозиторий>
cd hexlet-code

uv venv
source .venv/bin/activate   # Linux / Mac
# или
.venv\Scripts\activate      # Windows

uv sync

make migrate

make collectstatic

python manage.py runserver

