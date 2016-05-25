from setuptools import setup

setup(
        setup_requires=['pbr', 'setuptools', 'testtools'],
        test_suite='sandhisplitter.tests',
        pbr=True,
)
