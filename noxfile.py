import nox
from nox_poetry import session


@session(python="3.10")
def linkcheck(session):
    session.install(".")
    # LinkCheck can handle rate limits since Sphinx 3.4, which is needed as
    # our doc has too many links to GitHub.
    session.run("pip", "install", "sphinx==5.3", silent=True)

    session.run("pip", "install", "-r", "docs/requirements.txt", silent=True)
    session.run("make", "docs-linkcheck", external=True)
