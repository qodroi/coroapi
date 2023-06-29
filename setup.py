from setuptools import setup, find_packages

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='covid19-api',
	version='1.0',
	author='Roi',
	author_email='unknown',
	description='coroapi is fast and up-to-date Covid-19 API',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/qodroi/coroapi',
	packages=find_packages(),
	package_data={'coroapi': ['countries.json']},
	include_package_data=True,
	install_requires=[
        'requests',
        'beautifulsoup4',
	  	'numpy',
      ]
)
