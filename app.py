from flask import Flask,render_template,url_for, request, redirect

app=Flask(__name__,static_url_path='/static')
@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')
if __name__ == "__main__":
    #app.jinja_env.auto_reload=True
    app.run(host="0.0.0.0",debug=True)