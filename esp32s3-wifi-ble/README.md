# ESP32-S3 WiFi + BLE 双模项目
基于 MicroPython 的 ESP32-S3 模块化项目，同时支持 WiFi 联网和 BLE 蓝牙串口通信。

## 硬件平台
- ESP32-S3 (双核处理器 + PSRAM)
- MicroPython v1.28+

## 项目结构
- `main.py`：主程序，调度WiFi和蓝牙模块
- `ble_module.py`：BLE蓝牙独立模块（稳定无报错）
- `wifi_module.py`：WiFi STA模式连接模块

## 核心功能
1. **BLE蓝牙串口**：手机APP双向通信，动态句柄，无空数据/报错
2. **WiFi联网**：STA模式自动连接路由器，获取IP地址
3. **模块化设计**：代码解耦，易维护、易复用、易扩展

## 使用方法
1. 修改 `main.py` 中的 WiFi 名称和密码
2. 将 3 个文件上传至 ESP32-S3 根目录
3. 重启设备，自动运行双功能

## 蓝牙通信说明
- 服务UUID：`0000ffe0-0000-1000-8000-00805f9b34fb`
- 特征值UUID：`0000ffe1-0000-1000-8000-00805f9b34fb`
- 支持：UTF-8 文本收发