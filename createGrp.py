grpName = 'grp'

sel = cmds.ls(sl=True)
grpList =[]
for obj in sel:
    
    grp = cmds.createNode('transform', n = obj + '_' + grpName)
    cmds.delete(cmds.parentConstraint(obj, grp, mo = 0 ))
    getParent = cmds.listRelatives(obj, p = True)

    cmds.parent(obj, grp)
    
    cmds.parent(grp, getParent)
    grpList.append(grp)


