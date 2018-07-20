# Python3 code to demonstrate
# the random generation of string id's
 
import random
import string
 
# defining function for random
# string id with parameter
def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
 



def genIMEI():
    identifier = "%02d" % random.randint(1,9)
    me = ran_gen(6,'0123456789') 
    serial = ran_gen(6,'0123456789')
    check = random.randint(1,9)
    return f"{identifier}{me}{serial}{check}"

def genIMSI(mccList):
    mcc = random.choice(mccList)
    mnc = random.randint(50,99)
    msin = ran_gen(10,'0123456789')
    return f"{mcc}{mnc}{msin}"

acctNum = f"PAN-{ran_gen(1,'ABC')}{ran_gen(1,'789')}-{ran_gen(8, '1234567890')}"
IMEI = genIMEI()
IMSI = genIMSI([289,589,659,777,888,999])

print(f"{acctNum},{IMEI},{IMSI}")

