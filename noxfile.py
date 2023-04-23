import nox
from nox_poetry import session

# The versions here must be in sync with the github-workflows.
# Or at least support all version from there.
# This list can contain more versions as used by the GitHub workflows to support
# custom local tests

PYTHON_VERSIONS = ["3.8", "3.10"]
SPHINX_VERSIONS = ["5.2.1", "4.5.0"]
DOCUTILS_VERSIONS = ["0.19", "0.17", "0.16", "0.15"]


TEST_DEPENDENCIES = [
    "pytest",
    "pytest-xdist",
    "myst-parser",
    "lxml",
    "pyparsing!=3.0.4",
]


def is_supported(python: str, sphinx: str, docutils: str) -> bool:
    return not (sphinx in ["4.5.0"] and docutils in ["0.19", "0.18"])


def run_tests(session, sphinx, docutils):
    session.install(".")
    session.install(*TEST_DEPENDENCIES)
    session.run("pip", "install", "-r", "docs/doc-requirements.txt", silent=True)
    session.run("pip", "install", f"sphinx=={sphinx}", silent=True)
    session.run("pip", "install", f"docutils=={docutils}", silent=True)
    session.run("echo", "TEST FINAL PACKAGE LIST", external=True)
    session.run("pip", "freeze")
    session.run("make", "test", external=True)


@session(python=PYTHON_VERSIONS)
@nox.parametrize("docutils", DOCUTILS_VERSIONS)  # order is important, last options needs to be given first ...
@nox.parametrize("sphinx", SPHINX_VERSIONS)  # ... by GH workflow
def tests(session, sphinx, docutils):
    if is_supported(session.python, sphinx, docutils):
        run_tests(session, sphinx, docutils)
    else:
        session.skip("unsupported combination")


@session(python="3.10")
def linkcheck(session):
    session.install(".")
    # LinkCheck can handle rate limits since Sphinx 3.4, which is needed as
    # our doc has too many links to GitHub.
    session.run("pip", "install", "sphinx==5.2.1", silent=True)

    session.run("pip", "install", "-r", "docs/doc-requirements.txt", silent=True)
    session.run("make", "docs-linkcheck", external=True)
