.PHONY: test clean format all docs dist upload upload-test

install_options = "--user"

all: format test

docs:
	sphinx-build docs/ docs/build

format:
	black .

install:
	pip install -e .

test: install
	python scripts/json2latex test/test.json data test/out.tex
	cd test; pdflatex test.tex
	pdftotext test/test.pdf test/test.txt
	cd test; python test.py

clean:
	rm -rf build dist *.egg-info docs/build
	cd test; rm -f *.log *.aux *.pdf *.txt out.tex
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ | xargs rm -rf

dist:
	python setup.py sdist bdist_wheel

upload:
	twine upload dist/*

upload-test:
	twine upload dist/* --repository-url https://test.pypi.org/legacy/
