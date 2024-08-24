#--Run4 complete ok set arm 80 degree position 3.1
  
    motor.run_for_degrees(port.E,math.floor(90*(1.8)),900)
    await moveHeadTo(57,-1,900)
    await moveHeadTo(6.5,-1,600)
    await turnDeg(67,False)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(38),1000,800)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(-85),1000,980)
