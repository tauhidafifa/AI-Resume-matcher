import streamlit as st
import fitz
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
skills = [
    "python", "java", "c++", "sql", "machine learning",
    "pandas", "numpy", "scikit-learn", "tensorflow",
    "pytorch", "git", "docker", "aws"
]
st.title("AI Resume Matcher")
st.write("Upload your resume and compare it with a job description.")
resume = st.file_uploader("Upload your resume", type=["pdf"])
job_description = st.text_area("Paste the job description")
if st.button("Analyze Resume"):
    if resume is None:
        st.error("Please upload your resume first.")
        st.stop()
    if job_description.strip() == "":
        st.error("Please enter a job description.")
        st.stop()
    try:
        doc = fitz.open(stream=resume.read(), filetype="pdf")
    except Exception:
        st.error("Could not read this PDF. Please upload a valid text-based PDF.")
        st.stop()
    resume_text = ""

    for page in doc:
        resume_text += page.get_text()

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, job_description])
    similarity = cosine_similarity(vectors[0], vectors[1])
    score = round(similarity[0][0] * 100)
        
    resume_lower = resume_text.lower()
    matched_skills = [skill for skill in skills if re.search(r"\b" + re.escape(skill) + r"\b", resume_lower)]
    job_lower = job_description.lower()
    required_skills = [skill for skill in skills if re.search(r"\b" + re.escape(skill) + r"\b", job_lower)]
    missing_skills = [skill for skill in required_skills if skill not in matched_skills]
    st.subheader("📊 Resume Analysis")
    st.warning("Missing Skills")
    st.write(", ".join(missing_skills))
    if missing_skills:
        st.info("Recommended Skills to Learn: " + ", ".join(missing_skills))
        st.write("How to Improve Your Resume:")
        for skill in missing_skills:
            st.write("• Add relevant projects or experience related to", skill)
    else:
        st.success("No major skill gaps found!")
    st.success("Matched Skills")
    st.write(", ".join(matched_skills))
    st.write(f"{len(matched_skills)} skills matched")
    st.write(f"{len(missing_skills)} skills missing")
    st.write("Resume Strengths:")
    for skill in matched_skills:
        st.write("✓", skill)
    matched_required_skills = [skill for skill in required_skills if skill in matched_skills]
    skill_score = (len(matched_required_skills) / len(required_skills)) * 100 if required_skills else 0
    st.metric("Skill Match", f"{skill_score:.0f}%")
    st.write(f"Required skills: {len(required_skills)}")
    overall_score =min((score * 0.3) + (skill_score * 0.7),100)
    st.metric("Overall Match", f"{overall_score:.0f}%")
    st.metric("Resume Match Score", f"{score}%")
    
    if overall_score >= 70:
        st.write("Strong match")
    elif overall_score >= 40:
        st.write("Moderate match")
    else:
        st.error("Low match")
    