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
docker compose up -d
```

# Client

```
python -m pip install -r requirements-cli.txt
python -m app.clients.commandline
```

## Example cli output

```
Mac: A1:CD:EF:GH:IJ:K1 - Name: Konna Beta One - Temperature: 23.78 - Humidity: 20.59
Mac: A1:CD:EF:GH:IJ:K9 - Name: Konna Alpha Three - Temperature: 20.95 - Humidity: 18.33
```
