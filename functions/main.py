from flask import Flask, render_template, request, redirect, jsonify
import json
import os


# Function code

def now_soon_later(request):
    return render("now-soon-later.html", request)


def plain(request):
    return render("plain.html", request)


def with_strapline(request):
    return render("with-strapline.html", request)


def render(template, request):
    data = request.json or {}
    data.update(request.args)
    data.update(request.form)
    name = request.form.get('name')
    title = request.form.get('title')
    mobile = request.form.get('mobile')
    email = request.form.get('email')
    if name and title and mobile and email:
        return render_template(template, name=name, title=title, mobile=mobile, email=email)
    else:
        return jsonify("Please provide name, title, mobile and email values."), 403


# For running locally

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def r_redirect():
    print(request.json)
    return redirect("http://localhost:8000/static")


@app.route('/plain', methods=['GET', 'POST'])
def r_plain():
    return plain(request)


@app.route('/now-soon-later', methods=['GET', 'POST'])
def r_now_soon_later():
    return now_soon_later(request)


@app.route('/with-strapline', methods=['GET', 'POST'])
def r_with_strapline():
    return with_strapline(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
