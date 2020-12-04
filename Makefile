CONDA_ENV ?= portfolio_management

.PHONY: all test clean

test:
	@pytest -s .

eslint:
	yarn run eslint api/static/js

env.create:
	@conda create -y -n ${CONDA_ENV} python=3.7

env.update:
	@conda env update -n ${CONDA_ENV} -f environment.yml
