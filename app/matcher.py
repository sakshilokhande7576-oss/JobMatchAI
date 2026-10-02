"""
Job matching logic for JobMatchAI.
"""

from app.parser import extract_skills
from app.scorer import calculate_match


def match_resume_to_job(resume_text, job_description):
    """
    Match resume skills against skills required by a job description.
    """

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    result = calculate_match(
        resume_skills,
        job_skills
    )

    return {
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        **result,
    }