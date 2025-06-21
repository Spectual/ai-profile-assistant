import json
import chromadb
from chromadb.config import Settings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from pathlib import Path
import os
from typing import List, Dict, Any

class RAGSystem:
    def __init__(self, openai_api_key: str, collection_name: str = "personal_data"):
        """
        Initialize RAG system
        
        Args:
            openai_api_key: OpenAI API key
            collection_name: ChromaDB collection name
        """
        self.openai_api_key = openai_api_key
        self.collection_name = collection_name
        
        # Initialize OpenAI embeddings
        self.embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        
        # Initialize ChromaDB
        self.chroma_client = chromadb.PersistentClient(
            path="./chroma_db",
            settings=Settings(anonymized_telemetry=False)
        )
        
        # Initialize text splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ".", "!", "?", "。", "！", "？"]
        )
        
        # Initialize vector database
        self.vectorstore = None
        
    def load_personal_data(self) -> Dict[str, Any]:
        """Load personal data from JSON file"""
        data_file = Path(__file__).parent / 'personal_data.json'
        if data_file.exists():
            with open(data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return self._get_default_data()
    
    def _get_default_data(self) -> Dict[str, Any]:
        """Get default data structure"""
        return {
            "basic": {
                "name": "Your Name",
                "title": "Your Title",
                "email": "your.email@example.com",
                "location": "Your Location",
                "summary": "Your professional summary here"
            },
            "skills": {
                "programmingLanguages": [],
                "mlFrameworks": [],
                "cloudPlatforms": [],
                "tools": [],
                "specialties": []
            },
            "experience": [],
            "projects": [],
            "education": [],
            "certifications": [],
            "interests": [],
            "careerGoals": ""
        }
    
    def _create_documents_from_data(self, data: Dict[str, Any]) -> List[Document]:
        """Convert personal data to document list"""
        documents = []
        
        # Basic information
        basic_info = f"""
Name: {data['basic']['name']}
Title: {data['basic']['title']}
Email: {data['basic']['email']}
Location: {data['basic']['location']}
Summary: {data['basic']['summary']}
        """.strip()
        documents.append(Document(page_content=basic_info, metadata={"type": "basic_info"}))
        
        # Skills information
        skills_info = f"""
Programming Languages: {', '.join(data['skills']['programmingLanguages'])}
Machine Learning Frameworks: {', '.join(data['skills']['mlFrameworks'])}
Cloud Platforms: {', '.join(data['skills']['cloudPlatforms'])}
Tools: {', '.join(data['skills']['tools'])}
Specialties: {', '.join(data['skills']['specialties'])}
        """.strip()
        documents.append(Document(page_content=skills_info, metadata={"type": "skills"}))
        
        # Work experience
        for i, exp in enumerate(data['experience']):
            exp_content = f"""
Work Experience {i+1}:
Position: {exp['title']}
Company: {exp['company']}
Duration: {exp['duration']}
Responsibilities: {'; '.join(exp['responsibilities'])}
Achievements: {'; '.join(exp['achievements'])}
            """.strip()
            documents.append(Document(page_content=exp_content, metadata={"type": "experience", "index": i}))
        
        # Project experience
        for i, proj in enumerate(data['projects']):
            proj_content = f"""
Project Experience {i+1}:
Project Name: {proj['name']}
Role: {proj['role']}
Duration: {proj['duration']}
Description: {proj['description']}
Technologies: {', '.join(proj['technologies'])}
Impact: {proj['impact']}
            """.strip()
            documents.append(Document(page_content=proj_content, metadata={"type": "project", "index": i}))
        
        # Education background
        for i, edu in enumerate(data['education']):
            edu_content = f"""
Education {i+1}:
Degree: {edu['degree']}
School: {edu['school']}
Year: {edu['year']}
Focus: {edu['focus']}
GPA: {edu['gpa']}
Relevant Courses: {', '.join(edu['relevantCourses'])}
            """.strip()
            documents.append(Document(page_content=edu_content, metadata={"type": "education", "index": i}))
        
        # Certifications
        if data['certifications']:
            cert_content = f"Certifications: {', '.join(data['certifications'])}"
            documents.append(Document(page_content=cert_content, metadata={"type": "certifications"}))
        
        # Interests
        if data['interests']:
            interests_content = f"Interests: {', '.join(data['interests'])}"
            documents.append(Document(page_content=interests_content, metadata={"type": "interests"}))
        
        # Career goals
        if data['careerGoals']:
            goals_content = f"Career Goals: {data['careerGoals']}"
            documents.append(Document(page_content=goals_content, metadata={"type": "career_goals"}))
        
        return documents
    
    def build_vectorstore(self):
        """Build vector database"""
        print("🔧 Building vector database...")
        
        # Load personal data
        data = self.load_personal_data()
        
        # Create documents
        documents = self._create_documents_from_data(data)
        
        # Split documents
        split_docs = []
        for doc in documents:
            splits = self.text_splitter.split_documents([doc])
            split_docs.extend(splits)
        
        print(f"📄 Created {len(split_docs)} document chunks")
        
        # Create vector database
        self.vectorstore = Chroma.from_documents(
            documents=split_docs,
            embedding=self.embeddings,
            collection_name=self.collection_name,
            client=self.chroma_client
        )
        
        print("✅ Vector database built successfully!")
    
    def search_relevant_context(self, query: str, k: int = 5) -> str:
        """
        Search for relevant context
        
        Args:
            query: User query
            k: Number of relevant documents to return
            
        Returns:
            Relevant context string
        """
        if not self.vectorstore:
            raise ValueError("Vector database not built. Call build_vectorstore() first.")
        
        # Search for relevant documents
        docs = self.vectorstore.similarity_search(query, k=k)
        
        # Build context
        context_parts = []
        for i, doc in enumerate(docs, 1):
            context_parts.append(f"Relevant Information {i}:\n{doc.page_content}")
        
        return "\n\n".join(context_parts)
    
    def get_personal_info(self) -> Dict[str, Any]:
        """Get basic personal information for system prompt"""
        data = self.load_personal_data()
        return {
            "name": data['basic']['name'],
            "title": data['basic']['title']
        } 