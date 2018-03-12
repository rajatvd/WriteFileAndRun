
from setuptools import setup

long_description = """IPython cell magic which builds on top of the writefile cell magic. It also optionally runs the cell after writing it to the file."""

setup(name='writefile_run',
		version='0.3',
		description='IPython cell magic to write a cell to a file and run it',
		long_description=long_description,
		author='Rajat Vadiraj Dwaraknath',
		url='https://github.com/rajatvd/WriteFileAndRun',
		install_requires=['ipython'],
		author_email='rajatvd@gmail.com',
		license='MIT',
		packages=['writefile_run'],
		zip_safe=False)
