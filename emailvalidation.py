import re
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
            return True
    return False

if isValidEmail("my.emailgmail.com") == True :
        print "This is a valid email address"
else:
        print "This is not a valid email address"
