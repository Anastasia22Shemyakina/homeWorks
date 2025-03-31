import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        action="store",
        default=200,
        help="Expected status code"
    )

@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--url")

@pytest.fixture(scope="session")
def expected_status(request):
    return int(request.config.getoption("--status_code"))
