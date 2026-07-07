from flask import Flask, jsonify

__version__ = "1.0.0"

app = Flask(__name__)


@app.get("/")
def index():
    """Return the application welcome payload."""
    return jsonify(message="Usine logicielle", version=__version__)


@app.get("/health")
def health():
    """Return the health status used by CI, Docker and Kubernetes probes."""
    return jsonify(status="ok"), 200


@app.get("/version")
def version():
    """Return the current application version."""
    return jsonify(version=__version__)


if __name__ == "__main__":
    app.run()
