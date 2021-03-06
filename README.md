# Ruuviget

A simple ruuvitag-information API server and a commandline client for displaying tempature data.

Uses the [RuuviTag Sensor Python Package](https://github.com/ttu/ruuvitag-sensor) for sensor data

# Setup

Copy example dotenv-file for configuration

```
cp .env-example .env
```

## Server

### Run natively on a linux host

Requirements

- `python >= 3.10`
- `bluez`
- `bluez-hcidump`

Exec:

```
python -m pip install -r requirements-server.txt
python -m app.server
```

### Run with docker compose on a linux host:

Exec:

```
docker compose up -d server --build
```

## Client

### Run natively

Exec:

```
python -m pip install -r requirements-cli.txt
python -m app.clients.commandline
```

With a loop repetition time of 5 seconds (instead the default of 60s):

```
python -m app.clients.commandline --repetition-in-seconds=5
```

### Run with docker compose:

Exec:

```
docker compose run commandline-client
```

With a loop repetition time of 5 seconds (instead the default of 60s):

```
docker compose run -e RUUVI_CLI_REPETITION_IN_SECONDS=5 commandline-client
```

With loop repetition disabled:

```
docker compose run -e RUUVI_CLI_REPETITION_IN_SECONDS=0 commandline-client
```

### Example commandline outputs

**Simple:** RUUVI_CLI_SIMPLE_OUTPUT=tru

```
Mac: A1:CD:EF:GH:IJ:K1 - Name: Konna K1 - Temperature: 23.78 - Humidity: 20.59
Mac: A1:CD:EF:GH:IJ:K9 - Name: Doggo K9 - Temperature: 20.95 - Humidity: 18.33
```

**Advanced:**

![Advanced output example](./resources/screenshot.png)
