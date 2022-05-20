# build: docker build -t ruuviget/commandline-client -f commandline-client.dockerfile .
# run: docker run --env-file=./.env --rm ruuviget/commandline-client
FROM python:3.10
WORKDIR /usr/src/app

# App requirements
COPY requirements-cli.txt .
RUN python -m pip install --no-cache-dir -r requirements-cli.txt

# App
COPY . .

CMD [ "python", "-m", "app.clients.commandline" ]