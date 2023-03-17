#!/bin/bash

project_name="/home/kokoro/gpt-pdf-summariser"

mkdir -p ${project_name}/app/api
mkdir -p ${project_name}/app/core
mkdir -p ${project_name}/app/db
mkdir -p ${project_name}/app/services
mkdir -p ${project_name}/app/tests

touch ${project_name}/app/api/__init__.py
touch ${project_name}/app/api/dependencies.py
touch ${project_name}/app/api/main.py
touch ${project_name}/app/api/pdf_summary.py

touch ${project_name}/app/core/__init__.py
touch ${project_name}/app/core/config.py
touch ${project_name}/app/core/settings.py

touch ${project_name}/app/db/__init__.py
touch ${project_name}/app/db/database.py
touch ${project_name}/app/db/models.py

touch ${project_name}/app/services/__init__.py
touch ${project_name}/app/services/pdf_extraction.py
touch ${project_name}/app/services/openai_api.py

touch ${project_name}/app/main.py

touch ${project_name}/app/tests/__init__.py
touch ${project_name}/app/tests/conftest.py
touch ${project_name}/app/tests/test_pdf_summary.py

touch ${project_name}/.gitignore
touch ${project_name}/Dockerfile
touch ${project_name}/docker-compose.yml
touch ${project_name}/pyproject.toml
touch ${project_name}/README.md
