# Project

This is a very basic Python egg for developing both projects and tests. Right now, this project is configured for testing common interview questions.
	
## Usage

This project is primarily used for test development of common interview questions. The implementation for these questions can be found under the ```project``` directory. This is the equivalent of the ```src``` directory.

Unittests are written for the code, and can be found under under the ```tests``` directory. Assuming that you have all dependencies installed, you can execute all the unittests via:

	$ make test
	
This command can be run multiple times even as you fix and fine tune both your tests and your code!

Here is an example output:

	$ make test.file FILE=tests/roman_to_int_test.py
	****************
	> test.file
	****************
	# This runs a specific test. Specify FILE=tests/<file_name> in addition to this
	# target to execute a specific test.
	source venv/bin/activate; py.test tests/roman_to_int_test.py -lvs
	========================================================================================== test session starts ===========================================================================================
	platform darwin -- Python 2.7.10, pytest-2.8.7, py-1.4.31, pluggy-0.3.1 -- /Users/psalas/Dev/git/python-interview-problems/venv/bin/python
	cachedir: .cache
	rootdir: /Users/psalas/Dev/git/python-interview-problems, inifile:
	plugins: mock-0.11.0, httpbin-0.2.0, cov-2.2.1
	collected 25 items

	tests/roman_to_int_test.py::test_roman_numeral_to_int[None-0] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[-0] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[I-1] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[II-2] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[III-3] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[IV-4] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[V-5] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[VI-6] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[VII-7] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[VIII-8] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[IX-9] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[X-10] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[XIV-14] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[XIX-19] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[XLIX-49] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[XL-40] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[L-50] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[XC-90] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[C-100] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[CD-400] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[D-500] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[CM-900] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[M-1000] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[MCD-1400] PASSED
	tests/roman_to_int_test.py::test_roman_numeral_to_int[MD-1500] PASSED

	======================================================================================= 25 passed in 0.05 seconds ========================================================================================

The current output of running `make test` is checked in as [current\_test\_output.log](./current_test_output.log) in the root directory.

## Documentation

The projects homepage can be found [here](https://github.com/gradeawarrior/python-interview-problems).

## Dependencies:

### Package

* None

### Development and Tests

The current requirements for using this project are:

* Python 2.7+ (Use homebrew on Mac)
* [VirtualEnv](https://virtualenv.pypa.io/en/stable/installation/)
* make

Once installed, you can see a list of make targets via ```make list```:

	$ make list
	************************************
	> Here is a list of Makefile targets
	************************************
	init: setup.venv
	setup.venv:
	delete.venv:
	list.tests:
	test:
	test.file:
	coverage: init
	ci: init
	generate.egg: clean
	install.egg:
	publish.test:
	publish:
	clean:
	clean.all: clean delete.venv
	list:

For a first time run, you will need to install the development requirements:

	make

After setting up your environment, you can run any of the test commands very quickly!

To run tests, simply execute:

	$ make test
	
To list out all tests:

	$ make list.tests
	****************
	> list.tests
	****************
	# This will list all tests in the tests directory
	find tests -type f -name *test*.py
	tests/fibonacci_test.py
	tests/longest_substring_test.py
	tests/min_window_substring_test.py
	tests/move_zeroes_test.py
	tests/smallest_possible_integer_test.py
	tests/tintri_screening_test.py
	tests/two_sums_bst_test.py

To run a specific test:

	make test.file FILE=tests/fibonacci_test.py
	
To clean your project:

	# Clean temporary files
	$ make clean
	
	# Clean everything including venv and .pyc files
	$ make clean.all

if you would like to generate an egg of your project:

	$ make generate.egg
	
This will create an .egg file under ```dist``` directory. To install the egg:

	$ easy_install dist/project-*.egg

Or I've also included a make target to do this too!

	$ make install.egg

# Copyright

Copyright (c) 2018 Peter Salas. See LICENSE for further details.
