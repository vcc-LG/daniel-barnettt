#About
Yet another twitter bot to randomly tweet out messages taken from my friend's twitter profile. 

#Installation
```python
pip install -r requirements.txt
```
Fill in your twitter app's credentials in a file called `credentials.py` in the root directory.

#Scheduling
I've used redis to schedule the tweets. Once you've got redis running, in two terminals run:
```python
python worker.py
```
and
```python
python clock.py
```