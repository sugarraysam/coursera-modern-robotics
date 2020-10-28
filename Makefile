export IPYTHONDIR = $(PWD)/.ipython

.PHONY: ipython
ipython:
	@pipenv run ipython;
