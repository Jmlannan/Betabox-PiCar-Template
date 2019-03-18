from driver import camera, stream
from picar import back_wheels, front_wheels
import picar

picar.setup()
db_file = "/home/pi/SunFounder_PiCar-V/remote_control/remote_control/driver/config"

'''
Setup the front wheels with:
  fw = front_wheels.Front_Wheels(debug=False, db=db_file)
  fw.ready()
Turn with:
  fw.turn_right(), turn_left(), or turn(angle)
 Turn them back using
  Front_Wheels.turn_straight
  
 To make the motor turn use
  bw = back_wheels.Back_Wheels(debug-False, db=db_file)
  bw.ready()
  bw.speed = (speed between 0 and 100)
  bw.forward() to move forward and bw.backward() to move backwards

To move the camera
  cam = camera.Camera(debug=False, db=db_file)
  cam.ready()
  cam.turn_left(40)
  cam.turn_right(40)
  cam.turn_up(20)
  cam.turn_down(20)

'''