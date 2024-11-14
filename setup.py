#!/usr/bin/env python

import setuptools

# Pinning tenacity as the api has changed slightly which breaks all tests.
application_dependencies = []
prod_dependencies = []
test_dependencies = []
lint_dependencies = []
docs_dependencies = []
dev_dependencies = []
deploy_dependencies = []


with open("README.md", "r") as fh:
    long_description = fh.read()


with open("VERSION", "r") as buf:
    version = buf.read()


setuptools.setup(
    name="dog_api_python",
    version=version,
    description="Separate the high level client implementation from the underlying CRUD.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Drew Gulino",
    author_email="dgulino@relaypro.com",
    url="https://github.com/relaypro-open/dog_api_python",
    python_requires=">=3.7",
    packages=["dog"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    install_requires=application_dependencies,
    extras_require={
        #"production": prod_dependencies,
        #"test": test_dependencies,
        #"lint": lint_dependencies,
        #"docs": dev_dependencies,
        #"dev": dev_dependencies,
        #"deploy": deploy_dependencies,
    },
    include_package_data=True,
    zip_safe=False,
)
