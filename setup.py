import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flaskErrorHandler",
    version="0.3",
    author="Parmesh Ashwath",
    author_email="parmesh20120@gmail.com",
    description="A flask package to handle exception and notify on gmail",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/parmeshashwath/flaskErrorHandler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)