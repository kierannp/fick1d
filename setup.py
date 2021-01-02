import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fick1d", # Replace with your own username
    version="0.0.1",
    author="Kieran Nehil",
    author_email="nehilkieran@gmail.com",
    description="A small package for solving Fick's Second law in 1-dimension for various geometries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kierannp/fick1d",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
