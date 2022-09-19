from flask import Flask,render_template
app = Flask(__name__)
@app.route('/play')
def boxplay1():
    return render_template('index.html',var1 = 3, var2 ="blue")
@app.route('/play/<var1>')
def boxplay2(var1):
    return render_template('index.html',var1 = var1, var2="blue")
@app.route('/play/<int:var1>/<string:var2>')
def boxplay3(var1,var2):
    return render_template('index.html', var1=var1,var2=var2)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
