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


