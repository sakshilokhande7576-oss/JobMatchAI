"""
ATS scoring logic for JobMatchAI.
"""


def calculate_match(resume_skills, job_skills):
    """
    Calculate ATS-style skill matching between a resume and job description.
    """

    resume_set = set(resume_skills)
    job_set = set(job_skills)

    matched_skills = sorted(resume_set.intersection(job_set))
    missing_skills = sorted(job_set - resume_set)

    total_required = len(job_set)
    matched_count = len(matched_skills)

    if total_required == 0:
        match_percentage = 0.0
    else:
        match_percentage = round(
            (matched_count / total_required) * 100,
            2
        )

    return {
        "match_percentage": match_percentage,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "matched_count": matched_count,
        "total_required": total_required,
    }