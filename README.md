# Environment

```
cp .env.example .env
```

# Server

## Requirements

- `bluez`
- `bluez-hcidump`

```
python -m pip install -r requirements-server.txt
python -m app.server
```

With docker compose on a linux host:

```
docker compose up -d server
```

# Client

```
python -m pip install -r requirements-cli.txt
python -m app.clients.commandline
```

With docker compose:

```
docker compose run commandline-client
```

With a loop repetition time of 5 seconds:

```
docker compose run -e RUUVI_CLI_REPETITION_IN_SECONDS=5 commandline-client
```

With loop repetition disabled:

```
docker compose run -e RUUVI_CLI_REPETITION_IN_SECONDS=0 commandline-client
```

## Example cli output

```
Mac: A1:CD:EF:GH:IJ:K1 - Name: Konna Beta One - Temperature: 23.78 - Humidity: 20.59
Mac: A1:CD:EF:GH:IJ:K9 - Name: Konna Alpha Three - Temperature: 20.95 - Humidity: 18.33
```
