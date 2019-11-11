from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/performance')
def perform():
    return(render_template('perform.html'))
@app.route('/wrong')
def wrong():
    cri1=cri2=cri3=False
    username=request.args.get(usname)
    print("This is ",username)
    return(render_template('wrong.html',cri1=cri1,cri2=cri2,cri3=cri3))
if __name__=='__main__':
    app.run(debug=True)


