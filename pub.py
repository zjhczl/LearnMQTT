

import paho.mqtt.client as mqtt
import json

# 创建 MQTT 客户端
client = mqtt.Client()

# 连接到 MQTT 服务器
client.connect("test.com", 1883, 60)  # 你需要替换为你的 MQTT 服务器地址和端口

# 创建你的消息
message = {
    "tid": "3bbf17b1-5573-46fd-a329-a657e2b43303",
    "bid": "adcce92d-d15d-4cfa-9795-115bb7967efb",
    "data": {
        "url_type": 1,
        "url": "rtmp://gis.breton.top:1935/live/123456",
        "video_id": "1581F5FHD22C100C6QMF/66-0-0/zoom-0",
        "video_quality": 1
    },
    "method": "live_start_push"
}


# 将字典转换为 JSON 格式的字符串
message_json = json.dumps(message)

# 发布消息到特定的主题
client.publish("thing/product/5YSZKBJ0020YX9/services", message_json)

# 断开与 MQTT 服务器的连接
client.disconnect()
