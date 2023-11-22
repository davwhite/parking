import paho.mqtt.publish as publish

# MQTT broker details
broker_url = "mosquitto-service"
broker_port = 1883  # Default MQTT port

# Topic and message to publish
topic = "test"
message = "Hello World"

# Publish the message to the MQTT broker
publish.single(topic, message, hostname=broker_url, port=broker_port)

print(f"Published message '{message}' to topic '{topic}' on {broker_url}:{broker_port}")
