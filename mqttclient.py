import paho.mqtt.subscribe as subscribe
from car_control import CarControl

host = "mqtt.eclipse.org"
topic = "car_control"
control_commands = ["Front", "Back", "RightTurn", "LeftTurn", "SetSpeed", "StraightRight", "StraightLeft"]
controls = {"Front":0, "Back":1, "RightTurn":2, "LeftTurn":3, "SetSpeed":4, "StraightRight":5, "StraightLeft":6}


class MqttListener(object):
    
    #subscribe = subscribe()
    
    def __init__(self, host, topic):
        self.host = host
        self.topic = topic
        self.cc = CarControl()
        

    def subscribe_callback(self, call_back):
        subscribe.callback(call_back, topics = self.topic, hostname = self.host)
         
    def unsubscribe(self):
        pass
    
    def command_callback(self, client, userdata, message):
        print ("command_callback:payload", message.payload)
        speed = 0    
        if "SetSpeed" in message.payload:
            data = message.payload.split(",")
            speed = int(data[1])
            payload = "SetSpeed"
            command_data = controls[payload]
        else:
            payload = message.payload
            command_data = controls[payload]
            
        print("Command: {}, Data:{}, Speed:{}".format(payload, command_data, speed))
        
        if(payload != "SetSpeed"):
            self.cc.drive_mode(command_data)
        else:
            self.cc.drive_mode(command_data, speed)
    
    
def main():
    
    mqtt_client = MqttListener(host, topic)
    mqtt_client.subscribe_callback(mqtt_client.command_callback)
    
    
if __name__ == "__main__":
    main()
