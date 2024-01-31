import nox


@nox.session(python=["3.9", "3.10", "3.11"])
def test(session):
    """Run test"""

    session.install(".")
    session.run(
        "sphinx-build",
        "-b",
        "html",
        "-d",
        "_build/doctree",
        "docs",
        "_build/html",
        env={
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONNOWARNINGS": "once",
        },
    )


@nox.session(tags=["style", "lint"])
def ruff(session):
    """Run Ruff."""
    posargs = session.posargs if session.posargs else ["check", "src", "noxfile.py"]

    session.install("ruff")
    session.run("ruff", *posargs)


@nox.session
def fmt(session):
    """Run format."""

    posargs = (
        session.posargs if session.posargs else ["format", "-q", "src", "noxfile.py"]
    )

    session.notify("ruff", posargs=posargs)


@nox.session(tags=["style", "lint"])
def flake8(session):
    """Run flake8."""

    posargs = session.posargs if session.posargs else ["src"]

    session.install("flake8")
    session.install("flake8-copyright")
    session.install("flake8-commas")
    session.install("flake8-print")
    session.install("flake8-return")
    session.install("flake8-string-format")
    session.run("flake8", *posargs)


@nox.session(tags=["style", "lint"])
def isort(session):
    """Run isort."""

    posargs = session.posargs if session.posargs else ["src"]

    session.install("isort")
    session.run("isort", "--check-only", "--diff", *posargs)


@nox.session(tags=["security"])
def bandit(session):
    """Run bandit."""

    posargs = session.posargs if session.posargs else ["src"]

    session.install("bandit")
    session.run("bandit", "--quiet", "-r", *posargs)


@nox.session(tags=["typing"])
def mypy(session):
    """Run mypy."""

    posargs = session.posargs if session.posargs else ["src"]

    session.install("mypy")
    session.install("types-docutils")
    session.run("mypy", *posargs)


@nox.session
def readme(session):
    """Run readme check by twine."""

    session.install("build")
    session.install("twine")
    session.run("python", "-m", "build")
    session.run("twine", "check", "dist/*")
