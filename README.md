# Plangrid - Simple API in Python (2.7)


Overview
========

Plangrid is an example API which demonstrates building a simple REST API with python flask . This api is backed by a static json database.


Requirements
===========

* Python 2.7
* Works on Linux, Windows, Mac OSX and (quite possibly) BSD.

Run
=======
<code>
python flaskapi.py
</code>

APIs and Documentation
==============================
This service got single endpoint at http://127.0.0.1:5001/.  Depending on the Accept header input this api returns different "messages"

Test 
==============================
<code>
curl -i -H "Accept: application/json" http://localhost:5001/
</code>
or
<code>
curl -i http://localhost:5001/
</code>

UnitTests 
==============================
<code>
python flasktest.py
</code>
