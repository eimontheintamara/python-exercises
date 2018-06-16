from flask import Flask,render_template
app=Flask(__name__,template_folder='template')
@app.route('/')
def hello():
    greeting="Hello** Ei Mon Theint**Warmly welcome**"
    return render_template("index.html",greeting=greeting)
if __name__=="__main__":
    app.run()
