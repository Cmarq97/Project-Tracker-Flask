"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    grades = hackbright.get_grades_by_github(github)

    html = render_template("student_info.html",
                           first=first,
                           last=last,
                           github=github,
                           grades=grades)
    return html


@app.route("/project-search")
def get_project_form():
    """Show form for searching for a project."""

    return render_template("project_search.html")


@app.route("/project")
def get_project():
    """Show information about a project"""
    title = request.args.get('title')

    project = hackbright.get_project_by_title(title)

    completed_projects = hackbright.get_grades_by_title(title)

    html = render_template("project_info.html", project=project, grades=completed_projects)

    return html


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/add-student")
def add_student():
    return render_template("add_student.html")


@app.route("/new-student", methods=['POST'])
def new_student():
    """Added a student."""

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')
    hackbright.make_new_student(first, last, github)

    html = render_template("new_student.html",
                           first=first,
                           last=last,
                           github=github)
    return html


if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
