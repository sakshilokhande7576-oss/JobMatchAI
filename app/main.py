"""
Command-line interface for JobMatchAI.
"""

from app.matcher import match_resume_to_job


def main():
    print("\n===== JobMatchAI =====")

    print("\nPaste your Resume text.")
    print("When finished, press Enter twice.\n")

    resume_lines = []

    while True:
        line = input()
        if line == "":
            break
        resume_lines.append(line)

    resume_text = "\n".join(resume_lines)

    print("\nPaste the Job Description.")
    print("When finished, press Enter twice.\n")

    job_lines = []

    while True:
        line = input()
        if line == "":
            break
        job_lines.append(line)

    job_description = "\n".join(job_lines)

    result = match_resume_to_job(
        resume_text,
        job_description
    )

    matched_count = result["matched_count"]
    total_required = result["total_required"]

    print("\n===== ATS MATCH REPORT =====")
    print(f"Overall Match: {result['match_percentage']}%")
    print(f"Skill Coverage: {matched_count} / {total_required}")

    print("\nMatched Skills:")

    if result["matched_skills"]:
        for skill in result["matched_skills"]:
            print(f"  ✓ {skill}")
    else:
        print("  None")

    print("\nMissing Skills:")

    if result["missing_skills"]:
        for skill in result["missing_skills"]:
            print(f"  - {skill}")
    else:
        print("  None")

    print("\nRecommendation:")

    if result["missing_skills"]:
        missing = ", ".join(result["missing_skills"])
        print(f"  Focus on the missing skills: {missing}.")
    else:
        print("  Your resume covers all detected job skills.")


if __name__ == "__main__":
    main()