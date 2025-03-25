# Flask + Vue.js Project

This is a full-stack web application using Flask (Python) for the backend and Vue.js for the frontend.

## Project Structure

```
.
├── backend/             # Flask backend
│   ├── app/            # Application package
│   ├── config.py       # Configuration settings
│   ├── requirements.txt # Python dependencies
│   └── run.py          # Application entry point
└── frontend/           # Vue.js frontend
    ├── src/            # Source files
    ├── public/         # Static files
    └── package.json    # Node.js dependencies
```

## Backend Setup

1. Create a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Flask application:
```bash
python run.py
```

## Frontend Setup

1. Install Node.js dependencies:
```bash
cd frontend
npm install
```

2. Run the development server:
```bash
npm run serve
```

## Development

- Backend API runs on: http://localhost:5000
- Frontend development server runs on: http://localhost:8080


![image](https://github.com/user-attachments/assets/4c9720b5-b2de-490b-8617-2df26b77adce)

