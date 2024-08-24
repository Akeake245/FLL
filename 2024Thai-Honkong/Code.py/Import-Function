from hub import light_matrix, port, motion_sensor
import runloop
import motor, motor_pair, force_sensor
import math
#from typing import ForwardRef



#-----Global variables for this program that can be used in all functions---------------
heading = 0
speedL = 200        #speed deault 360
speedH = 480
accelL = 500        #acceleration default 1000
# N = 0, NW = 45, W = 90, SW = 135, S = 180, SE = -135, E = -90, NE = -45

#-----Functions--------------------------------------------------------------------------
#---Function intitials robot-------------------------------------------------------------
def initBot():
#initial drivetrain
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1,port.A,port.B) # pair main driving motor A & B
    #initial motion sensor
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
    motion_sensor.reset_yaw(0)

# Function coverts dictance in CM to motor degree of 8..8cm wheel------------------------
def cmToDegrees(cm=1.0):
    return math.floor(cm*20.46) # 13 for big wheel & 20.46 fof small wheel

#---Function turn to heading---------------------------------------------------------------
async def headToCw(targetHead=0,cw=True, speed=360,brakeMode=motor.COAST,acc=1000, manualTurn=0,):
    await runloop.until(motion_sensor.stable,timeout=300) #wait until motion sensor stable
    if motion_sensor.tilt_angles()[0] == -1800:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, math.floor(manualTurn*10/5.6), 100, velocity=speed, stop=brakeMode, acceleration=acc) #from heuritic calculation, have to recheck another hub
        return
    motor.reset_relative_position(port.A,0) #reset wheel distance before turn
    motor.reset_relative_position(port.B,0)
    turnDegrees = abs(math.floor(manualTurn*10/5.6)) # calculate turn degree +
    if cw: #CW
        while (motion_sensor.tilt_angles()[0]-targetHead*10>20) or (motion_sensor.tilt_angles()[0]<10 and targetHead*10>10 ):
            motor_pair.move(motor_pair.PAIR_1,100,velocity=speed,acceleration=acc)
            if math.floor((abs(motor.relative_position(port.A))+abs(motor.relative_position(port.B)))*0.5) > abs(turnDegrees+5): #move not over 0.5 degree break prevent from fail gyro
                break # walk up to manual degree
    else: #CCW
        while (targetHead*10-motion_sensor.tilt_angles()[0]>20) or (motion_sensor.tilt_angles()[0]>-10 and targetHead*10<10 ):
            motor_pair.move(motor_pair.PAIR_1,-100,velocity=speed,acceleration=acc)
            if math.floor((abs(motor.relative_position(port.A))+abs(motor.relative_position(port.B)))*0.5) > abs(turnDegrees+5): #move not over 0.5 degree break prevent from fail gyro
                break # walk up to manual degree

    motor_pair.stop(motor_pair.PAIR_1,stop=brakeMode)
#------------------------------------------------------------------------------------------

#---Function Move head to and distace in centimeter----
async def moveHeadTo(cm=1.0,targetHead=0,speed=360,brakeMode=motor.COAST,acc=500):
    await runloop.until(motion_sensor.stable,timeout=300) #wait until motion sensor stable
    motor.reset_relative_position(port.A,0) #reset wheel distance
    motor.reset_relative_position(port.B,0)
    turnDegrees = cmToDegrees(cm)
    if motion_sensor.tilt_angles()[0] == -1800:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1,turnDegrees,0,velocity=speed,stop=brakeMode,acceleration=acc) #Manual move when gyro fail
        return
    if speed >=500:
        errorFactor = -1.5
    else:
        errorFactor = -2

    while math.floor((abs(motor.relative_position(port.A))+abs(motor.relative_position(port.B)))*0.5) < abs(turnDegrees):
        # compute the error in degrees from 0
        error = (motion_sensor.tilt_angles()[0]-(targetHead*10)) * -0.1
        # correction is an integer which is the negative of the error
        if abs(motion_sensor.tilt_angles()[0]) == 1800 :
            correction = 0 #no correction when gyro fail
        else:
            correction = int(error * errorFactor)
        # apply steering to correct the error
        if cm >=0:
            motor_pair.move(motor_pair.PAIR_1, correction, velocity= speed, acceleration=acc) #move FW
        else:
            motor_pair.move(motor_pair.PAIR_1, -correction, velocity= -speed, acceleration=acc) #move FW
    motor_pair.stop(motor_pair.PAIR_1,stop=brakeMode)
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
async def turnDeg(turnDegree=180, cw=True,speed=500,acc=500):
    if cw:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, math.floor(turnDegree*10/5.6), 100, velocity=speed, stop=motor.SMART_BRAKE, acceleration=acc) #from heuritic calculation, have to recheck another hub
    else:
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, math.floor(turnDegree*10/5.6), -100, velocity=speed, stop=motor.SMART_BRAKE, acceleration=acc) #from heuritic calculation, have to recheck another hub
    return
#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------
async def main():
# write your code here
    await light_matrix.write("T")
    initBot()#initial robot drivetrain and sensors
    runloop.sleep_ms(200)
    heading = 0
