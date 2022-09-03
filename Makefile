create-venv:
	sudo apt install python3.8-venv &&\
		/usr/bin/python3 -m venv ./env &&\
			source ./env/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C hello.py

format:
	black *.py

test:
	python -m pytest -vv --cov=hello test_hello.py
