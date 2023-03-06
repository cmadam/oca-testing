.PHONY: all checkout install-elastic venv test run cleanup
install-elastic:
	./elastic-install.sh
checkout:
	./checkout-code.sh
