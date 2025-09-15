import uvicorn
import sys
from app import app  # Import your FastAPI app
from tracer import simple_tracer # Import our custom tracer

print("--- Starting server with custom tracer ---")
print("--- Send a request to http://12p0.0.1:8000 to see the trace ---")

# Activate the tracer
sys.settrace(simple_tracer)

try:
    # Run the Uvicorn server
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
finally:
    # Deactivate the tracer when the server stops
    sys.settrace(None)

print("--- Server stopped ---")