Plangrid - Simple API in Python (2.7)

Overview:
Plangrid is an example API which demonstrates building a simple REST API with python flask . This api is backed by a static json database.
This takes simple POST and GET with one endpoint. 

Requirements
Python 2.7
Works on Linux, Windows, Mac OSX and (quite possibly) BSD.

Start Python App:
   python ./app.py 

APIs and Documentation
 This service got single endpoint at http://127.0.0.1:5001/
 Depending on the Accept header input this api returns different "messages".

Test :
curl -i -H "Accept: application/json" http://localhost:5001/
or
curl -i http://localhost:5001/

UnitTest:
python flasktest.py




