from flask import Flask, render_template


app= Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row = 8, col = 8, color_one = 'black', color_two = 'red')

@app.route('/<int:row>/')
def level2(row,):
    return render_template('index.html',col = 8, row = row,color_one = 'green', color_two = 'black')

@app.route('/<int:row>/<int:col>')
def level3(row,col):
    return render_template ('index.html',col = col, row = row, color_one = 'green', color_two = 'purple')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def row_col_two(x,y,one,two):
    return render_template("index.html",row=x,col=y,color_one=one,color_two=two)
if __name__=="__main__":
    app.run(debug=True)