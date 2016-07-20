# Sandhi Splitter

[![Build Status](https://travis-ci.org/libindic/sandhi-splitter.svg?branch=master)](https://travis-ci.org/libindic/sandhi-splitter)
[![Coverage Status](https://coveralls.io/repos/github/libindic/sandhi-splitter/badge.svg?branch=master)](https://coveralls.io/github/libindic/sandhi-splitter?branch=master)


A probabalistic approach to solving the problem of agglutination which
exists in indic languages. Implementation here applies for Malayalam,
although codes used are mostly language agnostic.

# Installation 

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

# Training and Testing

Training is done using the script `sandhisplitter/train.py`
To test the code, do the following:

After installation, with necessary arguments, use
```bash
    sandhisplitter_train [args]
    sandhisplitter_benchmark_model [args]
```

For more details, refer to [docs/index.rst](https://github.com/jerinphilip/sandhi-splitter/blob/master/docs/index.rst)


# Using the Sandhisplitter class

`Sandhisplitter` class provides two main functions, `split` and `join`.

```python
>>> from sandhisplitter import Sandhisplitter
>>> s = Sandhisplitter()
>>> s.split('ആദ്യമെത്തി')
(['ആദ്യം', 'എത്തി'], [4])
>>> s.split('വയ്യാതെയായി')
(['വയ്യാതെ', 'ആയി'], [7])
>>> s.split('എന്നെക്കൊണ്ടുവയ്യ')
(['എന്നെക്കൊണ്ടുവയ്യ'], [])
>>> s.split('ഇന്നത്തെക്കാലത്ത്')
(['ഇന്നത്തെക്കാലത്ത്'], [])
>>> s.split('എന്തൊക്കെയോ')
(['എന്ത്', 'ഒക്കെയോ'], [3])

>>> s.join(['ആദ്യം', 'ആയി'])
'ആദ്യമായി'
```
