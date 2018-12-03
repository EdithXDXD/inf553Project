import numpy as np

dim = 4
user_based_dict = {}
personal_dict = {}
xuez_tao_dict = {}
kai_w_dict = {}
test_dict = {}
test_list = []

"""
with open("final_test.txt") as file:
    for line in file:
        data= line.split(" ")
        test_dict[data[0]+" "+data[1]]=float(data[2])
        test_list.append(data[0]+" "+data[1])

with open("model_predict.txt") as file:
    for line in file:
        data= line.split(" ")
        model_based_dict[data[0]+" "+data[1]]=float(data[2])

with open("personalize_score.txt") as file:
    for line in file:
        data= line.split(" ")
        personal_dict[data[0]+" "+data[1]]=float(data[2])
"""
with open("test_small_2.txt") as file:
    for line in file:
        data= line.split(",")
        test_dict[data[0]+" "+data[1]]=float(data[2])
        test_list.append(data[0]+" "+data[1])

with open("test_small2_item_output.txt") as file:
    for line in file:
        data= line.split(" ")
        xuez_tao_dict[data[0]+" "+data[1]]=float(data[2])

with open("small_person_score.txt") as file:
    for line in file:
        data= line.split(" ")
        personal_dict[data[0]+" "+data[1]]=float(data[2])

with open("user_based_result_2.txt") as file:
    for line in file:
        data= line.split(",")
        kai_w_dict[data[0]+" "+data[1]]=float(data[3])


N = len(test_list)
X = np.zeros((N, dim))
Y = np.zeros((N, 1))
w = np.zeros((dim, 1))

for i in range(N):
    Y[i][0] = test_dict[ test_list[i] ]
    if test_list[i] in xuez_tao_dict:
        X[i][0] = xuez_tao_dict[ test_list[i] ]
    else:
        X[i][0] = 3.5
    if test_list[i] in personal_dict:
        X[i][1] = personal_dict[ test_list[i] ]
    else:
        X[i][1] = 3.5
    if test_list[i] in kai_w_dict:
        X[i][2] = kai_w_dict[ test_list[i] ]
    else:
        X[i][2] = 3.5

    X[i][3]=1
    #if (i<10):
    #    print("x="+str(X[i][0])+","+str(X[i][1])+","+str(X[i][2])+" Y="+str(Y[i][0]))
        
lambd = 0.1
tmp = np.linalg.inv(np.dot(np.transpose(X), X) + lambd * np.eye(dim))
tmp = np.dot( tmp,  np.transpose(X))
w = np.dot(tmp, Y)
print("w="+str(w[0][0])+","+str(w[1][0])+","+str(w[2][0])+","+str(w[3][0]))
pred_result = np.dot(X,w)
errors = pred_result - Y
rss = np.sum(errors * errors)
print("rss="+str(np.sqrt(rss*1.0/N)))

y_1000_dict = {}
person_1000_dict = {}
xuez_tao_1000_dict = {}
kai_w_1000_dict = {}
test_dict = {}
y_1000_list = []
with open("test_small_1000.txt") as file:
    for line in file:
        data= line.split(",")
        y_1000_dict[data[0]+" "+data[1]]=float(data[2])
        y_1000_list.append(data[0]+" "+data[1])

with open("person_score_1000.txt") as file:
    for line in file:
        data= line.split(" ")
        person_1000_dict[data[0]+" "+data[1]]=float(data[2])

with open("user_based_result.txt") as file:
    for line in file:
        data= line.split(",")
        kai_w_1000_dict[data[0]+" "+data[1]]=float(data[3])

with open("test_small_item_output.txt") as file:
    for line in file:
        data= line.split(" ")
        xuez_tao_1000_dict[data[0]+" "+data[1]]=float(data[2])

N_1000 = len(y_1000_list)
X_1000 = np.zeros((N_1000, dim))
Y_1000 = np.zeros((N_1000, 1))

for i in range(N_1000):
    Y_1000[i][0] = y_1000_dict[ y_1000_list[i] ]
    if y_1000_list[i] in xuez_tao_1000_dict:
        X_1000[i][0] = xuez_tao_1000_dict[ y_1000_list[i] ]
    else:
        X_1000[i][0] = 3.5
    if y_1000_list[i] in person_1000_dict:
        X_1000[i][1] = person_1000_dict[ y_1000_list[i] ]
    else:
        X_1000[i][1] = 3.5
    if y_1000_list[i] in kai_w_1000_dict:
        X_1000[i][2] = kai_w_1000_dict[ y_1000_list[i] ]
    else:
        X_1000[i][2] = 3.5

    X_1000[i][3]=1
    #if (i<10):
    #    print("x="+str(X[i][0])+","+str(X[i][1])+","+str(X[i][2])+" Y="+str(Y[i][0]))

test1000_pred = np.dot(X_1000, w)

TP = 0
TN = 0
FP = 0
FN = 0
for i in range(N_1000):
    if (test1000_pred[i][0]>=4.0 and Y_1000[i][0]>=4.0):
        TP += 1
    elif (test1000_pred[i][0]>=4.0 and Y_1000[i][0]<4.0):
        FP += 1
    elif (test1000_pred[i][0]<4.0 and Y_1000[i][0]<4.0):
        TN += 1
    else:
        FN += 1
print("precision="+str( TP*1.0/(TP+FP) ))
print("recall="+str( TP*1.0/(TP+FN) ))
print("accuracy="+str( (TP+TN)*1.0/(TP+TN+FP+FN) ))

print(" ")
for i in range(20):
    print("prediction:"+str(test1000_pred[i][0])+", actual:"+str(Y_1000[i][0]))






