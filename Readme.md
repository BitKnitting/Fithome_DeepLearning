Capture readings from the TP.

# Python
- set up venv
- install 

Soon after sending readings, the browser interface to Firebase will stop showing updates.  In order to delete readings...
Note: To delete readings when browser sets to read only...
see [this stackoverflow about blank json](https://stackoverflow.com/questions/38651204/firebase-read-only-non-realtime-mode-activated-to-improve-browser-performanc)

To get readings into file:
- go to the monitor's directory and open terminal.
`curl 'https://fithome-9ebbd.firebaseio.com/flower-09282019/readings.json?print=pretty' > fithome.json ` (here the monitor name was flower-09282019)


I stopped/ started.  So I had a fithome_old.json and fithome.json.  To merge these, I used the jq utility as discussed on [StackOverflow](https://stackoverflow.com/questions/19529688/how-to-merge-2-json-file-using-jq)