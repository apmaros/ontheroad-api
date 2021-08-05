# must use TABS instead of spaces
# otherwise fails with makefile:X: *** missing separator.  Stop.

install:
	PIP_CONFIG_FILE=pip.conf pip install -r requirements.txt
run:
	bin/run
test:
	echo "here come tests"
