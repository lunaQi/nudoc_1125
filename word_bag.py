# -*- coding:utf-8 -*-

import pickle as pk
kinds = ['car','gat', 'house', 'it', 'jinrong', 'jk', 'mil', 'ny', 'ty', 'yl']
#Sum_list = []
bag_list = []
#f2 = open("/Users/luna/nudoc/wordBag.txt",'w')
for kind in kinds:
    list_Class = pk.load(open("/Users/luna/nudoc/" +kind+'/'+kind+"_chisquare.npy",'rb'))
    for i in range(0,500):
        #Sum_list.append(list_Class[i])
        tmp = list(list_Class[i])
        bag_list.append(tmp[0])
        #f2.write(str(tmp[0]) + "\n")
#f2.close()
#pk.dump(Sum_list,open('/Users/luna/nudoc/wordSumList.npy', 'wb'))
pk.dump(bag_list,open('/Users/luna/nudoc/bagListSum.npy', 'wb'))
bag_set = set(bag_list)
bag_ListFinal = list(bag_set)
pk.dump(bag_ListFinal,open('/Users/luna/nudoc/bagListFinal.npy','wb'))
print(len(bag_ListFinal))
print("Finished!")