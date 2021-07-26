edge=[0,1,2,3,4,5]
file = open('text1.txt', 'w')
file.write('\n')      #将回车写入txt文件中
file.write(' ')        #将空格写入txt文件中
file.write('abc')  #将abc写入 txt文件中
file.write(str(edge[0])) #将数组数据第0号元素写入txt文件中
file.close()