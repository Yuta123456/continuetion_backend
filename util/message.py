import random
def get_fruits():
    fruits = ["๐ฅ", "๐", "๐", "๐", "๐", "๐","๐","๐ฅญ","๐", 
              "๐", "๐", "๐", "๐", "๐"]
    return random.choice(fruits)
def get_no_reply_message():
    no_reply_message =  "ใใฎใกใใปใผใธใฏๅๅฟใงใใชใใงใใ๐ฐ"
    no_reply_message += "\nๅๅฟใงใใใกใใปใผใธไธ่ฆง"
    no_reply_message += "\nShow: ็ด่ฟใฎ็ถ็ถใใผใฟใ่กจ็คบใใพใ"
    no_reply_message += "\nRecord: ่จ้ฒใๅใใใใฎใกใใปใผใธใ้ใใพใ"
    no_reply_message += "\nFruits: ใฉใณใใ ใชใใซใผใใ้ใใพใ"
    no_reply_message += "\nset:็ถ็ถๅๅฎน: ็ถ็ถๅๅฎนใใปใใใใพใ"
    no_reply_message += "\nstop: ๆฏๆฅ่ใใฎใๆญขใใพใ"
    no_reply_message += "\nrestart: ๆฏๆฅ่ใใฎใๅ้ใใพใ"
    return no_reply_message

def get_set_complete_message(contents):
    return contents + "ใง็ถ็ถๅๅฎนใใปใใใใพใใใ"

def get_stop_send_message():
    message = "ๆฏๆฅ็ถ็ถใใใใฉใใ่ใใฎใ่พใใพใ๐ฅฒ"
    return message


def get_restart_send_message():
    message = "ๆฏๆฅ็ถ็ถใใใใฉใใ่ใใพใ๏ผ๐ฅฐ"
    return message