# Assumptions:
* If any repeated link is fetched then it should not be processed again.
* Word pairs is two words in same sequence and should belong to same line.
* Single charecters and numbers will be considered as independent word and
hence the frequency will be calculated for them also

# Install in Debian:
* Install python 3 and Pip3
```
sudo apt update
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.8
sudo apt-get install python3-pip
pip3 install pipenv
```
# Install Dependencies
```
pipenv install
```
# How to Run:
### Run using python script
Setup environment variable so that the root URL is available as an environment variable:
```
export url='<url-to-be-processed>'
```
Run the python script using the below command
```
python3 main.py 
```

### Run using Make command

This will run using the default URL = 'https://www.314e.com/'
```
make run
```
# How to Test:

The testcases are very well compatible with nosetest framework.

### To run testsuit using nosetests use the below command:
```
nosetests test.py
```
### The test cases can also be ran by the below make command
```
make test
```
