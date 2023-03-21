.PHONY: all checkout install-elastic venv install-code import-data test run clean-elastic clean-data clean-all install-all
install-elastic:
	./install-elastic.sh
checkout:
	./checkout-code.sh
venv:
	./create-venv-local.sh
check-venv:
	./check-venv.sh
install-code:
	./install-stix-shifter-kestrel-local.sh
import-data:
	./import-data-local.sh
clean-elastic:
	docker stop es01; docker rm es01
clean-data:
	rm -rf ${HOME}/huntingtest/data
install-all: check-venv checkout install-code install-elastic import-data