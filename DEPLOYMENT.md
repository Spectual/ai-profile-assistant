# Deployment Guide

This guide will help you set up your AI Profile Assistant project for local development and deployment.

## Deployment Architecture

```
GitHub Pages (Frontend) ←→ Local Backend ←→ OpenAI API
```

## Step 1: Prepare OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Log in or create an account
3. Create a new API Key in the API Keys page
4. Copy and save the API Key (format: sk-...)

## Step 2: Set up Backend Locally

### Local Development Setup

1. **Navigate to backend directory**
   ```bash
   cd backend
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env and add your OpenAI API key
   OPENAI_API_KEY=sk-your-api-key-here
   ```

4. **Run the backend server**
   ```bash
   python app.py
   ```

The server will start at `http://localhost:5001`

## Step 3: Configure Frontend

1. **Set up environment variables**
   ```bash
   cp env.example .env
   ```

2. **Configure backend API address**
   ```bash
   VITE_API_BASE_URL=http://localhost:5001
   ```

3. **Install dependencies and start development server**
   ```bash
   npm install
   npm run dev
   ```

## Step 4: Deploy to GitHub Pages (Optional)

1. **Add secrets to your GitHub repository**
   - Go to your GitHub repository
   - Click "Settings" → "Secrets and variables" → "Actions"
   - Click "New repository secret"
   - Add:
     - Name: `VITE_API_BASE_URL`
     - Value: Your backend URL (e.g., http://localhost:5001 for local development)

2. **Push code to trigger deployment**
   ```bash
   git add .
   git commit -m "Configure for deployment"
   git push origin main
   ```

3. **Enable GitHub Pages**
   - Go to repository "Settings" → "Pages"
   - Source: Select "Deploy from a branch"
   - Branch: Select `gh-pages`
   - Click "Save"

## Step 5: Test Deployment

1. **Test backend API**
   ```bash
   curl http://localhost:5001/api/health
   ```
   Should return: `{"status":"healthy","message":"AI Assistant API is running"}`

2. **Test frontend**
   - Visit your local development URL (usually http://localhost:5173)
   - Try sending a message to the AI assistant
   - Check if you get a proper response

## Troubleshooting

### Backend Issues

1. **API Key Error**
   - Check if environment variables are set correctly
   - Ensure API Key format is correct (starts with sk-)

2. **Dependency Installation Failed**
   - Check if `requirements.txt` file exists
   - Ensure Python version is compatible (recommended 3.8+)

3. **Port Issues**
   - Ensure port 5001 is available
   - Check if another service is using the same port

### Frontend Issues

1. **API Connection Failed**
   - Check if `VITE_API_BASE_URL` is set correctly
   - Ensure backend URL is accessible

2. **Build Failed**
   - Check if all dependencies are installed correctly
   - Ensure Node.js version is compatible

3. **CORS Errors**
   - Backend is configured with CORS support
   - If issues persist, check if backend URL is correct

## Personal Data Configuration

### Update Personal Information

1. Edit `backend/personal_data.json` file with your information
2. Restart the backend server
3. Call the rebuild endpoint to update the vector database:
   ```bash
   curl -X POST http://localhost:5001/api/rebuild-vectorstore
   ```

### Data Structure

The personal data file includes:
- `basic`: Basic information (name, title, email, etc.)
- `skills`: Skills list
- `experience`: Work experience
- `projects`: Project experience
- `education`: Education background
- `certifications`: Certifications
- `interests`: Interests and hobbies
- `careerGoals`: Career objectives

## RAG System Management

### Vector Database

- The RAG system automatically builds a vector database from your personal data
- Vector database is stored in `chroma_db/` directory
- Rebuild vector database after updating personal data

### Performance Optimization

- Adjust chunk size in `rag_system.py` for better performance
- Modify similarity search parameters as needed
- Monitor API usage and costs

## Security Considerations

1. **API Key Security**
   - Never hardcode API keys in your code
   - Use environment variables for sensitive information
   - Rotate API keys regularly

2. **Access Control**
   - Consider adding rate limiting for production use
   - Monitor for unusual access patterns

3. **Data Privacy**
   - Ensure personal data doesn't contain sensitive information
   - Regularly review AI conversation content

## Monitoring and Maintenance

1. **Monitor API Usage**
   - Regularly check OpenAI API usage
   - Set up usage alerts

2. **Update Personal Data**
   - Edit `backend/personal_data.json` file
   - Restart backend and rebuild vector database

3. **Backup Data**
   - Regularly backup personal data
   - Save API keys to a secure location

## Development Workflow

1. **Local Development**
   - Run backend on localhost:5001
   - Run frontend on localhost:5173
   - Make changes and test locally

2. **Testing**
   - Test all API endpoints
   - Verify RAG system functionality
   - Check frontend-backend communication

3. **Deployment**
   - Push changes to GitHub
   - GitHub Actions will build and deploy frontend
   - Backend remains local for development 