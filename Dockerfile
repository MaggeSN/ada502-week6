FROM python
COPY temp_store .
COPY pyproject.toml .
RUN pip install pipx
RUN pipx install poetry
RUN /root/.local/bin/poetry install
CMD ["/root/.local/bin/poetry","run","uvicorn","temp_store.main:app"]
