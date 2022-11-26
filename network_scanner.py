import scapy.all as scp
import optparse

def giris():
    parse = optparse.OptionParser()
    parse.add_option("-i","--ipadres",dest="ip_adresi",help="Hedef ip giriniz")

    (user_giris,arguments)= parse.parse_args()

    if not user_giris.ip_adresi:
        print("Hedef IP Girmediniz...")

    return user_giris.ip_adresi

def tarayici(ip):
    istek_paket = scp.ARP(pdst=ip)
    #scp.ls(scp.ARP())
    yayin_paket = scp.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scp.ls(scp.Ether())
    paket = yayin_paket / istek_paket
    (asilpaket,gecersizpaket) = scp.srp(paket,timeout=1)
    asilpaket.summary()

ipadresim = giris()
tarayici(ipadresim)
