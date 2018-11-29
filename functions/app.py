from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    """Helps local testing"""
    return redirect("http://localhost:8000", code=302)


@app.route('/now-soon-later', methods=['POST'])
def now_soon_later():
    return render("now-soon-later.html")


@app.route('/plain', methods=['POST'])
def plain():
    return render("plain.html")


@app.route('/with-strapline', methods=['POST'])
def with_strapline():
    return render("with-strapline.html")


def render(template):
    name = request.form.get('name') or ""
    title = request.form.get('title') or ""
    mobile = request.form.get('mobile') or ""
    email = request.form.get('email') or ""
    return render_template(template, name=name, title=title, mobile=mobile, email=email)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
