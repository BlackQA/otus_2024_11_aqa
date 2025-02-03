import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", help="URL для проверки"
    )
    parser.addoption(
        "--status_code",
        action="store",
        default="200",
        help="Ожидаемый статус код ответа",
    )


@pytest.fixture
def url_status(request):
    url = request.config.getoption("--url")
    status_code = int(request.config.getoption("--status_code"))
    return url, status_code
