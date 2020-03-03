import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name                          = "basemath",
    version                       = "1.0",
    license                       = "MIT",
    author                        = "eerne/m13kj",
    author_email                  = "infinitumco666@gmail.com",
    description                   = "A small library to work with numbers of any base",
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/m13kj/basemath",
    packages                      = setuptools.find_packages(),
    classifiers                   = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        ],
    python_requires = ">=3.6",
    )
