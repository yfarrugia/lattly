__author__ = 'yanikafarrugia'

from setuptools import setup, find_packages

with open('README.md') as f:
	readme = f.read()
with open('LICENSE') as f:
	license = f.read()

setup(
	name = 'lattly',
	version = '0.1.0',
	description = 'Bringing People Together',
	long_description = readme,
	author = 'Yanika Farrugia',
	author_email = 'farrugia.yani@gmail.com',
	url = 'https://github.com/yfarrugia/lattly',
	license = license,
	packages = find_packages(exclude = ('lattly_tests', 'lattly_docs'))
)
