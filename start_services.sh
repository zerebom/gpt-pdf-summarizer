
#!/bin/bash

# Start FastAPI app
uvicorn app.api.main:app --host 0.0.0.0 --port 8001 --workers 1 --reload &
# Start Streamlit app
poetry run streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0 &


# Keep the script running
wait
