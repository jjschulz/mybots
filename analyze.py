import numpy as np
import matplotlib.pyplot as plt

# backLegSensorValues=np.load('data/backlegSensorVals.npy')
# frontLegSensorValues=np.load('data/frontlegSensorVals.npy')
# # print(backLegSensorValues)

# plt.plot(backLegSensorValues, label='back leg values', linewidth=3)
# plt.plot(frontLegSensorValues, label='front leg values')
# plt.legend()
# plt.show()


BacklegSineValues=np.load('data/BacklegSineValues.npy')
FrontlegSineValues=np.load('data/FrontlegSineValues.npy')
plt.plot(BacklegSineValues)
plt.plot(FrontlegSineValues)
plt.show()