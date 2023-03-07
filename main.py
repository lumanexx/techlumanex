from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "ELUU P 78, OBI NWANNEM 79"
  
if __name__ == "__main__":
  app.run(host= '0.0.0.0' , debug=True)
     