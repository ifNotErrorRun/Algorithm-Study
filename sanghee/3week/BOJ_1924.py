# https://www.acmicpc.net/problem/1924
# feat: 2007년 BOJ_1924.py

# 문제
# 오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

# 출력
# 첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.


month, day = input().split()

def WhatDayToday(month, day):

  month = int(month)
  day = int(day)

  days_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  days_week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

  while month >= 2:
    day = day + days_month[month - 2]
    month -= 1

  for i in range(7):
    if day % 7 == i:
      print(days_week[i])

WhatDayToday(month, day)