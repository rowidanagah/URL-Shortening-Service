from setuptools import setup

setup(
	name = 'URL_Shortening_Service',
	version = '0.1',
	description = 'Given a URL, our services should generate a shorter alias URL',
	url ='http://127.0.0.1:5000/',
	install_requires = 'requirements.txt',
	packages = ['URL_Shortening_Service']
	)