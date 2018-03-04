from flask import Flask, request,jsonify
import db

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def root():
    if request.method == 'GET':
        if request.headers['Accept'] == 'application/json':
            return jsonify(db.get_msg())
        else: 
            #return jsonify(db.get_msg())
            return "<p> Hello, World </p>"

if __name__ == "__main__":
    app.run(port=5001, debug=True)
