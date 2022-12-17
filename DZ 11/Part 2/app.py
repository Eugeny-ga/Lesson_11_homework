from flask import Flask, render_template

from utils import get_all, get_candidate_by_id, get_candidates_by_name, get_candidates_by_skill
app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_all()
    return render_template("list.html", candidates=candidates)


@app.route("/candidate/<int:id>/")
def candidate_profile(id):
    candidate = get_candidate_by_id(id)

    return render_template("single.html", candidate=candidate)

@app.route("/search/<candidate_name>")
def candidate_name(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    count = len(candidates)
    return render_template('search.html', candidates=candidates, count=count)


@app.route("/skills/<skill>/")
def page_skills(skill):
    candidates = get_candidates_by_skill(skill)
    count = len(candidates)
    return render_template('skill.html', count=count, skill=skill, candidates=candidates)


if __name__ == "__main__":
    app.run()
