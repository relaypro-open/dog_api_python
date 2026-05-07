HOSTNAME=github.com
NAMESPACE=relaypro-open
NAME=dog_api_python
BINARY=${NAME}
VERSION=1.0.4
OS_ARCH=linux_amd64

.PHONY: wheel clean github_release delete_release

wheel:
	python3 -m pip install --upgrade build
	python3 -m build --wheel

clean:
	rm -rf build/ dist/ src/*.egg-info

github_release:
	sed -i 's/^version = \".*\"/version = \"${VERSION}\"/g' pyproject.toml
	git add -f pyproject.toml
	git commit -m "release tag: ${VERSION}"
	git tag ${VERSION}
	git push --tags --force

delete_release:
	git tag -d ${VERSION}
	git push --delete origin ${VERSION}
