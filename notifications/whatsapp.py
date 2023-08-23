import pywhatkit as kit
  
def send_message(msg_list, phone_number):
    if msg_list:
        concantenate_msg = ""
        for msg in msg_list:
            concantenate_msg += f"Date: {msg['date']} | Bank: {msg['url']} | Country: {msg['country']} | Value: {msg['value']}\n\n"
        try:
            kit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=concantenate_msg,
                wait_time=15,
                tab_close=True,
                close_time=1
            )
            print("All messages sent successfully!")
        except Exception as e:
            print(e)
            return
    else:
        print("No messages to send.")