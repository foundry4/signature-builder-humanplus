from flask import Flask, render_template, request, redirect


# Function code

def now_soon_later(request):
    return render("now-soon-later.html", request)


def plain(request):
    return render("plain.html", request)


def with_strapline(request):
    return render("with-strapline.html", request)


def render(template, request):
    name = request.form.get('name') or ""
    title = request.form.get('title') or ""
    mobile = request.form.get('mobile') or ""
    email = request.form.get('email') or ""
    return render_template(template, name=name, title=title, mobile=mobile, email=email)


# For running locally

app = Flask(__name__)


@app.route('/plain', methods=['POST'])
def r_plain(request):
    return plain(request)


@app.route('/now-soon-later', methods=['POST'])
def r_now_soon_later(request):
    return now_soon_later(request)


@app.route('/with-strapline', methods=['POST'])
def r_with_strapline():
    with_strapline(request)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
