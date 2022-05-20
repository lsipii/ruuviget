# build: docker build -t ruuviget/server -f server.dockerfile .
# run: docker run --env-file=./.env --rm -v /var/run/dbus/:/var/run/dbus/:z --privileged --net=host ruuviget/server
FROM python:3.10
WORKDIR /usr/src/app

# Container requirements
RUN apt-get update && apt-get install -y \
    bluetooth \
    bluez \
    bluez-hcidump \
    sudo

# App requirements
COPY requirements-server.txt .
RUN python -m pip install --no-cache-dir -r requirements-server.txt

# App
COPY . .

CMD [ "python", "-m", "app.server" ]