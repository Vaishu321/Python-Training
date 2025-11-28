class Notification:
    def send(self,message):
        print("Sending message:",message)

class EmailNotification(Notification):
    def send(self,message):
        print("Sending Email to user:",message)

class SMSNotification(Notification):
    def send(self,message):
        print("Sending SMS to user:",message)

class PushNotification(Notification):
    def send(self,message):
        print("Sending Push to user:",message)

#Usage
n1=EmailNotification()
n1.send("Your order is confirmed")
n2=SMSNotification()
n2.send("Your OTP is 4589")
n3=PushNotification()
n3.send("You have a new message")
