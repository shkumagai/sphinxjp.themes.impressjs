.PHONY: update-impressjs package release-test release-prod clear-dist test

SRC_DIR := node_modules/impress.js
DEST_DIR := sphinxjp/themes/impressjs/templates/impressjs/static

update-impressjs:
	npm install
	cp -r $(SRC_DIR)/js $(DEST_DIR)/js
	cp -r $(SRC_DIR)/css $(DEST_DIR)/css

package:
	poetry build

release-test:
	twine upload --repository testpypi dist/*

release-prod:
	twine upload --repository pypi dist/*

clear-dist:
	rm -rf dist/*

test:
	tox
