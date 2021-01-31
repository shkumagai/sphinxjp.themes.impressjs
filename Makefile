.PHONY: install update-impressjs package release-test release-prod

SRC_DIR := node_modules/impress.js
DEST_DIR := sphinxjp/themes/impressjs/templates/impressjs/static

install: node_modules
	npm install
	pip install -U pip
	pip install -r requirement.txt

update-impressjs: install
	cp -r $(SRC_DIR)/js $(DEST_DIR)/js
	cp -r $(SRC_DIR)/css $(DEST_DIR)/css

package: update-impressjs
	python setup.py sdist

release-test:
	twine upload --repository testpypi dist/*

release-prod:
	twine upload --repository testpypi dist/*

clear-dist:
	rm -rf dist/*

test:
	tox
