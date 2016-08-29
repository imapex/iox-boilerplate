# iox-boilerplace

A boilerplate application template for deploying applications to IOX Local Manager

# Requirements

* ioxclient
* python
* devnet sandbox or hardware platform running IOX local manager

Currently validated on the following hardware platforms

* C819HG-4G-G-K9

# Getting Started

1. Modify [./package.yaml] with your applications information
2. Add your custom code to main.py
3. Run ./deploy.sh <yourappname>


# What's included

* Logging Setup
* Using ENV variables provided by CAF
* Using third party, pure python libraries
* Using network (Expose a set of REST APIs)
* Some Build Pipeline scripts

## TODO

* CI/CD pipeline
* Unit Tests
