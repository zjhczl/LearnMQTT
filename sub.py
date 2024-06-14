import paho.mqtt.client as mqtt

# 当连接到服务器时的事件处理


def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 订阅一个主题
    client.subscribe("thing/product/5YSZKBJ0020YX9/state")
    # client.subscribe("thing/product/5YSZKBJ0020YX9/osd")
    client.subscribe("thing/product/5YSZKBJ0020YX9/services")
    client.subscribe("thing/product/5YSZKBJ0020YX9/services_reply")

    # client.subscribe("thing/product/5YSZKBJ0020YX9/osd")
    # client.subscribe("thing/product/1581F5FHD22C100C6QMF/osd")


# 当接收到来自服务器的消息时的事件处理


def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}\nMessage: {msg.payload.decode()}")


# 创建一个MQTT客户端对象
client = mqtt.Client()

# 绑定事件处理函数
client.on_connect = on_connect
client.on_message = on_message

# 连接到MQTT代理服务器
client.connect("test.com", 1883)

# 在一个无限循环中等待接收消息
client.loop_forever()
