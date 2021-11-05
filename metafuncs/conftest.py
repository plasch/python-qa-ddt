def pytest_addoption(parser):
    parser.addoption(
        "--inp", action="store", type=str,
        help="inputs to pass to test functions, as string separated by spaces",
    )

    parser.addoption("--all", action="store_true", help="run all combinations of tests")


def pytest_generate_tests(metafunc):

    if "inp" in metafunc.fixturenames:
        metafunc.parametrize("inp", metafunc.config.getoption("--inp").split(" "))

    if "limited_param" in metafunc.fixturenames:
        end = 3
        if metafunc.config.getoption("all"): end = 10
        metafunc.parametrize("limited_param", range(end))
