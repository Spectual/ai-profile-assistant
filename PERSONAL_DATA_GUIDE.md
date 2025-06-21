# Personal Data Configuration Guide

This guide will help you edit the `backend/personal_data.json` file to customize your AI Profile Assistant information.

## File Structure

```json
{
  "basic": { ... },
  "skills": { ... },
  "experience": [ ... ],
  "projects": [ ... ],
  "education": [ ... ],
  "certifications": [ ... ],
  "interests": [ ... ],
  "careerGoals": "..."
}
```

## Basic Information (basic)

```json
{
  "basic": {
    "name": "Your Name",
    "title": "Your Professional Title",
    "email": "your.email@example.com",
    "location": "Your Location",
    "summary": "Your professional summary"
  }
}
```

**Example:**
```json
{
  "basic": {
    "name": "John Doe",
    "title": "Full Stack Developer",
    "email": "john.doe@example.com",
    "location": "San Francisco, CA",
    "summary": "I am an experienced full stack developer specializing in React, Node.js, and cloud services. With over 5 years of web development experience, I am passionate about creating user-friendly applications."
  }
}
```

## Skills (skills)

```json
{
  "skills": {
    "programmingLanguages": ["Language1", "Language2"],
    "mlFrameworks": ["ML Framework1", "ML Framework2"],
    "cloudPlatforms": ["Cloud Platform1", "Cloud Platform2"],
    "tools": ["Tool1", "Tool2"],
    "specialties": ["Specialty1", "Specialty2"]
  }
}
```

**Example:**
```json
{
  "skills": {
    "programmingLanguages": ["JavaScript", "Python", "TypeScript", "Java"],
    "mlFrameworks": ["TensorFlow", "PyTorch", "Scikit-learn"],
    "cloudPlatforms": ["AWS", "Google Cloud", "Azure"],
    "tools": ["Docker", "Kubernetes", "Git", "Jenkins"],
    "specialties": ["Frontend Development", "Backend Development", "DevOps", "Machine Learning"]
  }
}
```

## Work Experience (experience)

```json
{
  "experience": [
    {
      "title": "Job Title",
      "company": "Company Name",
      "duration": "Duration",
      "responsibilities": [
        "Responsibility 1",
        "Responsibility 2"
      ],
      "achievements": [
        "Achievement 1",
        "Achievement 2"
      ]
    }
  ]
}
```

**Example:**
```json
{
  "experience": [
    {
      "title": "Senior Frontend Developer",
      "company": "Tech Company",
      "duration": "2022 - Present",
      "responsibilities": [
        "Lead frontend development for core products",
        "Manage team of 5 frontend developers",
        "Optimize website performance and user experience"
      ],
      "achievements": [
        "Improved website loading speed by 40%",
        "Implemented responsive design for mobile devices",
        "Established frontend development standards"
      ]
    }
  ]
}
```

## Project Experience (projects)

```json
{
  "projects": [
    {
      "name": "Project Name",
      "description": "Project Description",
      "technologies": ["Technology1", "Technology2"],
      "impact": "Project Impact",
      "duration": "Project Duration",
      "role": "Your Role"
    }
  ]
}
```

**Example:**
```json
{
  "projects": [
    {
      "name": "E-commerce Platform Redesign",
      "description": "Redesigned traditional e-commerce platform into modern React application, improving user experience and system performance.",
      "technologies": ["React", "Node.js", "MongoDB", "Redis"],
      "impact": "Increased user conversion rate by 25%, reduced system response time by 60%",
      "duration": "6 months",
      "role": "Technical Lead"
    }
  ]
}
```

## Education (education)

```json
{
  "education": [
    {
      "degree": "Degree Name",
      "school": "School Name",
      "year": "Graduation Year",
      "focus": "Field of Study",
      "gpa": "GPA Score",
      "relevantCourses": ["Course1", "Course2"]
    }
  ]
}
```

**Example:**
```json
{
  "education": [
    {
      "degree": "Bachelor of Science in Computer Science",
      "school": "University of Technology",
      "year": "2020",
      "focus": "Software Engineering",
      "gpa": "3.8/4.0",
      "relevantCourses": ["Data Structures", "Algorithm Design", "Software Engineering", "Database Systems"]
    }
  ]
}
```

## Certifications (certifications)

```json
{
  "certifications": [
    "Certification1",
    "Certification2"
  ]
}
```

**Example:**
```json
{
  "certifications": [
    "AWS Certified Solutions Architect",
    "Google Cloud Professional Developer",
    "Microsoft Azure Developer Associate"
  ]
}
```

## Interests (interests)

```json
{
  "interests": [
    "Interest1",
    "Interest2"
  ]
}
```

**Example:**
```json
{
  "interests": [
    "Open source contributions",
    "Mentoring junior developers",
    "Reading latest tech research papers",
    "Hiking and outdoor photography"
  ]
}
```

## Career Goals (careerGoals)

```json
{
  "careerGoals": "Your career objectives and aspirations"
}
```

**Example:**
```json
{
  "careerGoals": "I'm passionate about building innovative software solutions that can make a positive impact on society. I'm looking for opportunities to lead cutting-edge projects, mentor talented developers, and contribute to the advancement of technology."
}
```

## Complete Example

Here's a complete example of the `personal_data.json` file:

```json
{
  "basic": {
    "name": "Your Name",
    "title": "Your Professional Title",
    "email": "your.email@example.com",
    "location": "Your Location",
    "summary": "I am a passionate professional with experience in developing innovative solutions. I specialize in modern technologies and have a strong background in software development and cloud platforms."
  },
  "skills": {
    "programmingLanguages": ["Python", "JavaScript", "TypeScript", "Java"],
    "mlFrameworks": ["TensorFlow", "PyTorch", "Scikit-learn"],
    "cloudPlatforms": ["AWS", "Google Cloud Platform", "Azure"],
    "tools": ["Docker", "Kubernetes", "Git", "Jenkins"],
    "specialties": ["Software Development", "Machine Learning", "Cloud Computing", "DevOps"]
  },
  "experience": [
    {
      "title": "Senior Software Engineer",
      "company": "Tech Company",
      "duration": "2022 - Present",
      "responsibilities": [
        "Lead development initiatives for core products",
        "Built and deployed scalable applications",
        "Mentored junior engineers"
      ],
      "achievements": [
        "Reduced application response time by 40%",
        "Implemented CI/CD pipeline",
        "Led migration to cloud infrastructure"
      ]
    }
  ],
  "projects": [
    {
      "name": "AI-Powered Chatbot Platform",
      "description": "Built an intelligent chatbot using NLP and transformer models",
      "technologies": ["Python", "Transformers", "FastAPI", "Docker"],
      "impact": "Reduced customer service workload by 60%",
      "duration": "6 months",
      "role": "Lead Developer"
    }
  ],
  "education": [
    {
      "degree": "Master of Science in Computer Science",
      "school": "University of Technology",
      "year": "2019",
      "focus": "Software Engineering and AI",
      "gpa": "3.8/4.0",
      "relevantCourses": ["Advanced Algorithms", "Machine Learning", "Software Architecture"]
    }
  ],
  "certifications": [
    "AWS Certified Solutions Architect",
    "Google Cloud Professional Developer"
  ],
  "interests": [
    "Open source contributions",
    "Mentoring junior developers",
    "Reading latest research papers"
  ],
  "careerGoals": "I'm passionate about building innovative software solutions that can make a positive impact on society."
}
```

## Updating Personal Data

After editing the `personal_data.json` file:

1. **Restart the backend server** to load the new data
2. **Rebuild the vector database** by calling the rebuild endpoint:
   ```bash
   curl -X POST http://localhost:5001/api/rebuild-vectorstore
   ```

## Tips for Better AI Responses

1. **Be Specific**: Include detailed descriptions of your responsibilities and achievements
2. **Use Action Verbs**: Start descriptions with strong action verbs
3. **Include Metrics**: Add quantifiable results when possible
4. **Keep it Professional**: Use professional language and tone
5. **Be Consistent**: Maintain consistent formatting and style throughout
6. **Update Regularly**: Keep your information current and relevant

## RAG System Integration

The RAG system will automatically:

1. **Process your data** into structured documents
2. **Chunk the content** into manageable pieces
3. **Create embeddings** for semantic search
4. **Store vectors** in the database
5. **Retrieve relevant information** based on user queries

This ensures that the AI assistant provides accurate, contextually relevant responses about your background and experience. 