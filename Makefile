create:
	python3 -m venv venv
update libs:
	pip freeze > requirements.txt
install:
	pip install -r requirements.txt