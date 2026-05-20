# ESP8266 巴法云TCP远程控制
基于 ESP8266 + 巴法云 TCP 协议实现的远程继电器控制项目，支持WiFi自动重连、TCP心跳保活、指令接收LED闪烁提醒

## 硬件适配
- 主控：ESP8266 (Generic ESP8266 Module / NodeMCU)
- 继电器控制引脚：GPIO5
- 板载状态LED：GPIO2（接收TCP指令自动闪烁一次）

## 核心功能
1. WiFi自动连接 + 断线自动重连机制
2. 巴法云TCP服务器稳定连接，定时心跳保活
3. 远程开关继电器控制
4. 指令接收可视化：板载LED闪烁提醒
5. 兼容2.4G频段WiFi，适配Generic ESP8266开发板

## 项目配置参数
### WiFi 配置
- WiFi名称：CMCC-xaNu
- WiFi密码：KuanRmde

### 巴法云TCP配置
- 私钥UID：c5006f65ec69fd1506b08d05436e9eb8
- 订阅主题：TRuQoFKqa002
- 服务器地址：tcp.bemfa.com
- 端口号：8344

## 使用教程
1. 安装Arduino IDE，并添加ESP8266开发板环境
2. 开发板选择：Generic ESP8266 Module
3. 直接编译代码并上传至ESP8266
4. 打开串口监视器（波特率9600）查看运行状态
5. 通过巴法云控制台发送指令控制设备

## 控制指令
- `msg=on` ：开启继电器
- `msg=off`：关闭继电器

## 注意事项
1. ESP8266仅支持**2.4G WiFi**，不支持5G WiFi
2. 路由器2.4G信道建议设置为1/6/11，提升兼容性
3. 保证设备供电稳定，避免供电不足导致WiFi连接失败
