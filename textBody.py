from importfile import *
from userData import *

def openMail():
            # Connection settings
            HOST = UserData.host
            USERNAME = UserData.user
            PASSWORD = UserData.password

            m = imaplib.IMAP4_SSL(HOST, 993)
            m.login(USERNAME, PASSWORD)
            m.select('INBOX')

            # result, data = m.uid('search', None, "UNSEEN") #UNSEEN
            # if result == 'OK':
            #     for num in data[0].split()[:5]:
            #         result, data = m.uid('fetch', num, '(RFC822)')
            #         if result == 'OK':
            #             email_message_raw = email.message_from_bytes(data[0][1])
            #             email_from = str(make_header(decode_header(email_message_raw['From'])))
            #             # von Edward Chapman -> https://stackoverflow.com/questions/7314942/python-imaplib-to-get-gmail-inbox-subjects-titles-and-sender-name
            #             subject = str(email.header.make_header(email.header.decode_header(email_message_raw['Subject'])))
            #             body = email_message_raw.get_payload(decode=True)


            result, data = m.uid('search', None, "UNSEEN") #UNSEEN
            for num in data[0].split()[:5]:
                result, data = m.uid('fetch', num, '(RFC822)')
                if result == 'OK':
                    email_message = email.message_from_bytes(data[0][1])
                    email_from = str(make_header(decode_header(email_message['From'])))
                    # von Edward Chapman -> https://stackoverflow.com/questions/7314942/python-imaplib-to-get-gmail-inbox-subjects-titles-and-sender-name
                    subject = str(email.header.make_header(email.header.decode_header(email_message['Subject'])))
                    b = email_message 

                    if b.is_multipart():
                        for part in b.walk():
                            ctype = part.get_content_type()
                            cdispo = str(part.get('Content-Disposition'))

                            if ctype == 'text/plain' and 'attachment' not in cdispo:
                                body = part.get_payload(decode=True)  # decode
                                break
                    else:
                        body = b.get_payload(decode=True)
            
            regarding = subject
            txt = body
            m.close()
            m.logout()

            print("###########################################################")
            print(regarding)
            print("###########################################################")
            print(txt)
            print("###########################################################")

if __name__ == '__main__':
    openMail()


    
