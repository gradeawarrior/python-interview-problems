VIRTUALENV?=venv

init: setup.venv
	$(info ****************)
	$(info > init)
	$(info ****************)
	source $(VIRTUALENV)/bin/activate; pip install -r requirements.txt

setup.venv:
	$(info ****************)
	$(info > setup:venv)
	$(info ****************)
	virtualenv $(VIRTUALENV)

delete.venv:
	$(info ****************)
	$(info > delete:venv)
	$(info ****************)
	rm -rf $(VIRTUALENV)

test: init
	# This runs all of the tests. To run an individual test, run py.test with
	# the -k flag, like "py.test -k test_path_is_not_double_encoded"
	$(info ****************)
	$(info > test)
	$(info ****************)
	source $(VIRTUALENV)/bin/activate; py.test tests -lvs

coverage: init
	$(info ****************)
	$(info > coverage)
	$(info ****************)
	source $(VIRTUALENV)/bin/activate; py.test --verbose --cov-report term --cov=requests tests

ci: init
	$(info ****************)
	$(info > ci)
	$(info ****************)
	source $(VIRTUALENV)/bin/activate; py.test --junitxml=junit.xml

generate.egg: clean
	$(info ****************)
	$(info > generate.egg)
	$(info ****************)
	python setup.py bdist_egg

install.egg:
	$(info ****************)
	$(info > install.egg)
	$(info ****************)
	easy_install dist/project-*.egg

publish.test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
	python setup.py bdist_wheel --universal upload
	rm -rf build dist .egg project.egg-info

clean:
	rm -rf build dist .egg project.egg-info

clean.all: clean
	rm -rf venv*
	find . -name __pycache__ | xargs rm -rf
	find . -name *.pyc | xargs rm -f

list:
	$(info ************************************)
	$(info > Here is a list of Makefile targets)
	$(info ************************************)
	@grep '^[^#[:space:]].*:' Makefile
