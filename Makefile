# to run tests from within spacemacs: =SPC c c= and select "test"
test:
	pytest
version:
	echo $(PYENV_PYTHON) \
  pyenv install 3.7.2
init:
	python setup.py install

update:
	pip3 install --upgrade
