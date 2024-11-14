from flask import Flask, render_template,jsonify

app=Flask(__name__)

Events=[
  {
    'id':1,
    'Eventname':'Drama',
    'Date':'12/12/2024',
    'time':'10am-2pm'
  },
  {
    'id':2,
    'Eventname':'Music',
    'Date':'12/12/2024',
    'time':'10am-2pm'
  },
  {
    'id':3,
    'Eventname':'Dance',
    'Date':'12/12/2024',
    'time':'10am-2pm'
  }
]

@app.route("/")
def hello_world():
  return render_template('home.html',event=Events)

@app.route('/api/Events')
def list_Events():
  return jsonify(Events)

if __name__ =='__main__':
  app.run(host='0.0.0.0',debug=True)
  