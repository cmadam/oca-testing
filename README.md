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
Run this step with this command:
```
make install-all
```
This step will:
  * checkout the code for:
    * kestrel (`develop_stixshifter_v5` branch) and 
    * stix-shifter (`develop` branch)
  * build stix-shifter and kestrel from the code
  * create a docker network named `elastic`
  * create a docker instance of elasticsearch, named `es01test`
    * store the password for `elastic` user on `es01test` in the file `${HOME}/es_pwd`
  * Import three elastic indexes in the newly created elasticsearch instance

### End-to-end test of the deployed testing environment
Run this step with this command:
```
make check-deployment
```
This step will run [a test huntbook](kestrel-test.hf) to test the deployment end-to-end.

## Running BDD tests
We are using [behave](https://github.com/behave/behave) to run the integration tests.
For now, [we have converted to BDD format](features/deployment-test.feature) the test described in the previous section.
Run the BDD tests manually with this command:
```
make bdd-tests
```

## Running the integration tests using github actions
The github actions workflow for integration testing is specified [here](.github/workflows/github-actions-flow.yml)

The github actions workflow is currently triggered every time a new commit is pushed, or a pull request is created in this repository. The workflow can also be triggered manually.   
TODO: start the workflow whenever a push request is created in the kestrel-lang or stix-shifter repository.
