HOSTNAME=github.com
NAMESPACE=relaypro-open
NAME=dog_api_python
BINARY=${NAME}
VERSION=1.0.4
OS_ARCH=linux_amd64

github_release:
	sed -i 's/^version = \".*\"/version = \"${VERSION}\"/g' pyproject.toml
	git add -f pyproject.toml
	git commit -m "release tag: ${VERSION}"
	git tag ${VERSION}
	git push --tags --force

delete_release:
	git tag -d ${VERSION}
	git push --delete origin ${VERSION}
