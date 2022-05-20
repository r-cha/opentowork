# opentowork

An experimental python backend for a webapp designed for job seekers to track
all of their job applications, from interest to acceptance.

## Environment Setup

The application requires a compatible conda environment.

```sh
conda env create -f dev-environment.yaml
conda activate otw-dev
```

## Running Locally

After activating your conda env, run the main app to start a development server.

```sh
python app/main.py
```

## Running Tests

After activating your conda env, use pytest to run unit tests.

```sh
pytest app
```

## Long term notes

- forward application status emails to user acct to automatically update search
- link to useful resources about finding a job
- "N other users tracking similar roles"
- analysis of resume/cover letter vs description
- third-party integrations (e.g. greenhouse)