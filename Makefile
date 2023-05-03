SRC_FILES = sphinx_pdf_generate/

.PHONY: list
list:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

.PHONY: lint
lint:
	pre-commit run --all-files

.PHONY: test
test:
	poetry run pytest -n auto --tb=long tests/

.PHONY: docs-html
docs-html:
	poetry run sphinx-build -j auto -b html docs/ docs/_build/html

.PHONY: docs-linkcheck
docs-linkcheck:
	poetry run make --directory docs/ linkcheck

.PHONY: format
format:
	poetry run black ${SRC_FILES}
	poetry run isort ${SRC_FILES}