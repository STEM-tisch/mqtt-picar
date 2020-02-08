import logging
import time
import picar

_INITIAL_SPEED = 50 # 0 - SLOW, 100 - FASTEST

class CarControl(object):
    
    def __init__(self, initial_speed = _INITIAL_SPEED):
        logging.info("Setting up CarControl...")
        print ("Setting up CarControl ....")
        self.initial_speed = initial_speed
        
        picar.setup()
        
        self.back_wheels = picar.back_wheels.Back_Wheels()
        self.front_wheels = picar.front_wheels.Front_Wheels()
        
        
        logging.info("Setting up Back Wheels...")
        print ("Setting up Back Wheels ....")
        self.back_wheels.speed = 0
        
        time.sleep(2)
        logging.info("Setting up Front Wheels...")
        print ("Setting up Front Wheels ....")          
        self.front_wheels.turning_offset = -25
        self.front_wheels.turn(90)
        time.sleep(2)
        
    def drive_test(self):
        self.back_wheels.speed = 90
        time.sleep(3)
        self.front_wheels.turn(90)
        self.back_wheels.forward()
        time.sleep(3)
        self.front_wheels.turn(90)
        self.back_wheels.backward()
        time.sleep(3)
        self.front_wheels.turn(170)
        self.back_wheels.forward()
        time.sleep(3)
        self.front_wheels.turn(10)
        self.back_wheels.forward()
        time.sleep(3)
        self.front_wheels.turn(130)
        self.back_wheels.forward()
        time.sleep(3)
        self.front_wheels.turn(50)
        self.back_wheels.forward()

    
    def drive_mode(self, mode, speed=_INITIAL_SPEED):
        
        if mode == 0:
            self.front_wheels.turn(90)
            self.back_wheels.forward()
        elif mode == 1:
            self.front_wheels.turn(90)
            self.back_wheels.backward()
        elif mode == 2:
            self.front_wheels.turn(170)
            self.back_wheels.forward()
        elif mode == 3:
            self.front_wheels.turn(10)
            self.back_wheels.forward()
        elif mode == 4:
            self.back_wheels.speed = speed
        elif mode == 5:
            self.front_wheels.turn(130)
            self.back_wheels.forward()
        elif mode == 6:
            self.front_wheels.turn(50)
            self.back_wheels.forward()
            
    def cleanup():
        self.back_wheels.speed = 0
        self.front_wheels.turn(90)
        
        
if __name__ == "__main__":
    car = CarControl()
    car.drive_test()
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        car.cleanup()
    
