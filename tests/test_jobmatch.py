"""# JobMatchAI
# No external dependencies required.
Automated tests for JobMatchAI.
"""

import unittest

from app.parser import extract_skills
from app.scorer import calculate_match
from app.matcher import match_resume_to_job


class TestParser(unittest.TestCase):

    def test_extract_skills(self):
        text = "Python, SQL, Flask, AWS and Git"
        skills = extract_skills(text)

        self.assertIn("python", skills)
        self.assertIn("sql", skills)
        self.assertIn("flask", skills)
        self.assertIn("aws", skills)
        self.assertIn("git", skills)


class TestScorer(unittest.TestCase):

    def test_calculate_match(self):
        resume_skills = ["python", "sql", "flask"]
        job_skills = ["python", "sql", "flask", "aws"]

        result = calculate_match(
            resume_skills,
            job_skills
        )

        self.assertEqual(result["matched_count"], 3)
        self.assertEqual(result["total_required"], 4)
        self.assertEqual(result["match_percentage"], 75.0)

        self.assertEqual(
            result["missing_skills"],
            ["aws"]
        )


class TestMatcher(unittest.TestCase):

    def test_match_resume_to_job(self):
        resume = """
        Python developer with Python, SQL, Flask and Git.
        """

        job = """
        Python developer with Python, SQL, Flask, Git and AWS.
        """

        result = match_resume_to_job(
            resume,
            job
        )

        self.assertEqual(
            result["match_percentage"],
            80.0
        )

        self.assertEqual(
            result["matched_count"],
            4
        )

        self.assertEqual(
            result["total_required"],
            5
        )

        self.assertIn(
            "aws",
            result["missing_skills"]
        )


if __name__ == "__main__":
    unittest.main()