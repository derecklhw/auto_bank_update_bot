import pywhatkit as kit
  
def send_message(msg_list, phone_number):
    if msg_list:
        for msg in msg_list:
            msg = f"Bank: {msg['url']} | Date: {msg['date']} | Currency: {msg['currency']} | Value: {msg['value']}"
            try:
                kit.sendwhatmsg_instantly(
                    phone_no=phone_number,
                    message=msg,
                    wait_time=10,
                    tab_close=True,
                    close_time=1
                )
                print("Message sent successfully!")
            except Exception as e:
                print(e)
                return
    else:
        print("No messages to send.")