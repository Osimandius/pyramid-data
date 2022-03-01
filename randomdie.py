import random
import plotly.express as px
import plotly.figure_factory as ff
count = []
dice_result = []
for i in range (0,1000000):
    dice1 = random.randint(1,2)
    dice2 = random.randint(1,20)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    #print(dice_result)
    count.append(i)

# graf2=px.bar(x=dice_result, y=count)
# graf2.show()

fig = ff.create_distplot([dice_result],["Result"])
fig.show()