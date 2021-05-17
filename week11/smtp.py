import smtplib

try:
    input = open("SMTP_Account.txt")
    account,password,receivers = input.read().split(",")
    input.close()
    try:
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        try:
            server.login(account,password)
            msg = "thanthap suksanit 5930300232"
            server.sendmail(account,receivers,msg)
            print("Send mail Successfully")
        except:
            print("Incorrect account or password")

        finally:
            print("Quit Server")
            server.quit()
    except:
        print("Server not found")
except:
    print("File not found")
    
