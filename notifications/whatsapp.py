import pywhatkit as kit
  
def send_message(msg):
    try:
        kit.sendwhatmsg_instantly(
            phone_no="+23057871057",
            message=msg,
            wait_time=15,
            tab_close=True,
            close_time=10
        )
        print("Message sent successfully!")
    except Exception as e:
        print(e)
        return