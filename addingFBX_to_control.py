import maya.cmds as cmds


fbxJnt_list = [u'Hips', u'Spine', u'Spine1', u'Spine2', u'Neck', u'Head', u'LeftShoulder', u'LeftArm', u'LeftForeArm', u'LeftHand', u'LeftHandThumb1', u'LeftHandThumb2', u'LeftHandThumb3', u'LeftHandIndex1', u'LeftHandIndex2', u'LeftHandIndex3', u'LeftHandMiddle1', u'LeftHandMiddle2', u'LeftHandMiddle3', u'LeftHandRing1', u'LeftHandRing2', u'LeftHandRing3', u'LeftHandPinky1', u'LeftHandPinky2', u'LeftHandPinky3', u'RightShoulder', u'RightArm', u'RightForeArm', u'RightHand', u'RightHandPinky1', u'RightHandPinky2', u'RightHandPinky3', u'RightHandRing1', u'RightHandRing2', u'RightHandRing3', u'RightHandMiddle1', u'RightHandMiddle2', u'RightHandMiddle3', u'RightHandIndex1', u'RightHandIndex2', u'RightHandIndex3', u'RightHandThumb1', u'RightHandThumb2', u'RightHandThumb3', u'LeftUpLeg', u'LeftLeg', u'LeftFoot', u'LeftToeBase', u'RightUpLeg', u'RightLeg', u'RightFoot', u'RightToeBase']

rigJnt_list = [u'root_IK_ctrl', u'spine_01_FK_ctrl', u'spine_02_FK_ctrl', u'spine_IK_ctrl', u'neck_FK_01_ctrl', u'head_ctrl', u'cavicle_l_FK_ctrl', u'upperarm_l_FK_ctrl', u'lowerarm_l_FK_ctrl', u'hand_l_FK_ctrl' , u'thumb_01_l_Ctrl', u'thumb_02_l_Ctrl', u'thumb_03_l_Ctrl',  u'index_02_l_Ctrl', u'index_03_l_Ctrl', u'index_04_l_Ctrl', u'middle_02_l_Ctrl', u'middle_03_l_Ctrl', u'middle_04_l_Ctrl',   u'ring_02_l_Ctrl', u'ring_03_l_Ctrl', u'ring_04_l_Ctrl',u'pinky_02_l_Ctrl', u'pinky_03_l_Ctrl', u'pinky_04_l_Ctrl', u'cavicle_r_FK_ctrl', u'upperarm_r_FK_ctrl', u'lowerarm_r_FK_ctrl', u'hand_r_FK_ctrl', u'pinky_02_r_Ctrl', u'pinky_03_r_Ctrl', u'pinky_04_r_Ctrl', u'ring_02_r_Ctrl', u'ring_03_r_Ctrl', u'ring_04_r_Ctrl', u'middle_02_r_Ctrl', u'middle_03_r_Ctrl', u'middle_04_r_Ctrl', u'index_02_r_Ctrl', u'index_03_r_Ctrl', u'index_04_r_Ctrl',u'thumb_01_r_Ctrl', u'thumb_02_r_Ctrl', u'thumb_03_r_Ctrl' , u'thigh_l_FK_ctrl', u'calf_l_FK_ctrl', u'foot_l_FK_ctrl', u'ball_l_FK_ctrl', u'thigh_r_FK_ctrl', u'calf_r_FK_ctrl', u'foot_r_FK_ctrl', u'ball_r_FK_ctrl']

#jntSel = cmds.ls(sl=True)
#print jntSel





def addFBXanim(animName):
    num = 0
    #animName = 'Hip_Hop_Dancing'
    
    
    
    constList = []
    for num in range(0,len(fbxJnt_list)):
        print animName + ':' + fbxJnt_list[num]
        print rigJnt_list[num]
        
        orientConst = cmds.orientConstraint(animName + ':' + fbxJnt_list[num], rigJnt_list[num],mo =1)
        #constList.append(orientConst)

        

addFBXanim('Hip_Hop_Dancing_01')