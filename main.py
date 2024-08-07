from flask import Flask, render_template, request, jsonify

from db.create import createTables, createUser
from db.GetUsers import getAllusers, getSpecificUsers
from db.UserOpration import updateUserAccess

app= Flask(__name__)

@app.route('/createUser',methods = ['POST'])
def create_user():

    name =  request.form['name']
    password= request.form['password']
    email = request.form['email']
    address= request.form['address']
    phone = request.form['phone']
    pincode  = request.form['pincode']
    dbRes=createUser(name=name, Email=email, Address=address, Phone=phone,password=password,PinCode=pincode)
    if dbRes==True:  
        return jsonify({'success':200,"message":"Successfully created"})
    else:
       return jsonify({'success':400,"message":"unable to create User"}) 
        

@app.route('/getAllUsers', methods=['GET'])
def getAllUser():
    return getAllusers()

@app.route('/getSpecificUser', methods=['GET'])
def getSpecificUser():
    userID = request.form['userID']
    return getSpecificUsers(userId=str(userID))

@app.route('/updateUserAccess', methods=['PATCH'])
def updateUser_Access():
    userId= request.form['userID']
    approved= request.form['approved']
    blocked= request.form['blocked']
    updateUserAccess(id=userId, approved=approved, blocked=blocked)
    return "access updated successfully"


if __name__ == "__main__":
    createTables()
    app.run()
