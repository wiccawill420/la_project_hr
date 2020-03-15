from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='hr',
    version='0.1.0',
    description='Manage users on a server based on an inventory json file',
    long_description=readme,
    author='William',
    author_email='wiccawill420@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)

