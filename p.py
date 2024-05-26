from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('projects.html')

@app.route("/p1")
def disp():
    return render_template('projects/p1.html',display = 'block')


@app.route("/p1.start", methods=['GET','POST'])
def projects():
    if request.method =="POST":
        msg = request.form['choice']
        return render_template('projects/p1.html',display = 'none',msg= msg)
    else:
        return TypeError("POST method is not working!!",msg= msg)


if __name__ == '__main__':
    app.run(debug=True)
