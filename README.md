# Evan_Li_IDS706_Hwk5

[![CI](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk5/actions/workflows/ci.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week4/actions/workflows/ci.yml)
# GitHub Actions Matrix Build for Multiple Python Versions
## Purpose of project
The purpose of this project is to test multiple python versions and environments in Github Actions. I use `setup-python` action in conjuction with `matrix strategy` to run multiple jobs with different configurations. I use a script `main.py` to check the operating system and python version

## Preparation
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 
3. make changes to any parts of the code `main.py` or `test_main.py`
4. push to see code testing in different operating systems and different python environments 

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`

eg: check lint errors:

<img width="637" alt="Screenshot 2023-09-21 at 4 26 22 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week4/assets/36715338/ccb23483-1501-49b7-b3ef-e4303da37079">


3. Test code `make test`

eg: check test cases:

<img width="1368" alt="Screenshot 2023-09-21 at 4 26 06 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week4/assets/36715338/85e027d9-e271-4f4b-97cc-0b4cdf94b6b1">

## Github actions with matrix strategy 

<img width="237" alt="Screenshot 2023-09-21 at 4 28 02 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week4/assets/36715338/1fccb552-74b9-4773-a411-b885732a57a2">
    
## References 
https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python


