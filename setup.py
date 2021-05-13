from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="cryptosnake",
    version="0.1",
    description="Simple crypto data API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/reppon97/soccer-data-api",
    author="Rejep Mammedov",
    author_email="reppon97@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
    ],
    packages=['cryptosnake'],
    include_package_data=True,
    install_requires=[
        'requests'
    ],

)
