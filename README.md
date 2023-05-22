# PDF Summarizer with GPT and Streamlit

### [Blog](https://zenn.dev/zerebom/articles/1ffd51da420c9e)
### [Slide](https://speakerdeck.com/zerebom/chatgpttonohui-hua-nodetafen-xi-kai-fa-dui-hua-wozui-shi-hua-surutamenozhi-zhen-tote-xing)

## About
This project is a PDF summarizer that leverages GPT AI to generate summaries from uploaded PDF files. The application uses FastAPI for the backend and Streamlit for the frontend. The project was created with the assistance of AI language models.

## Getting Started

These instructions will help you set up and run the project on your local machine for development and testing purposes.

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
```
git clone https://github.com/zerebom/gpt-pdf-summarizer.git
cd gpt-pdf-summarizer
```
2. Build and run the Docker container using Docker Compose:

This command will build the Docker image, start the container, and run both FastAPI and Streamlit applications.
```
docker-compose up --build
```


3. Access the applications:

- FastAPI: Open your browser and navigate to `http://localhost:8001`. You will see the FastAPI documentation (Swagger UI).
- Streamlit: Open your browser and navigate to `http://localhost:8501`. You will see the Streamlit user interface where you can upload PDF files and get summaries.

### Usage

1. In the Streamlit app,
upload a PDF file using the file uploader.

2. Once the file is uploaded, the application will extract the text from the PDF and send it to the GPT API for summarization.

3. The summarized text will be displayed on the Streamlit app. You can also interact with the GPT AI to ask questions about the summarized content.

## Project Structure

The project is organized as follows:
```
project_name/
├── app/
│ ├── api/
│ │ ├── init.py
│ │ ├── dependencies.py
│ │ ├── main.py
│ │ └── pdf_summary.py
│ ├── core/
│ │ ├── init.py
│ │ ├── config.py
│ │ └── settings.py
│ ├── db/
│ │ ├── init.py
│ │ ├── database.py
│ │ └── models.py
│ ├── services/
│ │ ├── init.py
│ │ ├── pdf_extraction.py
│ │ └── openai_api.py
│ ├── main.py
│ └── tests/
│ ├── init.py
│ ├── conftest.py
│ └── test_pdf_summary.py
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── README.md
```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to the project.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
