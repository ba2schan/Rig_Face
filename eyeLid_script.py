from maya import cmds, OpenMaya

#select vetx around eye lid

#create locator and put center of eyeball(remove after setup)

center = 'center'
side = ['L', 'r']
part = 'down'
num = 0

vtx = cmds.ls(sl = 1, fl= 1)
grp = cmds.createNode('transform', n = side[0] + '_eye_'+ part +'_grp')

if cmds.objExists('xform'):
    cmds.parent(grp,'xform')


for v in vtx:
    
    num += 1
    cmds.select(cl = 1)
    jnt = cmds.joint()

    renameJnt = cmds.rename( jnt,   str(side[0])+ '_eye_' + str(num) +'_end_'+ part +'_jnt' )
    pos = cmds.xform(v, q = 1 , ws =1, t = 1)
    cmds.xform(renameJnt, ws=1, t = pos)
    posC = cmds.xform(center, q = 1, ws = 1, t = 1)
    cmds.select(cl= 1 )
    jntC = cmds.joint()
    renameJntC  = cmds.rename( jntC, str(side[0])+ '_eye_' + str(num)  + '_' + part +'_jnt'  )
    cmds.xform(renameJntC, ws = 1, t = posC)
    cmds.parent(renameJnt, renameJntC)
    cmds.parent(renameJntC, grp)

#----------------
#select joints

sel  = cmds.ls(sl=1)
num = 0
grp = cmds.createNode('transform', n = str(side[0]) + '_eye_'+ part +'_loc_grp')

for s in sel:
    num += 1
    loc = cmds.spaceLocator()[0]
    renameloc = cmds.rename( loc,  str(side[0]) + '_eye_' + str(num) +'_' + part + '_end_loc' )
    pos = cmds.xform(s, q=1, ws=1, t=1)
    cmds.xform(renameloc, ws =1, t=pos)
    par = cmds.listRelatives(s, p =1)[0]
    cmds.aimConstraint(renameloc, par, mo =1, weight =1 , aimVector =(1,0,0), upVector =(0,1,0), worldUpType = 'object', worldUpObject = 'L_eyeUpVec_Loc')
    cmds.parent(renameloc, grp)




#select locs
#create curve 

sel = cmds.ls(sl=True)
crv = 'curveShape1'
for s in sel:
    pos = cmds.xform(s ,q = 1 , ws = 1 , t = 1)
    u = getUParam(pos, crv)
    name = s.replace('loc_','pci_')
    pci = cmds.createNode('pointOnCurveInfo', n = name)
    #print pci
    cmds.connectAttr(crv + '.worldSpace', pci + '.inputCurve')
    cmds.setAttr(pci +  '.parameter', u)
    cmds.connectAttr(pci + '.position', s + '.t')


#run this first 

from maya import cmds , OpenMaya
def getUParam(pnt  = [], crv = None):

    point = OpenMaya.MPoint(pnt[0], pnt[1], pnt[2])
    curveFn = OpenMaya.MFnNurbsCurve(getDagPath(crv))
    paramUtill = OpenMaya.MScriptUtil()
    paramPtr = paramUtill.asDoublePtr()
    isOnCurve = curveFn.isPointOnCurve(point) 
    if isOnCurve == True:
        
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    else :
        point = curveFn.closestPoint(point,paramPtr,0.001,OpenMaya.MSpace.kObject)
        curveFn.getParamAtPoint(point , paramPtr,0.001,OpenMaya.MSpace.kObject )
    
    param = paramUtill.getDouble(paramPtr)  
    return param


def getDagPath( objectName):
    
    if isinstance(objectName, list)==True:
        oNodeList=[]
        for o in objectName:
            selectionList = OpenMaya.MSelectionList()
            selectionList.add(o)
            oNode = OpenMaya.MDagPath()
            selectionList.getDagPath(0, oNode)
            oNodeList.append(oNode)
        return oNodeList
    else:
        selectionList = OpenMaya.MSelectionList()
        selectionList.add(objectName)
        oNode = OpenMaya.MDagPath()
        selectionList.getDagPath(0, oNode)
        return oNode