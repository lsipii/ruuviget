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
