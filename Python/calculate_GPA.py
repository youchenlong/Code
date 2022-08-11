# 分数
scores = []
# 学分
credit = []
# 输入分数和学分
while True:
    s = input('请输入课程分数（输入quit结束）：')
    if s == 'quit':
        break
    c = input('请输入课程学分：')
    if s.isdigit() and c.isdigit():
        scores.append(float(s))
        credit.append(float(c))
    else:
        print('分数和学分必须是数字，请重新输入')
# 计算GPA
total_credit = sum(credit)
weighted_scores = 0
for s,c in zip(scores, credit):
    if s >= 90:
        s = 4
    elif s < 60:
        s = 0
    else:
        s = (s-60)/10 + 1
    weighted_scores += s*c
GPA = weighted_scores / total_credit
print(GPA)