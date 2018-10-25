import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


INSTALL_REQUIRES = (
    ['pandas', 'requests']
)


setuptools.setup(
    name="yahoo_finance_api",
    version="0.0.1",
    author="Mayank Wadhwa",
    author_email="mayankwadhwa@outlook.in",
    description="Yahoo finance api for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mayankwadhwa/Yahoo-Finance-Python",
    packages=setuptools.find_packages(),
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
