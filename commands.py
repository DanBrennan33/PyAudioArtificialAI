import subprocess
from get_answer import Scraper

# "Artificial" Artificial Intelligence to talk with us

class Commander:
    def __init__(self):
        self.confirm = ["yes", "affirmative", "si", "sure", "do it", "yeah", "confirm"]
        self.cancel = ["no", "negative", "don't", "cancel", "wait"]
        
    # Prompts to automate respond from program based on Static question
    # Also looks up answer on google via web scraper for some dynamic replies.  
        
    def discover(self, text):
        if "what" in text and "your name" in text:
            if "my" in text:
                self.respond("You haven't told me your name yet.")
            else:
                self.respond("My name is Linux. How are you?")
        else:
            scrape = Scraper("https://www.google.ca/search?q=" + text)
            answer = scrape.lookup()
            self.respond(answer)
        
        
        # Issue command to open application
        
        #if "launch" or "open" in text:
            #app = text.split(" ", 1)[-1]
            #self.respond("Opening " + app)
            #os.system("app")


    def respond(self, response):
        print(response)
        subprocess.call("say " + response, shell=True)
        



