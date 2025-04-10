# CPF Validator

A simple CPF (Brazilian tax ID) validator service with a client interface.

## Services

- **servidor**: Flask server that validates CPF numbers
- **cliente**: Interactive client to test CPF validation

## Running the Services

### Starting the Server

To start the server in detached mode:
```bash
docker compose up -d servidor
```

### Running the Client

To run the client in interactive mode:
```bash
docker compose run --rm cliente
```

You can now enter CPF numbers to validate them. Type 'sair' to exit.

### Stopping Everything

To stop all services:
```bash
docker compose down
```

## Notes

- The server runs on port 5000
- The client will automatically wait for the server to be available
- Both services must be running for the validation to work 