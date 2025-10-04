.PHONY: default org-publish index

default:
	@echo "Usage: make org-publish|index"
	@echo "org-publish - export org files to html"
	@echo "index       - build index.html"
	make index

org-publish:
	@./scripts/org-publish.sh

index:
	@./scripts/build-index.py
