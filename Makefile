# export PYTHONASYNCIODEBUG=1
# export PYTHONWARNINGS=default

test:
	nosetests -vv \
	--with-coverage \
	--cover-package=backend \
	--cover-erase \
	--cover-min-percentage=85 \
	--cover-html \
	--cover-branches \
	--cover-xml

isort:
	isort --check-only --recursive backend

flake8:
	flake8 backend/ --max-complexity=10  --count --max-line-length=80 --import-order-style=google

install:
	python setup.py install

publish-test:
	python setup.py register -r pypitest
	python setup.py sdist upload -r pypitest

publish:
	python setup.py register -r pypi
	python setup.py sdist upload -r pypi
	
clean:
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete
	rm -rf .coverage build cover compliance/reports dist docs/_build htmlcov MANIFEST nosetests.xml backend.egg-info .tox coverage.xml