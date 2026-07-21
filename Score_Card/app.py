from flask import Flask, request, render_template
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])

def fatch_data():
    student_name = request.form["name"]
    student_roll_num = request.form["roll"]
    student_class = request.form["class"]
    student_section = request.form["section"]
    #Student Marks 
    English = request.form["english"]
    Math = request.form["maths"]
    Science = request.form["science"]
    Social = request.form["social"]
    Computer = request.form["computer"]

    student_info = pd.DataFrame({
        "Name": [student_name],
        "Roll Number": [student_roll_num],
        "Class": [student_class],
        "Section": [student_section],
    })
    student_marks = pd.DataFrame({
        "english" : [English],
        "Math" : [Math],
        "Science" : [Science],
        "Social-Science" : [Social],
        "computer" : [Computer],
    })

    #To Handle Data Cleanleeeee...
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DATA_FOLDER = os.path.join(BASE_DIR, "Data")
    os.makedirs(DATA_FOLDER, exist_ok=True)

    DATA_FILE = os.path.join(DATA_FOLDER, "Data.csv")

    with open(DATA_FILE, "a+") as f:
        f.write(student_info.to_string(index=False))
        f.write("\n")
        f.write(student_marks.to_string(index=False))
        f.write("\n")
        f.write("-" * 50)
        f.write("\n")

    return "Student data saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)