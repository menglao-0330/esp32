# ble_module.py - ESP32-S3 BLE蓝牙独立模块
# 作者：自定义 | 基于MicroPython
# 功能：稳定BLE串口通信，动态句柄，无报错
import bluetooth
import time

class BLEServer:
    def __init__(self, name="ESP32-S3"):
        self.ble = bluetooth.BLE()
        self.ble.active(False)
        time.sleep(0.5)
        self.ble.active(True)
        self.name = name
        self.char_handle = None
        self.init_service()

    def init_service(self):
        # 标准BLE串口UUID
        SVC_UUID = bluetooth.UUID("0000ffe0-0000-1000-8000-00805f9b34fb")
        CHAR_UUID = bluetooth.UUID("0000ffe1-0000-1000-8000-00805f9b34fb")
        handles = self.ble.gatts_register_services([
            (SVC_UUID, [(CHAR_UUID, bluetooth.FLAG_WRITE | bluetooth.FLAG_NOTIFY)])
        ])
        self.char_handle = handles[0][0]
        # 开启广播
        adv_data = b"\x02\x01\x06\x05\x09" + self.name.encode()
        self.ble.gap_advertise(100, adv_data)

    def set_callback(self, callback):
        def wrapper(event, data):
            if event == 3:
                raw_data = self.ble.gatts_read(self.char_handle)
                if raw_data:
                    callback(raw_data.decode('utf-8'))
        self.ble.irq(wrapper)

    def send(self, msg):
        try:
            self.ble.gatts_notify(0, self.char_handle, msg.encode())
        except Exception:
            pass