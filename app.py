from flask import Flask, render_template
# set the project root directory as the static folder, you can set others.
app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug="True")
