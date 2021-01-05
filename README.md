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
* Install Dependencies
```
pipenv install
```
# How to Run:
* Setup environment variable so that the root URL is available as an environment variable:
```
export url='<url-to-be-processed>'
```
* Run the python Script
python3 main.py

# How to Test:
* The testcases are very well compatible with nosetest framework
```
nosetests test.py
```
