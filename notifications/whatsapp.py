import pywhatkit as kit
  
def send_message(msg_list):
    if msg_list:
        for msg in msg_list:
            msg = f"Date: {msg['date']} | Bank: {msg['bank_name']} | Value: {msg['value']}"
            try:
                kit.sendwhatmsg_instantly(
                    phone_no="+23057871057",
                    message=msg,
                    wait_time=10,
                    tab_close=True,
                    close_time=5
                )
                print("Message sent successfully!")
            except Exception as e:
                print(e)
                return
    else:
        print("No messages to send.")