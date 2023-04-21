#!/usr/bin/python
#coding=utf-8

import socket
import nmap
import tkinter as tk
from tkinter import messagebox
//Hola en este proyecto estoy aprendiendo a escanear puertos//
//Estoy aprendiendo a usar librerias de python// 
# Función para escanear puertos
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

# Función para escanear servicios
def scan_services(ip, ports):
    nm = nmap.PortScanner()
    nm.scan(ip, ','.join(map(str, ports)), '-sS')
    services = []
    for port in nm.all_hosts():
        for proto in nm[host].all_protocols():
            lport = nm[host][proto].keys()
            for port in lport:
                service = {
                    'port': port,
                    'protocol': proto,
                    'name': nm[host][proto][port]['name'],
                    'state': nm[host][proto][port]['state']
                }
                services.append(service)
    return services

# Función para manejar el escaneo
def scan():
    ip = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())
    
    # Escaneo de puertos
    open_ports = scan_ports(ip, start_port, end_port)
    
    # Escaneo de servicios
    services = scan_services(ip, open_ports)
    
    # Mostrar resultados en la interfaz de usuario
    messagebox.showinfo("Resultado ya valistee", f"Puertos abiertos: {open_ports}\nServicios detectados: {services}")

# Crear la ventana de la interfaz de usuario
root = tk.Tk()
root.title("Scanner de Seguridad de Red")

# Crear campos de entrada de datos
label_ip = tk.Label(root, text="Dirección IP:")
label_ip.pack()
entry_ip = tk.Entry(root)
entry_ip.pack()

label_start_port = tk.Label(root, text="Puerto de inicio jijiji:")
label_start_port.pack()
entry_start_port = tk.Entry(root)
entry_start_port.pack()

label_end_port = tk.Label(root, text="Puerto de fin lero leroo:")
label_end_port.pack()
entry_end_port = tk.Entry(root)
entry_end_port.pack()

# Crear botón de escaneo
button_scan = tk.Button(root, text="Escanea, andale vato, sin miedo", command=scan)
button_scan.pack()

# Ejecutar la interfaz de usuario
root.mainloop()
