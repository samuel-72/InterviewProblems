import sys

def checkIP(IPAddress):
    IP = IPAddress.split('.')

    if (len(IP) != 4):
        print "Invalid IP Address"
        return False
        
    else:
        for octet in IP:
            if (int(octet) < 0 or int(octet) > 255):
                print "Invalid IP Address"
                return False

    print "IP Address is valid"
    return True


print "Enter the IP Address within quotes (Ex : '127.0.0.0' or \"127.0.0.0\"): "

checkIP(str(input()))