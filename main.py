from netfilterqueue import NetfilterQueue
from scapy.all import IP, TCP, Ether, Raw
import subprocess
import struct

def process_packet(packet):
    pkt = IP(packet.get_payload())
    
    if pkt.haslayer(TCP):
        # Modifique o conteúdo do payload para adicionar dados personalizados.
        custom_header = b"payloadcustomizado"
        custom_packet = IP(src=pkt[IP].src, dst=pkt[IP].dst) / TCP(sport=pkt[TCP].sport, dport=pkt[TCP].dport) / custom_header / pkt[TCP].payload
        pkt[IP] = custom_packet[IP]
        pkt[TCP] = custom_packet[TCP]
        del pkt[IP].chksum
        del pkt[TCP].chksum
        
        # Enviar o pacote modificado de volta para a rede.
        packet.set_payload(bytes(pkt))
    
    packet.accept()

if __name__ == "__main__":
    subprocess.run("/sbin/iptables -A INPUT -j NFQUEUE --queue-num 0")
    subprocess.run("/sbin/iptables -A OUTPUT -j NFQUEUE --queue-num 0")
    nfqueue = NetfilterQueue()
    nfqueue.bind(0, process_packet)  # 0 é o número da fila
    try:
        nfqueue.run()
    except KeyboardInterrupt:
        nfqueue.unbind()
