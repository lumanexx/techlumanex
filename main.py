from flask import Flask,  render_template, jsonify

app = Flask(__name__)


JOBS = [
  {
  
    'id': 1,
    'title': 'Frontend Engineer',
    'location': 'Lagos, Nigeria',
    'salary': '#500.000'
  },
  {
    'id': 2,
    'title': 'Data Engineer',
    'location': 'Remote',
    'salary': '#500.000'
  },
  {
    'id': 3,
    'title': 'UI/UX Designer',
    'location':'Abuja, Nigeria',
    'salary': '#500.000'
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'Portharcourt, Nigeria',
    'salary': '#500.000'
  }
]
@app.route("/")
def home():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
if __name__ == "__main__":
  app.run(host= '0.0.0.0' , debug=True)
     