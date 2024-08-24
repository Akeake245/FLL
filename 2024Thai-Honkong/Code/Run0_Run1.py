#--Test command-----------------------------------------------------------


#Run  0
    await moveHeadTo(200,0,1000)


#--------------------------------------------------------------------------
#--Run1 complete black at 2
    speedR1=800
    await moveHeadTo(29,0,600)
    await headToCw(90,False,500,acc=200,manualTurn=-90)
    await moveHeadTo(10,90,400)
    await moveHeadTo(4,110,900)
    await moveHeadTo(10,113,400)
    await moveHeadTo(14,112,150)
    await headToCw(130,False,300,acc=150,manualTurn=-20)
    await motor.run_for_degrees(port.D,math.floor(-2000),800)
    await moveHeadTo(3,110,400)
    motor.run_for_degrees(port.E,math.floor(200*1.8),195)
    await moveHeadTo(-17,100,880)
    await moveHeadTo(6,105,900)
    await moveHeadTo(58,85,850)
    await moveHeadTo(-3,120,250)
    await motor.run_for_degrees(port.D,math.floor(-3000),850)
    await moveHeadTo(80,100,850)
    await motor.run_for_degrees(port.E,math.floor(-105*1.8),speedH)
#-----------------------------------------------------------------------
