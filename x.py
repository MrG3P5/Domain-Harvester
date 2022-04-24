from multiprocessing.dummy import Pool as ThreadPool
import requests as Req
import os
import socket
import pyfiglet

try:
    open("result.txt", "a")
except:
    pass

def __banner__():
    os.system("cls||clear")
    my_banner = pyfiglet.figlet_format("X-Harvester", font="slant", justify="center")
    print(my_banner)


def DomainHarvester(domain):
    try:
        getip = socket.gethostbyname(domain)
        req = Req.get("https://sonar.omnisint.io/reverse/" + getip, timeout=3)
        print(f"[*] {domain} -> {getip} : {len(req.json())} Domain")
        for i in req.json():
            open("result.txt", "a").write(i + "\n")
    except:
        pass


if __name__=="__main__":
    __banner__()
    input_list = open(input("[?] Domain List : ")).read().replace("https://", "").replace("http://", "").splitlines()
    Thread = input("[*] Thread : ")
    pool = ThreadPool(int(Thread))
    pool.map(DomainHarvester, input_list)
    pool.close()
    pool.join()
