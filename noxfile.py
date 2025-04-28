import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session(python=["3.13"])
def lint(session: nox.Session) -> None:
    """Run linters."""
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files")

@nox.session
def test_issue_13359(session: nox.Session) -> None:
    """Test for https://github.com/pypa/pip/issues/13359"""
    session.install("pip==25.1")
    session.install("PySide6")
