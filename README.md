# PlateLoc-sila2-client

Python SiLA 2 client for [PlateLoc-sila2](https://github.com/plan5-labs/PlateLoc-sila2), the SiLA 2 server for the Agilent PlateLoc thermal microplate sealer.
The client code is generated with [`sila2`](https://gitlab.com/SiLA2/sila_python) from the server's feature
definition (`PlateLocController`), so command and property names match the server.

## Installation

This package is not published on PyPI. Install it from the GitHub repository using [uv](https://docs.astral.sh/uv/).

**As a dependency of your project** (from your project's root directory):

```bash
uv add git+https://github.com/plan5-labs/PlateLoc-sila2-client.git
```

**Into an existing environment** (like `pip install`):

```bash
uv pip install git+https://github.com/plan5-labs/PlateLoc-sila2-client.git
```

**For development** (clone and install in editable mode):

```bash
git clone https://github.com/plan5-labs/PlateLoc-sila2-client.git
cd PlateLoc-sila2-client
uv sync
```

Requires Python 3.10 or later.

## Usage

Start the [PlateLoc-sila2](https://github.com/plan5-labs/PlateLoc-sila2) server first, then connect with the client:

```python
from pathlib import Path
from plateloc_controller import Client

client = Client("127.0.0.1", 5074, root_certs=Path("server-cert.pem").read_bytes())
plateloc = client.PlateLocController
plateloc.SetSealingTemperature(150)        # degrees Celsius
plateloc.SetSealingTime(3)                 # seconds
cycle = plateloc.StartCycle()              # observable command
print(plateloc.ActualTemperature.get())
```

`root_certs` is the certificate of the server (see the server's README for TLS settings).

### Example script

[`plateloc_controller/examples/snip_plateloc.py`](plateloc_controller/examples/snip_plateloc.py) contains one region per command and property.
It reads the server address from [`config.yml`](plateloc_controller/examples/config.yml) in the current directory:

```yaml
PlateLoc:
  host: 127.0.0.1
  port: 5074
  cert_path: path/to/server-cert.pem
```

Edit `host`, `port` and `cert_path`, then copy the region you need into your own script (in the same directory) and run it.

## License

MIT License. Copyright (c) 2025-2026 RIKEN. See [LICENSE](LICENSE).
