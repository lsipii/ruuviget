# build: docker build -t lsipii/ruuviget-commandline-client -f commandline-client.dockerfile .
# run: docker run -ti --env-file=./.env --rm lsipii/ruuviget-commandline-client
FROM python:3.10
WORKDIR /usr/src/app

# Install container depencencies
RUN apt-get update && apt-get install -y lolcat figlet gnuplot
# Add games to env
ENV PATH $PATH:/usr/games

# App requirements
COPY requirements-cli.txt .
RUN python -m pip install --no-cache-dir -r requirements-cli.txt

# App
COPY . .

CMD [ "python", "-m", "app.clients.commandline" ]