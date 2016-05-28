travis:
	python setup.py test --coverage \
		--coverage-package-name=sandhisplitter
	flake8 --max-complexity 10 sandhisplitter
clean:
	find . -iname "*.pyc" -exec rm -vf {} \;
	find . -iname "__pycache__" -delete
