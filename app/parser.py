"""
Resume and job description text parser for JobMatchAI.
"""


def normalize_text(text):
    """Normalize text for matching."""
    if not isinstance(text, str):
        return ""

    return " ".join(text.lower().strip().split())


def extract_keywords(text):
    """
    Extract common technical/job-related keywords from text.
    """

    normalized = normalize_text(text)

    known_skills = [
        "python",
        "java",
        "sql",
        "mysql",
        "excel",
        "pandas",
        "numpy",
        "power bi",
        "tableau",
        "flask",
        "fastapi",
        "rest api",
        "html",
        "css",
        "javascript",
        "git",
        "github",
        "aws",
        "lambda",
        "s3",
        "ec2",
        "docker",
        "linux",
        "machine learning",
        "deep learning",
        "tensorflow",
        "scikit-learn",
        "data analysis",
        "data analytics",
        "data visualization",
        "api",
        "json",
        "ai",
        "artificial intelligence",
    ]

    found = []

    for skill in known_skills:
        if skill in normalized:
            found.append(skill)

    return sorted(set(found))


def extract_skills(text):
    """Backward-compatible alias for skill extraction."""
    return extract_keywords(text)


def parse_resume(text):
    """Parse resume text and extract relevant skills."""

    return {
        "type": "resume",
        "skills": extract_keywords(text),
        "text": normalize_text(text),
    }


def parse_job_description(text):
    """Parse a job description and extract required skills."""

    return {
        "type": "job_description",
        "skills": extract_keywords(text),
        "text": normalize_text(text),
    }