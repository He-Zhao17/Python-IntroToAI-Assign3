import restaurant as rest
import dt





test = rest.getARFFDataOfCancer("cancer.arff")

# test remainder
tempcolumns = test[0].columns
tempAtrr = test[0][tempcolumns[0]]
tempcla = test[0][tempcolumns[-1]]
tempres = dt.remainder(tempAtrr, tempcla)
#print(tempres)

#test select min remainder
data = test[0].drop([tempcolumns[-1]], axis = 1)
#tempmin = dt.selectAttribute(data, tempcla)
#print(tempmin)

root = dt.makeNode(test[0], test[1])
print("hellp")

# 5-fold cross validation
wholeData = test[0]
sumNum = wholeData.shape[0]
a = sumNum // 5
dataList = []
p = 0.0
for i in range(1, 5):
    delRowsArr = range((i - 1) * a, i * a)
    df = wholeData.drop(delRowsArr)
    classify = wholeData[delRowsArr]
    root = dt.makeNode(df, test[1])
    tNum = 0
    idx = classify.index
    cl = classify.columns
    for val in idx:
        temp = classify.iloc[val].drop[cl[-1]]
        if root.classify(temp) == classify.iloc[val][cl[-1]]:
            tNum += 1
    p += tNum / a
delRowsArr = range(4 * a , sumNum)
df = wholeData.drop(delRowsArr)
classify = wholeData[delRowsArr]
root = dt.makeNode(df, test[1])
tNum = 0
idx = classify.index
cl = classify.columns
for val in idx:
    temp = classify.iloc[val].drop[cl[-1]]
    if root.classify(temp) == classify.iloc[val][cl[-1]]:
        tNum += 1
p += tNum / (sumNum - 4 * a)
p = p / 5










