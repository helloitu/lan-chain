
from netfilterqueue import NetfilterQueue
from scapy.all import *
import os
from ChatSimulator import ChatSimulator

killed = []
def block(who):
    if who not in killed:
        socket.gethostbyname(who)
        print(os.system(f"sudo iptables -I INPUT -s {who} -j DROP"))
        print(os.system(f"sudo iptables -I OUTPUT -d {who}  -j DROP"))
        killed.append(who)

def process_packet(packet):
    pkt = IP(packet.get_payload())
    if pkt.haslayer(TCP):
            if pkt[TCP].dport == 3030:
                if pkt.haslayer(Raw):
                    if 'lanchain' in pkt[Raw].load.decode('utf-8', 'ignore'):
                        print(pkt[Raw].load.decode('utf-8', 'ignore'))
                        if pkt[Raw].load.decode('utf-8', 'ignore').split('-')[2] == '1': block(pkt[IP].src)

    packet.set_payload(bytes(pkt))
    packet.accept()

if __name__ == "__main__":
    nfqueue = NetfilterQueue()
    nfqueue.bind(0, process_packet)
    traffic_inducer = ChatSimulator(int(os.getenv("LCHAIN_NOS")), os.getenv("LCHAIN_WHOAMI"))
    traffic_inducer.start_connections()
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()
        traffic_inducer.stop_connections()
