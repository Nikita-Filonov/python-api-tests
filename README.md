# Python API tests

## Links

- [Allure Report on GitHub Pages](https://nikita-filonov.github.io/python-api-tests/8/index.html)
- [GitHub Actions CI/CD](https://github.com/Nikita-Filonov/python-api-tests/actions)

## Overview

This project provides an example of API testing for a [REST API](https://en.wikipedia.org/wiki/REST) using Python. It
incorporates powerful libraries and best practices to ensure maintainability, readability, and efficiency. Key
technologies and methodologies used in this project include:

- [HTTPX](https://www.python-httpx.org/) – A powerful and efficient HTTP client for making API requests.
- [Pydantic](https://docs.pydantic.dev/latest/) – Used for data validation, deserialization, and serialization.
- [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) – Manages test settings in a
  structured and maintainable way.
- [Faker](https://faker.readthedocs.io/en/master/) – Generates fake data for testing purposes.
- [Pytest](https://docs.pytest.org/en/stable/) – A full-featured and powerful testing framework in Python.
- [JSON Schema validation](https://python-jsonschema.readthedocs.io/en/stable/) – Ensures contract testing by validating
  API responses against predefined schemas.
- [Allure](https://allurereport.org/) – A comprehensive test reporting framework that provides detailed and visually
  appealing reports.
- [Assertions in separate functions](./tools/assertions) – Encourages reusable and atomic test assertions.
- [API client abstraction](./clients/operations_client.py) – Encapsulates API interaction logic for better modularity
  and reusability.
- [Base API client](./clients/base_client.py) – Serves as the entry point for all HTTP calls.
- [Logging features](./tools/logger.py) – Improves test readability and debugging, especially in CI/CD environments.
- [Routing as Enum](./tools/routes.py) – Replaces raw string URLs with an enumerated routing system for better
  maintainability.
- [Pytest plugins](./fixtures) – Moves fixtures out of conftest.py to keep the test suite organized and manageable.
- [HTTPX event hooks](./clients/event_hooks.py) – Enables logging and additional features without modifying the original
  API client code.

This project targets[SampleAPIs](https://sampleapis.com/), which provides various fake API datasets for testing.
Specifically, this project works with the [FakeBank API](https://sampleapis.com/api-list/fakebank) and uses its
endpoints for testing purposes.

## Setup Instructions

### Prerequisites

Ensure that you have the following installed on your system:

- Python 3.11 or later
- pip (Python package manager)
- Git

## Installation

Clone the repository and navigate to the project directory:

```shell
git clone https://github.com/Nikita-Filonov/python-api-tests.git
cd python-api-tests
```

Create and activate a virtual environment:

```shell
python -m venv venv # Create virtual environment
source venv/bin/activate # Activate on macOS/Linux
venv\Scripts\activate # Activate on Windows
```

Install dependencies:

```shell
pip install --upgrade pip # Upgrade pip to the latest version
pip install -r requirements.txt # Install required dependencies
```

## Running Tests

To run API tests using pytest:

```shell
pytest -m regression --numprocesses 2 # Run regression tests in parallel
```

## Generating Allure Reports

Run tests and generate Allure results:

```shell
pytest -m regression --alluredir=allure-results
```

To serve the Allure report locally:

```shell
allure serve allure-results
```

## Running Tests in CI/CD

Tests are automatically executed in a CI/CD pipeline using [GitHub Actions](https://github.com/features/actions). The
workflow is configured to:

- Run tests on every push and pull request to the main branch.
- Generate and upload Allure reports as artifacts.
- Publish the[ Allure report](https://allurereport.org/) to [GitHub Pages](https://pages.github.com/) for easy access.

Ensure that the [gh-pages](https://github.com/Nikita-Filonov/python-api-tests/tree/gh-pages) branch exists in your
repository for successful deployment. If it does not exist, create it manually:

```shell
git checkout --orphan gh-pages
```

Then push the new branch:

```shell
git push origin gh-pages
```

To allow GitHub Actions to publish the report, enable Workflow permissions:

- Open your repository on GitHub.
- Go to Settings > Actions > General.
- Scroll down to Workflow permissions.
- Select Read and write permissions.
- Click Save.

Once set up, your tests will run automatically, and the Allure report will be deployed to GitHub Pages.

## Accessing Allure Reports

After a successful test run in CI/CD:

- The Allure report will be available at [GitHub Pages](https://nikita-filonov.github.io/python-api-tests/8/index.html).
- The workflow logs and artifacts can be accessed
  via [GitHub Actions](https://github.com/Nikita-Filonov/python-api-tests/actions).
- If the [*pages build and deployment*](https://github.com/Nikita-Filonov/python-api-tests/actions/runs/14155385792)
  workflow does not appear, verify your GitHub Pages settings:
    - Go to Settings > Pages.
    - Under Build and deployment, ensure the source is set to the `gh-pages` branch.

## Documentation for Used Actions

For detailed information on GitHub Actions used in this project, refer to the following:

- [Checkout Action](https://github.com/actions/checkout)
- [Setup Python Action](https://github.com/actions/setup-python)
- [Upload Artifact Action](https://github.com/actions/upload-artifact)
- [Download Artifact Action](https://github.com/actions/download-artifact)
- [Allure Report Action](https://github.com/simple-elf/allure-report-action)
- [GitHub Pages Deployment Action](https://github.com/peaceiris/actions-gh-pages)

## Summary

This project serves as a reference implementation for writing clean, maintainable, and effective API tests in Python. It
showcases best practices such as using a dedicated API client, structured assertions, logging, and CI/CD integration
with Allure reporting. The setup allows for easy test execution locally and in CI/CD environments, ensuring high-quality
automated testing with minimal manual intervention.

