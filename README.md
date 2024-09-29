# Evan_Li_IDS706_Hwk5
 
[![CI](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk5/actions/workflows/ci.yml/badge.svg)](https://github.com/bionicotaku/Evan_Li_IDS706_Hwk5/actions/workflows/ci.yml)

This project is a simple demo to test multiple python versions and environments in Github Actions.

First, I define the python versions and OS we want to test with `matrix strategy`: `[3.8, 3.9, 3.11]` `[ubuntu-latest, windows-latest, macos-latest]`.
Then I use `setup-python` to test all the code in all the environments above.

## GitHub Actions
1. Format code `make format`
2. Lint code `make lint`
3. Test code `make test`
4. Run the code to print current environment `make run`
