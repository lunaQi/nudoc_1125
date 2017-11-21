# -*- coding: utf-8 -*-

import pickle as pk
import os
#from tqdm import tqdm
kind1 = ['car','gat', 'house', 'it', 'jinrong', 'jk', 'mil', 'ny', 'ty', 'yl']
for kind in kind1:
    attribute_dic = {}
    f1 = open('/Users/luna/nudoc/' +kind + '/' + kind + '.txt','r')
    lines = f1.readlines()   #readlines自动将文件内容存到一个行的列表,会有"\n"
    #lines = f1.read().splitlines() #去除'\n'每行的
    #txt = f1.read()
    #print   #lines:存放着所有列的list
    #for word in lines:
        #print word
    #f1.close()
    for word in lines:
        word = word.strip("\n")
        if word is not '':
            attribute_dic[word] = 0
    #print('字典中的key:',len(attribute_dic))
    path = '/Users/luna/af_stopwords/training-' + kind
    #path = "/Users/luna/PycharmProjects/CHI/training_test/car"
    #os.makedirs("/Users/luna/nudoc/car")
    #nudoc_path = "/Users/luna/nudoc/car"
    files = os.listdir(path)
    file_path = []
    for file in files:
        child = os.path.join('%s/%s' %(path,file))
        if('.DS_Store' not in child):
            file_path.append(child)
    #print(file_path)
    #print file_path
    for file in file_path:
        f_o2o = open(file,'r')
        words= f_o2o.read().split(' ')
        # for i in words_temp:
        #print(words)   #words里有''

        #print words
        text_set = set(words)
        text_list = list(text_set)  #将得到的词语再转换成list，方便遍历
        #print("111111",text_list)
        for i in text_list:
            if i is not '':
                attribute_dic[i] =attribute_dic[i]+ 1
                #print(i,attribute_dic[i],'\n')

    pk.dump(attribute_dic,open('/Users/luna/nudoc/' + kind + '/' + kind +'.npy','wb'))

    '''
    print('pd转换开始')
    data = pd.DataFrame(attribute_dic)
    print('pd转换完成')
    #print attribute_dic
    #print data
    print('csv输出')
    data.to_csv('/data/luna/chi-sum/'+kind+'_sum.csv')
    #print(data.shape)
    '''
print('Finished')
