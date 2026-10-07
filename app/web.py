"""
Flask web interface for JobMatchAI.
"""

from flask import Flask, render_template, request

from app.matcher import match_resume_to_job


app = Flask(__name__, template_folder="../templates")


@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        resume_text = request.form.get("resume", "")
        job_description = request.form.get("job_description", "")

        result = match_resume_to_job(
            resume_text,
            job_description
        )

    return render_template(
        "index.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
