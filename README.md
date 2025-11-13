# API Playground

I found myself recently needing an example API service against which to demonstrate an API client.

The service in this container is intended to demonstrate several different API protocols, hosting nonsense
data for example purposes. See the API Documentation page for the details.

# Pre-requisites

You'll need [Docker](https://docs.docker.com/engine/) installed to build and run this container.

# Use

## Build and Run

Build the Docker container and run it in live-edit mode with:

```shell
docker compose watch
```

You can then hit the documentation landing page at [http://127.0.0.1:8008/](http://127.0.0.1:8008/).

Note that any edits to the Python code will take effect immediately.

`Ctrl+C` the running service to stop the container.

## API Documentation

With the service running, you can open [this link](http://127.0.0.1:8008/) in a browser and see the rendered [APIDOC.md](APIDOC.md) file.
