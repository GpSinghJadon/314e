PYTHON = python3

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup thess project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

install:
	@echo "Installing dependencies"
	pipenv install

test:
	pipenv run nosetests test.py

run:
	pipenv run python main.py

clean:
	rm -r *.log