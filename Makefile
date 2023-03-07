.PHONY: all checkout install-elastic venv install-code install-elastictl install-data test run cleanup
install-elastic:
	./elastic-install.sh
checkout:
	./checkout-code.sh
venv:
	./create-venv-local.sh
install-code:
	./install-stix-shifter-kestrel-local.sh
install-elastictl:
	./install-elastictl-local.sh
install-data:
	./install-data-local.sh
