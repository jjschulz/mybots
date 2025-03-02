import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p
class MOTOR:
    def __init__(self, jointName):
        self.jointName=jointName
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude=c.Backleg_amplitude
        joint_name = str(self.jointName, 'utf-8')
        if joint_name == "Torso_Backleg":
            self.frequency=c.Backleg_frequency
        else:
            self.frequency=c.Frontleg_frequency
        self.offset=c.Backleg_phaseOffset
        targetAngles=np.linspace(-np.pi,np.pi,c.loopConstant)
        self.motorValues=self.amplitude * np.sin(self.frequency * targetAngles + self.offset)

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
        bodyIndex = robotId,
        jointName = self.jointName,
        controlMode = p.POSITION_CONTROL,
        targetPosition = desiredAngle,
        maxForce = 500)

    def Save_Values(self):
        np.save("data/motorVals", self.motorValues)
