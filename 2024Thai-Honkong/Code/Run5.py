#--Run5 complete start at 4 1 big yellow lego with small blue part

    speedR5 = 850
    await moveHeadTo(37,0,750)
    await motor.run_for_degrees(port.E,math.floor(182*(1.8)),1000)
    await moveHeadTo(25,0,699)
    await motor.run_for_degrees(port.E,math.floor(-90*(1.8)),1000)
    await moveHeadTo(-3,0,700)
    await turnDeg(43,True)
    await moveHeadTo(16,-46,speedR5)
    await turnDeg(43,False)
    await motor_pair.move_tank_for_degrees(motor_pair.PAIR_1,cmToDegrees(300),980,1000,acceleration=5000)
