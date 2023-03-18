
#!/bin/bash

# Start FastAPI app
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 1 --reload &
# Start Streamlit app
streamlit run app/main.py --server.port 8501 --server.address 0.0.0.0 &


# Keep the script running
wait
