from typing import List, Dict

from flask import Flask, render_template,jsonify

app = Flask(__name__, template_folder='home1', static_folder='pic')

## jobs
JOBS: list[dict[str, str | int] | dict[str, str | int] | dict[str, str | int] | dict[str, str | int]] = [
    {
        'id': 1,
        'titel': 'App Developer',
        'salary': 1000000,
        'location': 'Bangalore, India'
    },
    {
        'id': 2,
        'titel': 'Web Developer',
        'salary': 1200000,
        'location': 'Bangalore, India'
    },
    {
        'id': 3,
        'titel': 'Data Scientist',
        'salary': 1700000,
        'location': 'Delhi, India'
    },
    {
        'id': 4,
        'titel': 'ML Eng',
        'salary': 3000000,
        'location': 'Bangalore, India'
    }
]
@app.route('/jobs')
def jobs_json():
    return jsonify(JOBS)

@app.route("/")
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('home/home.css', person=name)
def hello_world():
    return render_template('home.html',
                           jobs = JOBS)


## debug = true means if we change the code then the local server is also updated
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
