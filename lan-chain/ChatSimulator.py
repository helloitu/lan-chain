import socket,threading,time,traceback,os
from scapy.all import *


class ChatSimulator:
    def __init__(self, nos, whoami):
        self.nos = nos
        self.whoami = whoami
        self.stop_event = threading.Event()

    def checa_saude_no(self):
        #Valida saude do nó, 1 infectado, 0 saudavel
        return 1 if os.path.isfile('/tmp/LC_FLAG.txt') else 0
    
    def send_message(self, host):
        nao_responde = []
        while not self.stop_event.is_set():
            status = self.checa_saude_no()
            try:
                pkt = IP(dst=socket.gethostbyname(host)) / TCP(dport=3030) / f"{self.whoami}-{status}".encode('utf-8')
                send(pkt)
                pkt.show()
                time.sleep(5)
            except ConnectionRefusedError:
                print(f"[i] {host} negada.")
                time.sleep(3)
            except TimeoutError:
                print(f"Timeout [{host}]")
            except Exception as e:
                print(f"[{host}] - impossivel conectar")
                break

    def start_connections(self):
        for i in range(1, self.nos+1):
            host = f"lanchain-{i}"
            if host == self.whoami: continue
            thread = threading.Thread(target=self.send_message, args=(host,))
            thread.daemon = True
            thread.start()

    def stop_connections(self):
        self.stop_event.set()