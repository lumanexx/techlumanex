from flask import Flask,  render_templates

app = Flask(__name__)

@app.route("/")
def  hello_world():
  return render_templates('home.html')
  
if __name__ == "__main__":
  app.run(host= '0.0.0.0' , debug=True)
     