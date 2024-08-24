    speedR3 = 700
#--Run3 position 2
    await moveHeadTo(51,0,670)
    await turnDeg(60,False,speed=300)
    await moveHeadTo(68,68,670) #deliver masterpiece
    motor_pair.move_for_degrees(motor_pair.PAIR_1, math.floor(200*10/5.6),100, velocity=400, stop=motor.SMART_BRAKE, acceleration=200) #from heuritic calculation, have to recheck another hub
    await runloop.sleep_ms(650)
    motor.run_for_degrees(port.E,math.floor(225*(1.8)),450)
    await runloop.sleep_ms(2000)
    motor.run_for_degrees(port.E,math.floor(-240*(1.8)),230)
    await moveHeadTo(18.8,-130,450)
    await headToCw(-88,False,200,manualTurn=-42)
    await motor.run_for_degrees(port.E,math.floor(240*(1.8)),1000,acceleration=7000)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(54),693,745,stop=motor.COAST,acceleration=1000)
    motor.run_for_degrees(port.E,math.floor(-220*(1.8)),1000,acceleration=7000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,cmToDegrees(-30),20,velocity=600,stop=motor.CONTINUE,acceleration=1000)
    motor.run_for_degrees(port.E,math.floor(-30*(1.8)),1000,acceleration=7000)
    motor_pair.move_for_degrees(motor_pair.PAIR_1,cmToDegrees(-55),0,velocity=1000,acceleration=7000)
#--------------------------------------------------------------------------

#--R3 Fast-----------------------------------------------------------------
    #--R3 Fast-----------------------------------------------------------------
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(123),720,820,stop=motor.SMART_BRAKE,acceleration=1000)
    motor_pair.move_for_degrees(motor_pair.PAIR_1, math.floor(240*10/5.6),100, velocity=400, stop=motor.SMART_BRAKE, acceleration=200) #from heuritic calculation, have to recheck another hub
    motor.run_for_degrees(port.E,math.floor(225*(1.8)),230)
    await runloop.sleep_ms(2500)
    motor.run_for_degrees(port.E,math.floor(-240*(1.8)),230)
    await moveHeadTo(20,-130,450)
    await headToCw(-90,False,200,manualTurn=-40)
    await motor.run_for_degrees(port.E,math.floor(240*(1.8)),1000,acceleration=7000)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(54),693,745,stop=motor.COAST,acceleration=1000)
    motor.run_for_degrees(port.E,math.floor(-220*(1.8)),1000,acceleration=7000)
    await motor_pair.move_for_degrees(motor_pair.PAIR_1,cmToDegrees(-30),20,velocity=600,stop=motor.CONTINUE,acceleration=1000)
    motor.run_for_degrees(port.E,math.floor(-30*(1.8)),1000,acceleration=7000)
    motor_pair.move_for_degrees(motor_pair.PAIR_1,cmToDegrees(-50),0,velocity=1000,acceleration=7000)
#--------------------------------------------------------------------------
