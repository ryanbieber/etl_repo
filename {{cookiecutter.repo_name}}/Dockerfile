FROM python:{python_version}-slim

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

# Install application into container
COPY . .

RUN python pip install -r {{cookiecutter.repo_name}}/requirements.txt

# Run the executable
ENTRYPOINT ["python", "-m", "{{cookiecutter.repo_name}}"]