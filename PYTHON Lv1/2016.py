"""
2016년 1월 1일이 금요일일 때, 2016년 a월 b일은?
"""

import datetime
def solution(a, b):
    DateDict={0:'MON', 1:'TUE', 2:'WED', 3:'THU', 4:'FRI', 5:'SAT', 6:'SUN'}
    #answer = ''
    #return answer
    return DateDict[datetime.date(2016,a,b).weekday()]


def solution(a,b):
    months=[31,29,31,30,31,30,31,31,30,31,30,31]
    days='FRI SAT SUN MON TUE WED THU'.split()
    return days[(sum(months[:a-1])+b-1)%7]