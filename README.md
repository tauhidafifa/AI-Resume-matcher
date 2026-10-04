AI Resume Matcher

An AI-powered resume analysis tool that compares a candidate's resume with a job description and provides a match score, skill analysis, and improvement recommendations.

Problem

Recruiters and job seekers often spend a lot of time manually comparing resumes with job requirements. Important skill gaps can also be missed.

Solution

AI Resume Matcher automates the resume screening process by:

Extracting text from a PDF resume
Comparing the resume with a job description
Calculating resume-to-job similarity
Identifying matched skills
Identifying missing skills
Calculating skill match percentage
Generating an overall match score
Providing resume improvement suggestions
Features
Resume Analysis

Upload a PDF resume and automatically extract its text.

Job Matching

Compare the resume with a job description using TF-IDF and Cosine Similarity.

Skill Analysis

The system identifies:

Matched skills
Missing skills
Required skills
Skill coverage percentage
Match Classification

The application classifies the resume as:

Strong Match
Moderate Match
Low Match
Resume Improvement

For missing skills, the application provides recommendations for areas the candidate can improve or add to their resume.

Technology Stack
Python
Streamlit
PyMuPDF
Scikit-learn
TF-IDF
Cosine Similarity
Regular Expressions
How It Works

Resume PDF → Text Extraction → Resume + Job Description → TF-IDF Vectorization → Cosine Similarity → Skill Extraction → Matched & Missing Skills → Skill Match + Overall Match → Recommendations

Scoring

The Overall Match score combines:

30% Resume and Job Description text similarity
70% Required skill coverage

This gives greater importance to the skills required by the job.

Installation
1. Clone the Repository

git clone <your-github-repository-url>

cd AI-Resume-matcher

2. Create a Virtual Environment

python -m venv venv

3. Activate the Virtual Environment

For Windows:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Run the Application

streamlit run app.py

The application will open in your browser at:

http://localhost:8501

Future Scope
Semantic embeddings using modern NLP models
Context-aware skill extraction
Experience and education matching
Resume section analysis
Job recommendation system
Multiple resume comparison
LLM-powered resume improvement suggestions
Deployment as a web application
Project Status

Working MVP developed for a hackathon.