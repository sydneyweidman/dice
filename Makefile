
test:
	nose2 -v

init:
	pip install -r requirements.txt

upgrade:
	pip install --upgrade -r requirements-to-freeze.txt && \
	pip freeze > requirements.txt

tags: TAGS
	${HOME}/bin/pyfiles.py | xargs etags -a
