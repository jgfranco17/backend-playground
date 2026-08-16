# API Reference

Backend Playground exposes a small set of endpoints. Unversioned endpoints live at the
root; feature endpoints are versioned under `/v0`.

For interactive exploration, run the API locally and open `/docs` (Swagger UI) or
`/redoc`.

## Root endpoints

### `GET /`

Returns a static greeting. Useful as a smoke test that the service is up.

```bash
curl http://localhost:8000/
```

```json
{ "message": "Hello, world!" }
```

### `GET /healthz`

Health check endpoint, used by the Docker healthcheck defined in the `Dockerfile`.

```bash
curl http://localhost:8000/healthz
```

```json
{ "status": "healthy" }
```

## v0 endpoints

### `GET /v0/greet`

Returns a personalized greeting.

#### Query parameters

| Name   | Type   | Required | Description   |
| ------ | ------ | -------- | ------------- |
| `name` | string | Yes      | Name to greet |

#### Success response

```bash
curl "http://localhost:8000/v0/greet?name=Ada"
```

```json
{ "message": "Hello, Ada!" }
```

#### Error response

Omitting `name` returns a `400 Bad Request`:

```bash
curl "http://localhost:8000/v0/greet"
```

```json
{ "status": 400, "message": "Name cannot be empty" }
```

## Error format

All `HTTPException`s raised by the API are caught by a shared exception handler
(`api/service.py`) and returned as JSON in a consistent shape:

```json
{ "status": "<http status code>", "message": "<detail>" }
```
