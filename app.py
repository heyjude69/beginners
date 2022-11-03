from flask import Flask, redirect, url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/result/<float:score>')
def result(score):    
    cgpa= "{:.3f}".format(score)
    
    return render_template('result.html',cgpa=cgpa)
        
@app.route('/check/')
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        cn=request.form.get('CN')
        ebs=request.form.get('EBS')        
        dme=request.form.get('DME')        
        eds=request.form.get('EDS')        
        fla=request.form.get('FLA')        
        efs=request.form.get('EFS')        
        cps2=request.form.get('CPS2')    
        msit=request.form.get('MSIT')    
    convertedGrade=[int(cn),int(ebs),int(dme),int(eds),int(fla),int(efs),int(cps2),int(msit)]
    sgpa=(convertedGrade[0]*4+convertedGrade[1]*3+convertedGrade[2] *4+convertedGrade[3]*3 +convertedGrade[4] *3+convertedGrade[5] *3 +convertedGrade[6] *1 +convertedGrade[7]*1)/22   
    return redirect(url_for('result',score=sgpa))
   
if __name__=='__main__':
    app.run(debug=True)
