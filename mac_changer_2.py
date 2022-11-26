import subprocess
import optparse
import re

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="interface degistirme ...")
    parse.add_option("-m","--mac",dest="mac",help="yeni mac adres ...")

    return parse.parse_args()

def mac(interface,mac):
    subprocess.call('ifconfig',interface,'down')
    subprocess.call(["ifconfig",interface,"hw","ether",mac])
    subprocess.call(["ifconfig",interface,"up"])

def kontrol(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    Ymac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",ifconfig)

    if Ymac:
        return Ymac.group(0)
    else:
        return None

(userInput,arguments) = giris()
mac(userInput.interface,userInput.mac)
Emac = kontrol(userInput.interface)

if Emac == userInput.mac:
    print("İşlem Başarılı")
else:
    print("İşlem Başarısız")