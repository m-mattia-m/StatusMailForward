from importfile import *
from userData import *

class Main():
    
      def __init__(self):
            self.openMail()



      def sendMailTo(self, mailTxt, regarding):
            host = UserData.host
            port = UserData.port
            smtp_user = UserData.user
            smtp_pass = UserData.password
            
            from_email = UserData.from_email
            to_email = UserData.to_email
            
            msg = EmailMessage()
            msg["FROM"] = from_email
            msg["To"] = to_email
            msg["Subject"] = "NAS Status-Report"

            regarding += "\n\n"

            body = mailTxt.decode("utf-8")

            msg.set_content(regarding + body)
            # msg.set_content(mailTxt)
            # msg.set_content(regarding)
            
            text = msg.as_string()
            
            smtp = smtplib.SMTP(host, port)
            smtp.login(smtp_user, smtp_pass)
            
            smtp.sendmail(from_email, to_email, text)
            smtp.close()

            print("-->: Mail gesendet")


      def openMail(self):

            # Connection settings
            HOST = UserData.host
            USERNAME = UserData.user
            PASSWORD = UserData.password

            m = imaplib.IMAP4_SSL(HOST, 993)
            m.login(USERNAME, PASSWORD)
            m.select('INBOX')

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

            print("###########################################################")
            print(regarding)
            print("###########################################################")
            print(txt)
            print("###########################################################")
            
            print("-->: Betreff und Text ausgelesen")

            self.compareText(txt, regarding)
               
            m.close()
            m.logout()



      def compareText(self, mailTxt, regarding):
            self.mailTxt = mailTxt
            self.regarding = regarding
            bspRegarding = ""

            if regarding.endswith("] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"):
                  
                  tempLetter1 = regarding[11:14]

                  if len(regarding) == 82:
                        tempLetter2 = regarding[27:42]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 81:
                        tempLetter2 = regarding[27:41]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 80:
                        tempLetter2 = regarding[27:40]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 79:
                        tempLetter2 = regarding[27:39]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 78:
                        tempLetter2 = regarding[27:38]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 77:
                        tempLetter2 = regarding[27:37]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 76:
                        tempLetter2 = regarding[27:36]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 75:
                        tempLetter2 = regarding[27:35]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"
                  elif len(regarding) == 74:
                        tempLetter2 = regarding[27:34]
                        bspRegarding = "[192.168.1." + tempLetter1 + "]IP-ADRESSE [" + tempLetter2 + "] WURDE VON SSH AUF MATTIA-NAS BLOCKIERT"

            if regarding != bspRegarding:
                  print("-->: Mail verglichen")
                  self.sendMailTo(mailTxt, regarding)
            elif regarding == bspRegarding:
                  print("-->: Mail nicht verglichen")
            
      





if __name__ == '__main__':
      Main()