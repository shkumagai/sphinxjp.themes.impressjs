.PHONY: update-impressjs package release-test release-prod clear-dist test

SRC_DIR := node_modules/impress.js
DEST_DIR := sphinxjp/themes/impressjs/templates/impressjs/static

update-impressjs:
	@npm install
	@cp -r $(SRC_DIR)/js $(DEST_DIR)/js
	@cp -r $(SRC_DIR)/css $(DEST_DIR)/css

package:
	@poetry run python -m build

release-test:
	@twine upload --repository testpypi dist/*

release-prod:
	@twine upload --repository pypi dist/*

clean:
	@git clean -fdx

dist-clean:
	@rm -rf dist/*

test:
	@nox -s test

lint:
	@nox -t lint

fmt:
	@nox -s fmt

security:
	@nox -s bandit

typing:
	@nox -s mypy

readme:
	@nox -s readme
