import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nz_ird_validator",
    version="0.0.1",
    author="Daniel Cerezo Rodriguez",
    author_email="daniel@novahealth.co.nz",
    description="Package that validates NZ IRD numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/novahealth/nz_ird_validator.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU License",
        "Operating System :: OS Independent",
    ],
)