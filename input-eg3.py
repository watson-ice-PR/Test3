choice=input('请问您需要帮助吗？需要or不需要？')
if choice=='需要':
    elect=int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if elect==1:
        print('请去存取款窗口')
    elif elect==2:
        number=int(input('您需要兑换多少金加隆？'))
        print('您需要付人民币'+str(number*51.3)+'元')
        print('您需要付人民币', number*51.3, '元')
    else:
        print('请去咨询款窗口')
else:
    print('再见')