tornado WebSocket example
=========================

Installation
-------------
1. `git clone https://github.com/hiroakis/tornado-websocket-example.git`

2. `cd tornado-websocket-example`

3. Edit index.html

`var ws = new WebSocket('ws://localhost:8888/ws'` <- change to your url/localhost

4. `pip install -r requirements.txt`

5. `python app.py`

6. http://YourSite:8888/
(This is my demo page -> http://localhost:8888/)

7. Send a REST call:

REST API examples
------------------
Set the "id 1" value to 100 :
- `curl "http://localhost:8888/api?id=1&value=100"`

Set the "id 1" value to 300( The row No 1 will change to yellow ) :
- `curl "http://localhost:8888/api?id=1&value=300"`

Set The "id 1" value to 600( The row No 1 will change to red ):
- `curl "http://localhost:8888/api?id=1&value=600"`

- value 201 - 500 : change to yellow
- value 501 - : change to red

