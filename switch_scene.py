#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import keyboard
import logging
logging.basicConfig(level=logging.INFO)

sys.path.append('../')
from obswebsocket import obsws, requests  # noqa: E402


host = "192.168.1.153"
port = 4444
password = ""

ws = obsws(host, port, password)
ws.connect()

while True:
  # Verifica se il tasto G è premuto
  if keyboard.is_pressed("g"):
    # Cambia alla scena "mappa"
    ws.call(requests.SetCurrentScene('mappa'))
    print("Cambiata scena in: mappa")
    while True:
          if not keyboard.is_pressed("g"):
            # Cambia alla scena "principale"
            time.sleep(1)
            ws.call(requests.SetCurrentScene('principale'))
            time.sleep(1)
            print("Cambiata scena in: principale")
            break
  if keyboard.is_pressed("esc"):
    # Cambia alla scena "mappa"
    ws.call(requests.SetCurrentScene('mappa'))
    print("Cambiata scena in: mappa")
    while True:
          if keyboard.is_pressed("esc"):
            # Cambia alla scena "principale"
            time.sleep(1)
            ws.call(requests.SetCurrentScene('principale'))
            print("Cambiata scena in: principale")
            break
  # Aspetta mezzo secondo prima di verificare di nuovo lo stato del tasto G

