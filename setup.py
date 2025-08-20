import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrng",
    version="0.1.3",
    author="Balu Kanuri",
    author_email="balasubramanyamkanuri@gmail.com",
    description="A Quantum Random Number Generator using IBM's Qiskit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Balukanuri/qrng-using-qiskit",
    packages=setuptools.find_packages(),
    py_modules = ['qrng'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

)

