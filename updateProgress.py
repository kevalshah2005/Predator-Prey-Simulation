import random
import math
import pandas as pd

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

table1Values = {
  'Weasel 1': [],
  'Weasel 2': [],
  'Weasel 3': [],
  'Weasel 4': [],
  'Weasel 5': [],
  'Weasel 6': [],
  'Weasel 7': [],
  'Weasel 8': [],
  'Weasel 9': [],
  'Weasel 10': [],
  'Weasel 11': [],
  'Weasel 12': [],
  'Weasel 13': [],
  'Weasel 14': [],
  'Weasel 15': [],
  'Weasel 16': [],
  'Weasel 17': [],
  'Weasel 18': [],
  'Weasel 19': [],
  'Weasel 20': []
}

table2Values = {
  'Generation 1': [],
  'Generation 2': [],
  'Generation 3': [],
  'Generation 4': [],
  'Generation 5': [],
  'Generation 6': [],
  'Generation 7': [],
  'Generation 8': [],
  'Generation 9': [],
  'Generation 10': [],
  'Generation 11': [],
  'Generation 12': [],
  'Generation 13': [],
  'Generation 14': [],
  'Generation 15': [],
  'Generation 16': [],
  'Generation 17': [],
  'Generation 18': [],
  'Generation 19': []
  }

for i in range(generations):
  InitialPrey = MiceNum
  InitialPredators = WeaselNum
  PreyCaptured = 0
  for i in range(WeaselNum):
    AmountEaten = AmountEatenFunction(MiceNum)
    table1Values['Weasel ' + str(i + 1)].append(AmountEaten)
    WeaselOffspringNum = math.floor(AmountEaten / 5)
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

  table2Rows = [InitialPrey, PreyCaptured, PreySurvivors, InitialPredators, PredatorSurvivors, PredatorOffspring]
  table2Values['Generation ' + str(i + 1)].extend(table2Rows)

  

print("Mice List: "  + str(miceList))
print("Weasel List: " + str(weaselList))
#print(table2Values)
table1 = pd.DataFrame(table1Values, columns= ['Weasel 1', 'Weasel 2', 'Weasel 3', 'Weasel 4', 'Weasel 5', 'Weasel 6', 'Weasel 7', 'Weasel 8', 'Weasel 9', 'Weasel 10', 'Weasel 11', 'Weasel 12', 'Weasel 13', 'Weasel 14', 'Weasel 15', 'Weasel 16', 'Weasel 17', 'Weasel 18', 'Weasel 19', 'Weasel 20'])
print(table1)

table2 = pd.DataFrame(table2Values, columns= ['Generation 1', 'Generation 2', 'Generation 3', 'Generation 4', 'Generation 5', 'Generation 6', 'Generation 7', 'Generation 8', 'Generation 9', 'Generation 10', 'Generation 11', 'Generation 12', 'Generation 13', 'Generation 14', 'Generation 15', 'Generation 16', 'Generation 17', 'Generation 18', 'Generation 19'])
print(table2)