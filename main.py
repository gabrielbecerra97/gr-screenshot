import sys
import business/screenshoots

class Main:
    def __init__(self):
        if len(sys.argv) < 2:
            print('No arguments given')
        else:
            ScreenshootManager.wholeScreen()
        
main = Main()