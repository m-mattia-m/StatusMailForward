from importfile import *
from userData import *



def read():
    ses = imaplib.IMAP4_SSL(UserData.host, UserData.port)
    ses.login(UserData.user, UserData.password)
    ses.select()
    data = ses.search(None, 'UNSEEN')[1]
    for num in data[0].split():
        data = ses.fetch(num, '(RFC822)')[1][0][1].decode('utf-8')
        message = email.message_from_string(data)

        print(message['To'])
        print(message['From'])
        print(message['Subject'])

        for i in message.get_payload():
            print(i)

    ses.close()
    ses.logout()


if __name__ == '__main__':
    read()