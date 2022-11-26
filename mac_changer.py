import subprocess
import optparse

parse = optparse.OptionParser()
parse.add_option("-i","--interface",dest="interface",help="interface değiştirme...")
parse.add_option("-m","--mac",dest="mac_address",help="yeni mac adresi...")

(girisler,argumanlar) = parse.parse_args()
inter = girisler.interface
mac = girisler.mac_address


subprocess.call('ifconfig',inter,'down')
subprocess.call(["ifconfig",inter,"hw","ether",mac])
subprocess.call(["ifconfig",inter,"up"])
print("İşlem Başarılı")