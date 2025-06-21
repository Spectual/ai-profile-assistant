from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import json
from pathlib import Path
from dotenv import load_dotenv
from rag_system import RAGSystem

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Get OpenAI API key from environment variables and create client
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key) if api_key else None

# Initialize RAG system
rag_system = None
if api_key:
    rag_system = RAGSystem(api_key)
    # Build vector database
    rag_system.build_vectorstore()

# Debug information
print(f"🔍 Environment check:")
print(f"   OPENAI_API_KEY from env: {'✅ Set' if api_key else '❌ Not found'}")
if api_key:
    print(f"   API Key prefix: {api_key[:7]}...")
    print(f"   RAG System: {'✅ Initialized' if rag_system else '❌ Failed to initialize'}")
else:
    print("   Please set OPENAI_API_KEY environment variable")
print()

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Check if API key is set
        if not api_key:
            return jsonify({
                'error': 'OpenAI API key not configured. Please set OPENAI_API_KEY environment variable.',
                'success': False
            }), 500
        
        # Check if RAG system is initialized
        if not rag_system:
            return jsonify({
                'error': 'RAG system not initialized',
                'success': False
            }), 500
        
        # Use RAG system to search for relevant context
        try:
            relevant_context = rag_system.search_relevant_context(message, k=3)
            print(f"🔍 Retrieved {len(relevant_context.split('Relevant Information'))} relevant contexts")
        except Exception as e:
            print(f"⚠️  RAG search failed: {e}")
            relevant_context = "Unable to retrieve relevant information"
        
        # Get personal information
        personal_info = rag_system.get_personal_info()
        
        # Build system prompt
        system_prompt = f"""You are {personal_info['name']}'s AI assistant. Answer questions about {personal_info['name']} based on the following relevant information retrieved from the knowledge base:

RELEVANT CONTEXT:
{relevant_context}

INSTRUCTIONS:
- Answer questions based on the relevant context above
- If the context doesn't contain enough information, acknowledge the limitation
- Keep responses conversational, helpful, and professional
- Provide specific details from the context when relevant
- If asked about something not covered in the context, offer related information you do have
- Always respond in the same language as the user's question
"""

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7,
            max_tokens=500,
        )
        
        ai_response = response.choices[0].message.content
        
        return jsonify({
            'response': ai_response,
            'success': True,
            'context_used': relevant_context[:200] + "..." if len(relevant_context) > 200 else relevant_context
        })
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({
            'error': 'Failed to get AI response',
            'success': False
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    api_key_status = "configured" if api_key else "not configured"
    rag_status = "initialized" if rag_system else "not initialized"
    return jsonify({
        'status': 'healthy', 
        'message': 'AI Assistant API is running',
        'api_key': api_key_status,
        'rag_system': rag_status
    })

@app.route('/api/rebuild-vectorstore', methods=['POST'])
def rebuild_vectorstore():
    """Rebuild vector database"""
    try:
        if not api_key:
            return jsonify({
                'error': 'OpenAI API key not configured',
                'success': False
            }), 500
        
        global rag_system
        rag_system = RAGSystem(api_key)
        rag_system.build_vectorstore()
        
        return jsonify({
            'message': 'Vector database rebuilt successfully',
            'success': True
        })
        
    except Exception as e:
        print(f"Error rebuilding vectorstore: {str(e)}")
        return jsonify({
            'error': 'Failed to rebuild vector database',
            'success': False
        }), 500

if __name__ == '__main__':
    print("🚀 Starting AI Assistant Backend with RAG...")
    print(f"📡 API Key Status: {'✅ Configured' if api_key else '❌ Not configured'}")
    print(f"🧠 RAG System: {'✅ Ready' if rag_system else '❌ Not ready'}")
    print("🌐 Server will be available at: http://localhost:5001")
    print("📋 API Endpoints:")
    print("   - POST /api/chat - Send message to AI (with RAG)")
    print("   - GET  /api/health - Health check")
    print("   - POST /api/rebuild-vectorstore - Rebuild vector database")
    print("\n💡 Make sure to set OPENAI_API_KEY environment variable")
    app.run(debug=True, host='0.0.0.0', port=5001) 