
import os
import subprocess


def start():
    """
    Run all unittests.
    Will be used by poetry to run all test.
    Equivalent to: `poetry run python -u -m pytest tests --cov=./src`
    Will generate coverage report as well.
    """
    env = os.environ.copy()
    env["FORCE_ENV_FOR_DYNACONF"] = 'testing'
    subprocess.run(["python", "-u", "-m", "pytest", "tests", "-x", "-o", "log_cli=false", "--cov=./src"], env=env)