install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:	
	black *.py 

lint:
	ruff check python
	#pylint --disable=R,C  "$(git ls-files '*.py')"
	docker run --rm -i hadolint/hadolint < Dockerfile

.PHONY: check-format
check-format: ## check ruff format
	ruff format python --check

.PHONY: check-frontend-lint
check-frontend-lint: ## check frontend lint
	cd frontend && npm run lint

refactor: 
	ruff format python

build:
	cd python && python setup.py bdist_wheel --universal

deploy:
	#deploy goes here
		
all: install lint test format deploygit ls-files '*.py'