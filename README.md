##Project Title:GraphHiring: AI-Powered Candidate Intelligence and Ranking System


##Problem Statement:

Recruiters often review hundreds of applications for a single job opening. Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which can overlook highly qualified candidates who possess relevant skills and potential but use different terminology in their resumes.

As a result:

Qualified candidates may be missed.
Recruiters spend significant time screening resumes.
Hiring decisions may be less accurate.
Transferable skills and candidate potential are often ignored.

The challenge is to build an AI-driven system that understands both job requirements and candidate profiles to recommend the best-fit candidates.

##Proposed Solution:

GraphHiring is an AI-powered recruitment intelligence platform that evaluates candidates using semantic understanding rather than simple keyword matching.

The system:

Reads and understands job descriptions.
Parses candidate resumes.
Extracts skills and experience.
Uses transformer-based semantic similarity to compare candidates with job requirements.
Analyzes behavioral indicators such as leadership, collaboration, and innovation.
Generates candidate scores.
Produces an explainable ranking for recruiters.

This enables recruiters to identify candidates who are genuinely suitable for a role, even when exact keywords are not present.
##ARCHITECTURE DIAGRAM:

<img width="1536" height="1024" alt="hackpgt" src="https://github.com/user-attachments/assets/ca97dce2-146f-4006-8e2b-24e4fd4c94fc" />


##Features:
Resume Parsing
Extracts text from PDF resumes
Identifies candidate skills
Semantic Matching
Uses Sentence Transformers
Understands context beyond keywords
Behavioral Intelligence

##Detects:

Leadership
Collaboration
Innovation
Adaptability
Candidate Ranking

##Generates:

Semantic score
Skill score
Behavioral score
Final ranking score
Explainable AI
Provides reasons for candidate selection.
Recruiter Dashboard


##Interactive web interface built using Streamlit.
Technology Stack
Programming Language
Python
AI & Machine Learning
Sentence Transformers
Hugging Face Models
Scikit-Learn
Data Processing
Pandas
NumPy
Resume Parsing
pdfplumber
Dashboard
Streamlit
Version Control
Git
GitHub


##Installation Steps:
Clone Repository
git clone https://github.com/YOUR_USERNAME/GraphHiring.git
cd GraphHiring
Create Virtual Environment
python -m venv venv

##Activate:

Windows
venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt





##PROJECT STRUCTURE:
GraphHiring/
│
├── data/
│   ├── jobs/
│   ├── resumes/
│   └── outputs/
│
├── src/
│   ├── parser.py
│   ├── embeddings.py
│   ├── behavior_engine.py
│   ├── ranking.py
│   ├── explainability.py
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md


##Usage:
Step 1

Place job description in:

data/jobs/job.txt
Step 2

Place resumes in:

data/resumes/
Step 3

Generate Candidate Rankings

python main.py

Output:

data/outputs/ranked_candidates.csv
Step 4

##Launch Dashboard

streamlit run src/app.py

Open:

http://localhost:8501
Sample Results
Candidate	Score
Arjun Kumar	50.11
Priya Sharma	41.17

Top-ranked candidates are recommended to recruiters.
##SCREENSHOTS:
      <img width="1466" height="1018" alt="image" src="https://github.com/user-attachments/assets/77225d67-92fb-4134-b93b-55cfda668985" />
    LAUNCHING DASHBOARD:
       <img width="1912" height="987" alt="image" src="https://github.com/user-attachments/assets/90437e0a-15ec-4280-8495-81fa9f929cde" />
##Demo Instructions:
Scenario

Job Role:

Machine Learning Engineer

Test Candidates
Arjun Kumar
Python
NLP
AWS
Docker
Priya Sharma
Java
SQL
Kubernetes
Expected Result

GraphHiring ranks Arjun Kumar higher because:

Better semantic alignment
Stronger AI skillset
More relevant experience.
##NOTE:
##Resume Upload Guidelines

##Accepted File Type:

PDF files only (.pdf)
Text-based PDFs are recommended for best AI analysis
Scanned/image-only PDFs may produce less accurate results

##Resume Content:

Include skills, experience, projects, education, and achievements
Ensure the resume text is readable and not password-protected

##Upload Limit:

Multiple resumes can be uploaded
Recommended: up to 100 resumes at a time for smooth processing in the current prototype
Larger batches may take longer depending on system resources

##File Size:

Recommended maximum: 5 MB per resume
Note:
Candidate rankings are AI-generated recommendations and should be reviewed by recruiters before making hiring decisions.

