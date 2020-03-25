# TinderBot
A Tinder Bot using Python and Selenium

The bot is able to open a Chrome window, log in using facebook, like and dislike people, and swipe automatically.

Instructions:
Chrome's webdriver (can be downloaded from https://chromedriver.chromium.org/downloads)
Change the variable webdriver_path in TinderBot.py to the path where you installed the webdriver
Edit the username and password variables in tinder_login.py and replace them with your Facebook login credentials, since the bot will use Facebook as a login method.

Notes: 
Because Selenium access the xpath of the web elements, and because certain xpaths in the program access the text of the elements, this bot will run better in the Spanish version of Tinder. However, the swiping functionality remains unaffected.
For better performance it is recommended to run the TinderBot.py file on a terminal in interactive mode (cd to the file´s directory and type python -i TinderBot.py)
Once you run the program in interactive mode, a new window will open. Wait for it to load and, once you see the Facebook login option, type bot.login() in the terminal.
Then the bot will log in and you'll see a bunch of popups. If you have the Spanish version of Tinder, you can just type bot.swipe() in the terminal.
Otherwise just get rid of the popups and once they´re gone, you can run bot.swipe() from the terminal and it'll start swiping. 

The bot swipes right with a probability of 80%, and left with a probability of 50%. Future versions shall be able to do a better job at classifying the pictures. 

Have fun!

""" THIS PROGRAM IS ONLY FOR DEMOSTRATION PURPOSES AND NOT TO BE USED AGAINST TINDER´S TERMS OF SERVICE """
