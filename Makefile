# to run tests from within spacemacs: =SPC c c= and select "test"

test:
	pipenv run nose2

init:
	pipenv install

update:
	pipenv update
