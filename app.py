import os
from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "cyber-futuristic-key-2026")

# In-memory storage for leads and profile information
crm_leads = []

user_profile = {
    "student_id": "SYS-9042",
    "full_name": "Alex Vance",
    "role": "Frontend & Visual Developer",
    "email": "alex.vance@quantum.edu",
    "program": "BCA - Computer Applications",
    "bio": "Building high-performance futuristic web portals, visual user interfaces, and automated workflows.",
    "skills": "Kotlin, Next.js, Python, Flask, UI/UX Design",
    "status": "Active",
}


@app.route("/")
def home():
    meta_description = "Next-Generation Cybernetic Student Portal and Dynamic Profile Management System."
    return render_template("index.html", title="Home Portal", meta_description=meta_description, profile=user_profile)


@app.route("/about")
def about():
    meta_description = "Learn more about the system architecture, performance metrics, and operational guidelines."
    return render_template("index.html", title="About System", page="about", meta_description=meta_description)


@app.route("/courses")
def courses():
    course_list = [
        {"code": "BCA", "name": "Bachelor of Computer Applications", "level": "Undergraduate", "duration": "3 Years"},
        {"code": "BSc", "name": "BSc in Computer Science & AI", "level": "Undergraduate", "duration": "3 Years"},
        {"code": "MCA", "name": "Master of Computer Applications", "level": "Postgraduate", "duration": "2 Years"},
        {"code": "MSc", "name": "MSc Data Science & Neural Systems", "level": "Postgraduate", "duration": "2 Years"},
    ]
    meta_description = "Explore available undergraduate and postgraduate academic degree offerings."
    return render_template("courses.html", title="Academic Programs", courses=course_list, meta_description=meta_description)


@app.route("/subjects")
def subjects():
    subject_list = [
        "Robotic Process Automation & Workflow Systems",
        "Full-Stack Web Development (Next.js / Flask)",
        "Database Architecture & Cloud Integration",
        "Object-Oriented Software Engineering",
        "Modern Visual Design & Micro-Interactions",
    ]
    meta_description = "Curriculum modules and specialized learning subjects."
    return render_template("courses.html", title="Curriculum Modules", subjects=subject_list, meta_description=meta_description)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    meta_description = "Submit student inquiries or view existing contact logs in our integrated CRM database."
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        course_interest = request.form.get("course")
        message = request.form.get("message")

        if name and email:
            crm_leads.append({"name": name, "email": email, "course": course_interest, "message": message})
            flash("Data transmitted successfully. Inquiry logged into CRM.", "success")
            return redirect(url_for("contact"))
        else:
            flash("Validation Error: Name and Email fields are required.", "error")

    return render_template("contact.html", title="Contact & Inquiries", leads=crm_leads, meta_description=meta_description)


@app.route("/profile", methods=["GET", "POST"])
def profile():
    global user_profile
    meta_description = "Create and update your personalized student profile parameters."
    if request.method == "POST":
        user_profile["student_id"] = request.form.get("student_id", "SYS-0000")
        user_profile["full_name"] = request.form.get("full_name", "Anonymous")
        user_profile["role"] = request.form.get("role", "Developer")
        user_profile["email"] = request.form.get("email", "")
        user_profile["program"] = request.form.get("program", "BCA")
        user_profile["bio"] = request.form.get("bio", "")
        user_profile["skills"] = request.form.get("skills", "")
        user_profile["status"] = request.form.get("status", "Active")

        flash("Profile information saved and updated successfully!", "success")
        return redirect(url_for("profile"))

    return render_template("profile.html", title="Profile Engine", profile=user_profile, meta_description=meta_description)


if __name__ == "__main__":
    app.run(debug=True)