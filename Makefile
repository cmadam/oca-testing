.PHONY: all checkout install-elastic venv install-code import-data test run clean-elastic clean-data
install-elastic:
	./install-elastic.sh
checkout:
	./checkout-code.sh
venv:
	./create-venv-local.sh
install-code:
	./install-stix-shifter-kestrel-local.sh
import-data:
	./import-data-local.sh
clean-elastic:
	docker stop es01; docker rm es01
clean-data:
	rm -rf ${HOME}/huntingtest/data