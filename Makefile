# to run tests from within spacemacs: =SPC c c= and select "test"

test:
	nose2

init:
	pip install -r requirements.txt

upgrade:
	pip install --upgrade -r requirements-to-freeze.txt && \
	pip freeze > requirements.txt

tags:
	${HOME}/bin/pyfiles.py | xargs etags -a
