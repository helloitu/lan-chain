'''
This is the main file of the application.
'''
import tkinter as tk
from network_interface import NetworkInterface
from packet_receiver import PacketReceiver
class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Network Traffic Application")
        self.network_interface = NetworkInterface()
        self.packet_receiver = PacketReceiver()
        # Create GUI elements
        self.label = tk.Label(self, text="Network Traffic Application")
        self.label.pack()
        self.start_button = tk.Button(self, text="Start", command=self.start)
        self.start_button.pack()
        self.stop_button = tk.Button(self, text="Stop", command=self.stop)
        self.stop_button.pack()
    def start(self):
        self.network_interface.attach_to_interface()
        self.network_interface.start_listening()
        self.packet_receiver.start_receiving()
    def stop(self):
        self.network_interface.stop_listening()
        self.packet_receiver.stop_receiving()
if __name__ == "__main__":
    app = Application()
    app.mainloop()