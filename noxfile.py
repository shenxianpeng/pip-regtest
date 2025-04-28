import nox

nox.options.reuse_existing_virtualenvs = True

@nox.session
def test_issue_13359(session: nox.Session) -> None:
    """Test for https://github.com/pypa/pip/issues/13359"""
    session.install("pip==25.1")
    session.install("PySide6")

@nox.session
def test_issue_13353(session: nox.Session) -> None:
    """Test for https://github.com/pypa/pip/issues/13353"""
    session.install("pip==25.1")
    session.install("aiohttp[speedups] == 3.11.16")
