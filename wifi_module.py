# wifi_module.py - ESP32-S3 WiFi独立模块
# 功能：STA模式连接WiFi，自动重连，获取IP
import network
import time

class WiFiClient:
    def __init__(self):
        self.wlan = network.WLAN(network.STA_IF)

    def connect(self, ssid, password, timeout=10):
        self.wlan.active(True)
        if self.wlan.isconnected():
            print("✅ WiFi 已连接")
            return True
            
        print(f"🔗 正在连接 WiFi: {ssid}")
        self.wlan.connect(ssid, password)
        start_time = time.time()
        
        while not self.wlan.isconnected() and time.time() - start_time < timeout:
            time.sleep(0.5)
            print(".", end="")
            
        if self.wlan.isconnected():
            print("\n✅ WiFi 连接成功！")
            print("📶 IP信息:", self.wlan.ifconfig())
            return True
        else:
            print("\n❌ WiFi 连接失败")
            return False

    def get_ip(self):
        return self.wlan.ifconfig()[0] if self.wlan.isconnected() else None