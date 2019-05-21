# nz_ird_validator
A validator for New Zealand tax numbers (IRD)

## Installation

Follow this guide:
https://packaging.python.org/tutorials/packaging-projects/

if you would like to create your own package

# IRD VALIDATION PYTHON PACKAGE

A validator for New Zealand tax numbers (IRD)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

```
pip install git+https://github.com/novahealth/nz_ird_validator.git
```

### Usage

```
import nz_ird_validator

is_ird_valid = nz_ird_validator.is_valid("123-456-789")

if is_ird_valid:
    print("IRD IS VALID")
else:
    print("IRD IS NOT VALID")
```

## Built With

* [Python](https://www.python.org/) - Programming language
* [Pycharm](https://www.jetbrains.com/pycharm/) - IDE

## Authors

* **Daniel Cerezo Rodriguez** - *Initial work* - [Nova Health](https://novahealth.co.nz/)

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details