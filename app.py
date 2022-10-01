from flask import Flask, redirect, url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<float:score>')
def result(score):    
    cgpa= "{:.2f}".format(score)
    
    return render_template('result.html',cgpa=cgpa)
        
@app.route('/check/')
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        sepm=request.form.get('SEPM')
        app=request.form.get('APP')        
        daa=request.form.get('DAA')        
        math=request.form.get('MATH')        
        se=request.form.get('SE')        
        os=request.form.get('OS')        
        cc=request.form.get('CC')    
        cps1=request.form.get('CPS1')    
    convertedGrade=[int(sepm),int(app),int(daa),int(math),int(se),int(os),int(cc),int(cps1)]
    sgpa=(convertedGrade[0]*4+convertedGrade[1]*4+convertedGrade[2] *4+convertedGrade[3]*4 +convertedGrade[4] *2 +convertedGrade[5] *4 +convertedGrade[6] *3 +convertedGrade[7]*1)/26   
    return redirect(url_for('result',score=sgpa))
    # return convertedGrade
    
if __name__=='__main__':
    app.run(debug=True)