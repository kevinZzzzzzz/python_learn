"""
需求：实现一个成绩统计程序，可以对多名学生的成绩，进行统计和分析
备注：用户可以连续输入学生的成绩，直到用户输入"结束"字符串
最后输出
    总人数
    最高分
    最低分
    合格人数
    合格率
    优秀人数
    优秀率
    平均分数
"""

pointList = list()


def finalFun():
    print(pointList)
    amount = len(pointList)
    maxP = max(pointList)
    minP = min(pointList)
    moreThen60 = 0
    moreThen90 = 0
    for item in pointList:
        if item >= 90:
            moreThen90 += 1
            moreThen60 += 1
        elif item >= 60:
            moreThen60 += 1
    moreThen60Pre = float(moreThen60 / amount * 100)
    moreThen90Pre = float(moreThen90 / amount * 100)
    avg = sum(pointList) / amount
    print("""
    总人数%d
    最高分%d
    最低分%d
    合格人数%d
    合格率%.2f
    优秀人数%d
    优秀率%.2f
    平均分数%.2f
    """ % (amount, maxP, minP, moreThen60,moreThen60Pre, moreThen90, moreThen90Pre, avg))


def main():
    global pointList
    flag = True
    while flag:
        point = input("请输入分数:")
        if (point == '结束'):
            flag = False
        else:
            pointList.append(int(point))

    finalFun()
main()
