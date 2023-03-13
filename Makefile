.PHONY: all checkout install-elastic venv install-code import-data test run cleanup
install-elastic:
	python setup_elastic.py
checkout:
	./checkout-code.sh
venv:
	./create-venv-local.sh
install-code:
	./install-stix-shifter-kestrel-local.sh
import-data:
	./import-data-local.sh
