from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    socketAddress = (mailserver, port)
    clientSocket.connect((socketAddress))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    # print(recv)
    if recv[:3] != '220':
        recv = '220 reply not received from server.'
        # print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    # print(recv1)
    if recv1[:3] != '250':
        recv1 = '250 reply not received from server'
        # print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = 'MAIL FROM: <testemail@mail.com> \r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024)
    # print(recv2)
    if recv2[:3] != '250':
        recv2 = '250 reply not received from server'
        # print recv2
    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    emailTo = 'RCPT TO: <mordecaifan1@gmail.com> \r\n'
    clientSocket.send(emailTo.encode())
    recv3 = clientSocket.recv(1024)
    # print (recv3)
    if recv3[:3] != '250':
        recv3 = '250 reply not received from server'
        # print recv3
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    msgData = 'DATA\r\n'
    clientSocket.send(msgData.encode())
    recv4 = clientSocket.recv(1024)
    # print recv4
    # Fill in end

    # Send message data.
    # Fill in start
    clientSocket.send('\r\n'.encode())
    clientSocket.send('important data here\r\n'.encode())
    # Fill in end

    # Message ends with a single period.
    # Fill in start
    period_end = '.\r\n'
    clientSocket.send(period_end.encode())
    recv5 = clientSocket.recv(1024)
    # print recv5
    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    quitCommand = 'QUIT\r\n'
    clientSocket.send(quitCommand.encode())
    recv6 = clientSocket.recv(1024)
    # print recv6
    clientSocket.close()
    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
