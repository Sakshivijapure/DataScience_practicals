# # from flask import Flask, render_template, request, redirect, url_for, flash
# # import requests
# # import uuid

# # app = Flask(__name__)
# # app.secret_key = "secret_key"

# # # -----------------------------
# # # FastAPI backend URL
# # # -----------------------------
# # FASTAPI_URL = "http://127.0.0.1:8000/courses"

# # # -----------------------------
# # # Helper function to fetch courses
# # # -----------------------------
# # def load_courses():
# #     try:
# #         response = requests.get(FASTAPI_URL)
# #         response.raise_for_status()
# #         data = response.json()
# #         # Ensure each course has a unique 'id' for Flask routing
# #         for c in data:
# #             if "id" not in c:
# #                 c["id"] = str(uuid.uuid4())
# #         return data
# #     except Exception as e:
# #         flash(f"Error fetching courses: {e}")
# #         return []

# # # -----------------------------
# # # Routes
# # # -----------------------------
# # @app.route("/")
# # def index():
# #     courses = load_courses()
# #     return render_template("index.html", courses=courses)

# # @app.route("/add", methods=["GET", "POST"])
# # def add_course():
# #     if request.method == "POST":
# #         new_course = {
# #             "course_name": request.form["course_name"],
# #             "provider": request.form["provider"],
# #             "skills": request.form["skills"],
# #             "rating": float(request.form["rating"] or 0),
# #             "total_reviews": int(request.form["total_reviews"] or 0),
# #             "level": request.form["level"],
# #             "duration": request.form["duration"]
# #         }
# #         try:
# #             # Send POST request to FastAPI
# #             resp = requests.post(f"{FASTAPI_URL}/", json=new_course)
# #             resp.raise_for_status()
# #             flash("Course added successfully!")
# #         except Exception as e:
# #             flash(f"Error adding course: {e}")
# #         return redirect(url_for("index"))
# #     return render_template("form.html", action="Add", course=None)

# # @app.route("/edit/<int:id>", methods=["GET", "POST"])
# # def edit_course(id):
# #     # Get course data
# #     try:
# #         course = requests.get(f"{FASTAPI_URL}/{id}").json()
# #     except Exception as e:
# #         flash(f"Error fetching course: {e}")
# #         return redirect(url_for("index"))

# #     if request.method == "POST":
# #         updated_course = {
# #             "course_name": request.form["course_name"],
# #             "provider": request.form["provider"],
# #             "skills": request.form["skills"],
# #             "rating": float(request.form["rating"] or 0),
# #             "total_reviews": int(request.form["total_reviews"] or 0),
# #             "level": request.form["level"],
# #             "duration": request.form["duration"]
# #         }
# #         try:
# #             resp = requests.put(f"{FASTAPI_URL}/{id}", json=updated_course)
# #             resp.raise_for_status()
# #             flash("Course updated successfully!")
# #         except Exception as e:
# #             flash(f"Error updating course: {e}")
# #         return redirect(url_for("index"))

# #     return render_template("form.html", action="Edit", course=course)

# # @app.route("/delete/<int:id>", methods=["POST"])
# # def delete_course(id):
# #     try:
# #         resp = requests.delete(f"{FASTAPI_URL}/{id}")
# #         resp.raise_for_status()
# #         flash("Course deleted successfully!")
# #     except Exception as e:
# #         flash(f"Error deleting course: {e}")
# #     return redirect(url_for("index"))

# # # -----------------------------
# # # Run Flask app
# # # -----------------------------
# # if __name__ == "__main__":
# #     app.run(debug=True)


# from flask import Flask, render_template, request, redirect, url_for, flash
# import requests

# app = Flask(__name__)
# app.secret_key = "secret_key"

# FASTAPI_URL = "http://127.0.0.1:8000/courses"

# # Fetch courses from FastAPI
# def get_courses():
#     try:
#         response = requests.get(FASTAPI_URL)
#         return response.json()
#     except Exception as e:
#         print("Error fetching courses:", e)
#         return []

# @app.route("/")
# def index():
#     courses = get_courses()
#     return render_template("index.html", courses=courses)

# @app.route("/add", methods=["GET", "POST"])
# def add_course():
#     if request.method == "POST":
#         new_course = {
#             "course_name": request.form["course_name"],
#             "provider": request.form["provider"],
#             "skills": request.form.get("skills", ""),
#             "rating": float(request.form.get("rating", 0)),
#             "total_reviews": int(request.form.get("total_reviews", 0)),
#             "level": request.form.get("level", ""),
#             "duration": request.form.get("duration", "")
#         }
#         requests.post(FASTAPI_URL, json=new_course)
#         flash("Course added successfully!")
#         return redirect(url_for("index"))
#     return render_template("form.html", action="Add", course=None)

# @app.route("/edit/<int:course_id>", methods=["GET", "POST"])
# def edit_course(course_id):
#     course = requests.get(f"{FASTAPI_URL}/{course_id}").json()
#     if request.method == "POST":
#         updated_course = {
#             "course_name": request.form["course_name"],
#             "provider": request.form["provider"],
#             "skills": request.form.get("skills", ""),
#             "rating": float(request.form.get("rating", 0)),
#             "total_reviews": int(request.form.get("total_reviews", 0)),
#             "level": request.form.get("level", ""),
#             "duration": request.form.get("duration", "")
#         }
#         requests.put(f"{FASTAPI_URL}/{course_id}", json=updated_course)
#         flash("Course updated successfully!")
#         return redirect(url_for("index"))
#     return render_template("form.html", action="Edit", course=course)

# @app.route("/delete/<int:course_id>", methods=["POST"])
# def delete_course(course_id):
#     requests.delete(f"{FASTAPI_URL}/{course_id}")
#     flash("Course deleted successfully!")
#     return redirect(url_for("index"))

# @app.route('/fetch', methods=['GET'])
# def fetch_courses():
#     courses = get_all_courses_from_db()  # your function to fetch courses
#     return redirect(url_for('index'))     # or return JSON if using API


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "secret_key"

FASTAPI_URL = "http://127.0.0.1:8000/courses"

# Fetch courses from FastAPI
def get_courses():
    try:
        response = requests.get(FASTAPI_URL)
        return response.json()
    except Exception as e:
        print("Error fetching courses:", e)
        return []

@app.route("/")
def index():
    courses = get_courses()
    return render_template("index.html", courses=courses)

@app.route("/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        new_course = {
            "course_name": request.form["course_name"],
            "provider": request.form["provider"],
            "skills": request.form.get("skills", ""),
            "rating": float(request.form.get("rating", 0)),
            "total_reviews": int(request.form.get("total_reviews", 0)),
            "level": request.form.get("level", ""),
            "duration": request.form.get("duration", "")
        }
        requests.post(FASTAPI_URL, json=new_course)
        flash("Course added successfully!")
        return redirect(url_for("index"))
    return render_template("form.html", action="Add", course=None)

@app.route("/edit/<int:course_id>", methods=["GET", "POST"])
def edit_course(course_id):
    course = requests.get(f"{FASTAPI_URL}/{course_id}").json()
    if request.method == "POST":
        updated_course = {
            "course_name": request.form["course_name"],
            "provider": request.form["provider"],
            "skills": request.form.get("skills", ""),
            "rating": float(request.form.get("rating", 0)),
            "total_reviews": int(request.form.get("total_reviews", 0)),
            "level": request.form.get("level", ""),
            "duration": request.form.get("duration", "")
        }
        requests.put(f"{FASTAPI_URL}/{course_id}", json=updated_course)
        flash("Course updated successfully!")
        return redirect(url_for("index"))
    return render_template("form.html", action="Edit", course=course)

@app.route("/delete/<int:course_id>", methods=["POST"])
def delete_course(course_id):
    requests.delete(f"{FASTAPI_URL}/{course_id}")
    flash("Course deleted successfully!")
    return redirect(url_for("index"))

@app.route("/reload")
def reload_courses():
    flash("Courses reloaded!")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
