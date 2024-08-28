from flask import Flask 
from flask import render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Angelkay'}
    posts = [
            {
                'author': {'username': 'Angel'},
                'body': 'Beautiful Day in Lagos!'
                },
                {
                    'author': {'username': 'Kay'},
                    'body': 'Another Sunny Day'
                }
            ]
    return  render_template('index.html', title='Home', user=user, posts=posts)

if __name__ == "__main__":
    app.run(debug=True, port=8001)
