from flask import Flask,request,jsonify
import sqlite_connection as sq

app=Flask(__name__)



@app.route('/color', methods=['GET','POST'])
def index():
    if request.method=='GET':
        color_list=sq.get()
        if color_list!=None:
            response=jsonify(color_list)
            response.headers.add('Access-Control-Allow-Origin', '*')
            return response
        
        else: 
            return "Something went wrong",404
    
    elif request.method=='POST':
        sq.post(request.form['color'],request.form['value'])
        return jsonify(sq.get())
        

@app.route('/color/<int:id>', methods=['GET','PUT','DELETE'])
def color(id):
    if request.method=='GET':
        color=sq.get_one(id)
        if color !=None:
             response= jsonify(color)
             response.headers.add('Access-Control-Allow-Origin', '*')
             return response
        else: 
            return "Something went wrong",404
        
    
    elif request.method=='PUT':
        sq.put(id,request.form['color'],request.form['value'])
        return jsonify(sq.get_one(id))
                
    elif request.method=='DELETE':
        sq.delete(id)
        return jsonify(sq.get()),200
        
                


if __name__=='__main__':
    app.run(debug=True)