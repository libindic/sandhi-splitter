# Sandhi Splitter

[![Build Status](https://travis-ci.org/libindic/sandhi-splitter.svg?branch=master)](https://travis-ci.org/libindic/sandhi-splitter)
[![Coverage Status](https://coveralls.io/repos/github/libindic/sandhi-splitter/badge.svg?branch=master)](https://coveralls.io/github/libindic/sandhi-splitter?branch=master)


A probabalistic approach to solving the problem of agglutination which
exists in indic languages. Implementation here applies for Malayalam,
although codes used are mostly language agnostic.

# Training

Training is done using the script `sandhisplitter/train.py`
To test the code, do the following
``` bash
	git clone https://github.com/libindic/sandhi-splitter.git
    cd sandhi-splitter
    virtualenv env --python=/usr/bin/python3
    . env/bin/activate
    python setup.py install
```

After installation, with necessary arguments, use
```bash
    python sandhisplitter/train.py [args]
    python sandhisplitter/test.py [args]

```
Help is provided in the console.

# Using Module

1. First clone the repository
```
	git clone https://github.com/libindic/sandhi-splitter.git
```
2. Create a installable source and then install using pip
```
	python setup.py sdist
	pip install dist/sandhisplitter*.tar.gz
```

Note: We suggest you work on virtualenv instead of installing
system-wide using `sudo`, since module is still under development.



