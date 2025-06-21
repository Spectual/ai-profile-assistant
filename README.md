# AI Profile Assistant

A React + Python personal homepage AI assistant project where users can learn about your background, skills, project experience, and more through a chat interface.

## Features

- 🤖 Intelligent AI assistant powered by OpenAI GPT-4
- 🎨 Modern UI design with dark theme support
- 📱 Responsive design for mobile devices
- 🔄 Frontend-backend separation architecture
- 📄 Configurable personal data
- 🌐 GitHub Pages deployment support
- 🧠 True RAG (Retrieval-Augmented Generation) system

## Project Structure

```
├── src/                     # Frontend React application
│   ├── components/         # React components
│   ├── pages/             # Page components
│   ├── utils/             # Utility functions
│   └── ...
├── backend/                # Backend Python API
│   ├── app.py             # Flask application
│   ├── rag_system.py      # RAG system module
│   ├── personal_data.json # Personal data
│   ├── requirements.txt   # Python dependencies
│   └── ...
├── .github/workflows/     # GitHub Actions
└── README.md
```

## Quick Start

### 1. Clone the project

```bash
git clone <your-repo-url>
cd ai-profile-assistant
```

### 2. Configure personal data

Edit the `backend/personal_data.json` file with your personal information:

```json
{
  "basic": {
    "name": "Your Name",
    "title": "Your Professional Title",
    "email": "your.email@example.com",
    "location": "Your Location",
    "summary": "Your professional summary"
  },
  "skills": {
    "programmingLanguages": ["Python", "JavaScript"],
    "mlFrameworks": ["TensorFlow", "PyTorch"],
    // ... more information
  }
  // ... other information
}
```

### 3. Set up backend

#### Option A: Local Development

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp env.example .env
# Edit .env and add your OpenAI API key
```

4. Run the backend server:
```bash
python app.py
```

The server will start at `http://localhost:5001`

### 4. Configure frontend

1. Copy `env.example` to `.env`:
```bash
cp env.example .env
```

2. Set the backend API address:
```bash
VITE_API_BASE_URL=http://localhost:5001
```

### 5. Local development

```bash
# Install frontend dependencies
npm install

# Start frontend development server
npm run dev
```

### 6. Deploy to GitHub Pages

1. Add secrets to your GitHub repository:
   - `VITE_API_BASE_URL`: Your backend API address

2. Push code to the main branch - GitHub Actions will automatically deploy

3. Enable GitHub Pages in repository settings, select the gh-pages branch

## Configuration

### Environment Variables

- `OPENAI_API_KEY`: OpenAI API key (required for backend)
- `VITE_API_BASE_URL`: Backend API address (required for frontend)

### Personal Data Configuration

The `backend/personal_data.json` file contains the following sections:

- `basic`: Basic information (name, title, email, etc.)
- `skills`: Skills list
- `experience`: Work experience
- `projects`: Project experience
- `education`: Education background
- `certifications`: Certifications
- `interests`: Interests and hobbies
- `careerGoals`: Career objectives

## API Endpoints

### POST /api/chat
Send a message to the AI assistant

### GET /api/health
Health check endpoint

### POST /api/rebuild-vectorstore
Rebuild the vector database (use after updating personal data)

## RAG System

This project implements a true RAG (Retrieval-Augmented Generation) system:

1. **Document Processing**: Converts personal data to structured documents
2. **Text Chunking**: Splits documents into manageable chunks
3. **Vectorization**: Uses OpenAI embeddings to convert text to vectors
4. **Storage**: Stores vectors in ChromaDB
5. **Retrieval**: Searches for most relevant document chunks based on user queries
6. **Generation**: Passes retrieved context to AI for response generation

### RAG Advantages

- **Precise Retrieval**: Only retrieves information relevant to the question
- **Reduced Hallucination**: Based on retrieved real information
- **Scalability**: Supports large documents and complex queries
- **Efficiency**: Avoids sending all information to AI
- **Cost Optimization**: Reduces token usage

## Technology Stack

### Frontend
- React 18
- TypeScript
- Vite
- Tailwind CSS
- shadcn/ui
- React Router

### Backend
- Python 3.8+
- Flask
- OpenAI API
- ChromaDB (vector database)
- LangChain
- CORS support

## Contributing

Issues and Pull Requests are welcome!

## License

MIT License
