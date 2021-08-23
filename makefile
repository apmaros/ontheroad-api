# must use TABS instead of spaces
# otherwise fails with makefile:X: *** missing separator.  Stop.

install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements/prod.txt
run:
	python src/main/main.py
test:
	JWT_SECRET=secret python -m pytest
