FROM python:{python_version}-slim

# Install application into container
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
# Run the executable
# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}"]