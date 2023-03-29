# oca-testing
Integration testing for kestrel and stix-shifter

## Building the testing environment locally
### Prerequisites
Ensure that you have the following installed on your machine:
* Docker
* python (3.8 or later)
* virtualenv
* make
### Create and activate a python virtual environment
This step will create a directory named `huntingtest` in your home directory (`${HOME}` environment variable).
Then it will create a virtual environment named `huntingtest`. 
Finally, it will activate the `huntingtest` virtual environment.
```
make venv
source ${HOME}/huntingtest/huntingtest/bin/activate
```

### Bring up the testing environment
This step will:
  * checkout the code for:
    * kestrel (`develop_stixshifter_v5` branch) and 
    * stix-shifter (`develop` branch)
  * build stix-shifter and kestrel from the code
  * create a docker network named `elastic`
  * create a docker instance of elasticsearch, named `es01`
    * store the password for `elastic` user on `es01` in the file `${HOME}/es_pwd`
  * Import three elastic indexes in the newly created elasticsearch instance

### End-to-end test of the deployed testing environment

### BDD tests
