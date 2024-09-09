#cgpa2.0
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Function to convert grades to points
def default_grade(grade):
    if grade == 'O':
        return 10
    elif grade == 'A+':
        return 9
    elif grade == 'A':
        return 8
    elif grade == 'B+':
        return 7
    elif grade == 'B':
        return 6
    elif grade == 'C':
        return 5
    elif grade == 'U' or grade == 'SA' or grade == 'W' or grade == 'WH':
        return 0
    else:
        return None

# HTML template as a string
html_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SGPA & CGPA Calculator</title>
</head>
<body>
    <h1>SGPA Calculator</h1>
    <form action="/calculate_sgpa" method="post">
        <label for="maths">Maths:</label>
        <input type="text" id="maths" name="maths" required><br>
        <label for="ids">IDS:</label>
        <input type="text" id="ids" name="ids" required><br>
        <label for="dbms">DBMS:</label>
        <input type="text" id="dbms" name="dbms" required><br>
        <label for="cn">CN:</label>
        <input type="text" id="cn" name="cn" required><br>
        <label for="jp">JP:</label>
        <input type="text" id="jp" name="jp" required><br>
        <label for="asd">ASD:</label>
        <input type="text" id="asd" name="asd" required><br>
        <label for="jp_lab">JP Lab:</label>
        <input type="text" id="jp_lab" name="jp_lab" required><br>
        <label for="dbms_lab">DBMS Lab:</label>
        <input type="text" id="dbms_lab" name="dbms_lab" required><br>
        <label for="ss2">SS2:</label>
        <input type="text" id="ss2" name="ss2" required><br>
        <input type="submit" value="Calculate SGPA">
    </form>

    <h1>CGPA Calculator</h1>
    <form action="/calculate_cgpa" method="post">
        <label for="sem1">Semester 1:</label>
        <input type="number" id="sem1" name="sem1" step="0.01" required><br>
        <label for="sem2">Semester 2:</label>
        <input type="number" id="sem2" name="sem2" step="0.01" required><br>
        <label for="sem3">Semester 3:</label>
        <input type="number" id="sem3" name="sem3" step="0.01" required><br>
        <label for="sem4">Semester 4:</label>
        <input type="number" id="sem4" name="sem4" step="0.01" required><br>
        <input type="submit" value="Calculate CGPA">
    </form>
</body>
</html>
'''

# Route for home page
@app.route('/')
def welcome():
    return render_template_string(html_template)

# Route for SGPA calculation
@app.route('/calculate_sgpa', methods=['POST'])
def calculate_sgpa():
    maths = default_grade(request.form['maths'].upper())
    ids = default_grade(request.form['ids'].upper())
    dbms = default_grade(request.form['dbms'].upper())
    cn = default_grade(request.form['cn'].upper())
    jp = default_grade(request.form['jp'].upper())
    asd = default_grade(request.form['asd'].upper())
    jp_lab = default_grade(request.form['jp_lab'].upper())
    dbms_lab = default_grade(request.form['dbms_lab'].upper())
    ss2 = default_grade(request.form['ss2'].upper())

    # SGPA Calculation
    gpa = (4 * maths) + (3 * ids) + (3 * dbms) + (3 * cn) + (3 * jp) + (4 * asd) + (2 * jp_lab) + (2 * dbms_lab) + (1 * ss2)
    sgpa = gpa / 25

    return f'SGPA: {sgpa:.2f}'

# Route for CGPA calculation
@app.route('/calculate_cgpa', methods=['POST'])
def calculate_cgpa():
    sem1 = float(request.form['sem1'])
    sem2 = float(request.form['sem2'])
    sem3 = float(request.form['sem3'])
    sem4 = float(request.form['sem4'])

    # CGPA Calculation
    cgpa = (sem1 + sem2 + sem3 + sem4) / 4

    return f'CGPA: {cgpa:.2f}'

if __name__ == '__main__':
    app.run(debug=True)
