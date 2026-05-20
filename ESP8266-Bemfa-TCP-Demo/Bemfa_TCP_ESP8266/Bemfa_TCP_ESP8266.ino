#include <ESP8266WiFi.h>

// 随便改改注释测试GitHub的。20260519 1502

// ===================== 【标准配置项】新项目仅改这里 =====================
const char* ssid     = "menglao";          // WiFi名称
const char* password = "ren050249";        // WiFi密码
const char* uid      = "c5006f65ec69fd1506b08d05436e9eb8"; // 巴法云UID
const char* topic    = "TRuQoFKqa002";     // 巴法云TCP主题
const char* host     = "tcp.bemfa.com";    // 官方TCP地址
const uint16_t port  = 8344;               // 官方TCP端口
// ======================================================================

WiFiClient client;
unsigned long lastPing = 0;
bool isSubscribed = false;

void setup() {
  Serial.begin(9600);  // 标准波特率，解决串口乱码
  pinMode(0, OUTPUT);
  digitalWrite(0, HIGH);

  // WiFi连接
  Serial.print("WiFi连接中...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi connected ✅");
}

void loop() {
  // 断线重连 + 自动订阅
  if (!client.connected()) {
    Serial.println("重新连接TCP服务器...");
    if (client.connect(host, port)) {
      Serial.println("TCP连接成功 ✅");
      String subCmd = "cmd=1&uid=" + String(uid) + "&topic=" + topic + "\r\n";
      client.print(subCmd);
      Serial.print("订阅指令：");
      Serial.println(subCmd);
      isSubscribed = true;
      delay(500);
    } else {
      Serial.println("TCP连接失败");
      delay(2000);
      return;
    }
  }

  // 接收服务器指令
  if (client.available()) {
    String msg = client.readStringUntil('\n');
    Serial.print("服务器消息：");
    Serial.println(msg);

    if (msg.indexOf("msg=on") != -1) {
      digitalWrite(0, LOW);
      Serial.println("✅ 继电器开启");
    }
    if (msg.indexOf("msg=off") != -1) {
      digitalWrite(0, HIGH);
      Serial.println("❌ 继电器关闭");
    }
  }

  // 30秒心跳保活
  if (millis() - lastPing > 30000 && isSubscribed) {
    client.print("ping\r\n");
    Serial.println("❤️ 心跳保活");
    lastPing = millis();
  }

  delay(100);
}