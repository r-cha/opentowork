# opentowork [![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/downloads/release/python-3105/) [![Unit Tests](https://github.com/r-cha/opentowork/actions/workflows/python-app.yml/badge.svg)](https://github.com/r-cha/opentowork/actions/workflows/python-app.yml)



An experimental python backend for a webapp designed for job seekers to track
all of their job applications, from interest to acceptance.

## Getting Started

### Environment Setup

The application requires a compatible virtual environment.
Conda is the preferred environment manager (see dev-environment.yaml).

```sh
conda env create -f etc/dev-environment.yaml
conda activate otw-dev
```

### Running Locally

After activating your conda env, run the main app with uvicorn to start a development server.

```sh
uvicorn app.main:app --reload
```

### Running Tests

After activating your conda env, use pytest to run unit tests.

```sh
pytest app
```

## Contributing

Check out open Issues, and if one does not match your need, open a new one.

Feeling bold? After reviewing our [CONTRIBUTING](./CONTRIBUTING.md) guidelines and [CODE OF CONDUCT](./CODE_OF_CONDUCT.md),
solve your own Issue by opening a Pull Request!

## License

[THE ANTI-CAPITALIST SOFTWARE LICENSE](./LICENSE.md)

### What??

If you're an individual using OpenToWork for yourself, you have nothing to fear!
