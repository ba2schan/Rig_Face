selDriven = cmds.ls(sl=True)
selDriver =  cmds.ls(sl=True)

for num in range(0,len(selDriver)):
    cmds.pointConstraint(selDriver[num], selDriven[num], mo = 1)
    cmds.connectAttr(selDriver[num] + '.translate', selDriven[num]+ '.translate')
    