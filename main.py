# main.py - ESP32-S3 主程序
# 功能：同时运行 WiFi + BLE 双模功能
import time
from ble_module import BLEServer
from wifi_module import WiFiClient

# ==================== 配置区 ====================
WIFI_SSID = "SOES办公区-2G"
WIFI_PWD = "SOESGZEL"
BLE_NAME = "ESP32-S3-Pro"
# ================================================

# 初始化蓝牙
ble = BLEServer(BLE_NAME)

# 蓝牙数据接收回调
def on_ble_receive(msg):
    print(f"📩 蓝牙收到：{msg}")
    ble.send(f"ESP32已收到：{msg}")

ble.set_callback(on_ble_receive)
print("✅ 蓝牙启动完成")

# 初始化并连接WiFi
wifi = WiFiClient()
wifi.connect(WIFI_SSID, WIFI_PWD)

# 主程序运行日志
print("="*50)
print("🎉 ESP32-S3 双功能运行中：WiFi + BLE")
print("="*50)

# 主循环
while True:
    time.sleep(1)