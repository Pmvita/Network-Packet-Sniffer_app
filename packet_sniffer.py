import tkinter as tk
from tkinter import ttk
from scapy.all import sniff
import threading

class PacketSnifferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Packet Sniffer")

        self.tab_control = ttk.Notebook(root)
        
        self.sniffer_tab = ttk.Frame(self.tab_control)
        self.settings_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.sniffer_tab, text='Sniffer')
        self.tab_control.add(self.settings_tab, text='Settings')
        self.tab_control.pack(expand=1, fill='both')

        self.packet_list = tk.Listbox(self.sniffer_tab)
        self.packet_list.pack(expand=True, fill='both')

        self.start_button = tk.Button(self.sniffer_tab, text="Start Sniffing", command=self.start_sniffing)
        self.start_button.pack()

        self.stop_button = tk.Button(self.sniffer_tab, text="Stop Sniffing", command=self.stop_sniffing)
        self.stop_button.pack()

        self.settings_label = tk.Label(self.settings_tab, text="Settings will go here.")
        self.settings_label.pack()

        self.sniffing = False

    def start_sniffing(self):
        self.sniffing = True
        self.packet_list.delete(0, tk.END)
        # Start sniffing in a separate thread
        threading.Thread(target=self.sniff_packets).start()

    def stop_sniffing(self):
        self.sniffing = False

    def sniff_packets(self):
        sniff(prn=self.process_packet, store=0)

    def process_packet(self, packet):
        if self.sniffing:
            self.packet_list.insert(tk.END, str(packet))

if __name__ == "__main__":
    root = tk.Tk()
    app = PacketSnifferApp(root)
    root.mainloop()
