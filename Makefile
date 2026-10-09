.PHONY: update-impressjs package release-test release-prod clear-dist test

SRC_DIR := node_modules/impress.js
DEST_DIR := sphinxjp/themes/impressjs/templates/impressjs/static

update-impressjs:
	@npm install
	@cp -r $(SRC_DIR)/js $(DEST_DIR)/js
	@cp -r $(SRC_DIR)/css $(DEST_DIR)/css

package:
	@uv build

release-test:
	@twine upload --repository testpypi dist/*

release-prod:
	@twine upload --repository pypi dist/*

clean:
	@git clean -fdx

dist-clean:
	@rm -rf dist/*

test:
	@uv run nox -s test

lint:
	@uv run nox -t lint

fmt:
	@uv run nox -s fmt

security:
	@uv run nox -s bandit

typing:
	@uv run nox -s mypy

readme:
	@uv run nox -s readme
