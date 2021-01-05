PYTHON = python3

.DEFAULT_GOAL = help

help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "------------------------------------"

setup:
	@echo "Checking if project files are generated..."
	sudo apt update
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install ${PYTHON}
    sudo apt-get install python3-pip
    pipenv install

test:
	pipenv run nosetests test.py

run:
    export url='https://www.314e.com/'
	pipenv run python main.py

clean:
	rm -r *.log