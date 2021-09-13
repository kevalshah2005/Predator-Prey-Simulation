import random
import math
from matplotlib import pyplot as plt
from tqdm import tqdm

MiceNum = 10
WeaselNum = 1
miceList = []
weaselList = []
WeaselOffspringNum = 0
AmountEaten = 0
def AmountEatenFunction(MiceNum):
  AmountEaten = random.randint(math.floor(MiceNum/10), math.floor(MiceNum/5))
  return AmountEaten

generations = int(input("# of generations: "))

InitialPrey = MiceNum
InitialPredators = WeaselNum
PreyCaptured = 0
PreySurvivors = MiceNum
PredatorSurvivors = 0

i_range = tqdm(range(generations), desc="Loading...")

for i in i_range:
  InitialPrey = MiceNum
  InitialPredators = WeaselNum
  PreyCaptured = 0
  for j in range(WeaselNum):
    AmountEaten = AmountEatenFunction(MiceNum)
    WeaselOffspringNum = math.floor(AmountEaten / 4)
    if WeaselOffspringNum == 0:
      WeaselNum-=1
    MiceNum-=AmountEaten
    PreyCaptured += AmountEaten
  WeaselNum+=WeaselOffspringNum
  weaselList.append(WeaselNum)
  miceList.append(MiceNum)

  PreySurvivors = MiceNum
  if (MiceNum*2 < 100):
    MiceNum*=2
  else:
    MiceNum = 100
  if (MiceNum < 10):
    MiceNum = 10
  if WeaselNum == 0:
    WeaselNum+=1
  PredatorSurvivors = WeaselNum - WeaselOffspringNum
  PredatorOffspring = WeaselOffspringNum
  WeaselOffspringNum = 0
  AmountEaten = 0

  #print(InitialPrey, PreyCaptured, PreySurvivors, InitialPredators, PredatorSurvivors, PredatorOffspring)

#print("Mice List: "  + str(miceList))
#print("Weasel List: " + str(weaselList))

GenerationsNum = []
for i in range(generations):
  GenerationsNum.append(i)
  #GenerationsNum = np.append(GenerationsNum, i)

#Creating a plot for the data (WIP)
plt.plot(GenerationsNum, miceList, label = "Mice") 
plt.plot(GenerationsNum, weaselList, label = "Weasels")
plt.xlabel('Generations') 
plt.ylabel('# of Mice/Weasels')
plt.xlim([0, generations])
plt.title('Generations vs # of Mice')
plt.yscale('log', base=2)
plt.rcParams["font.size"] = 2
plt.legend()
plt.show()