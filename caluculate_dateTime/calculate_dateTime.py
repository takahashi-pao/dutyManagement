import datetime
from datetime import date
import numpy

# -----------------------------------------------------
# 調査
# -----------------------------------------------------
print(date(2022, 9, 2).isocalendar())

# 関数はdef文で行う
def howWeekNow(year, month, day):
    # dt_now = datetime.datetime.now()
    # year = dt_now.year
    # month = dt_now.month
    # day = dt_now.day

    howWeek = date(year, month, day).isocalendar()
    week = int(howWeek.week)-31
    if week < 0:
        week = howWeek.week
    weekDay = howWeek.weekday
    match weekDay:
        case 1:
            weekDay = "月"
        case 2:
            weekDay = "火"
        case 3:
            weekDay = "水"
        case 4:
            weekDay = "木"
        case 5:
            weekDay = "金"
        case 6:
            weekDay = "土"
        case 7:
            weekDay = "日"
        case _:
            weekDay = "Not Define"
    howYear = howWeek.year
    
    print(str(year)+"年"+str(month)+"月"+str(day)+"日は"+str(howYear)+"年"+str(week)+"週目の"+str(weekDay)+"曜日です")

exe1 = howWeekNow(2022, 1, 1)


# --------------------------------------------------
# 本ロジック
# --------------------------------------------------

# 設定数値の入力
startYear = int(input("開始年"))
startMonth = int(input("開始月"))
startDay = int(input("開始日"))

comparisonYear = int(input("比較年"))
comparisonMonth = int(input("比較月"))
comparisonDay = int(input("比較日"))

# 開始日データ
def startDate(year, month, day):
    howWeek = date(year, month, day).isocalendar()
    week = int(howWeek.week)
    decreaseValue = week-1
    # startWeekは確定で1
    startWeek = week - decreaseValue
    startYear = howWeek.year

    # 開始日における年、週数（補正後）、補正値
    return startYear, startWeek, decreaseValue

# 比較日データ
def comparisonDate(year, month, day):
    howWeek = date(year, month, day).isocalendar()
    comparisonYear = howWeek.year
    comparisonWeek = howWeek.week

    # 比較日における年、週数（当該年に対して）
    return comparisonYear, comparisonWeek

# 結果データ
def resultDay():
    startData = startDate(startYear, startMonth, startDay)
    print(startData)
    comparisonData =  comparisonDate(comparisonYear, comparisonMonth, comparisonDay)
    print(comparisonData)
    print("比較週:"+str(comparisonData[1]))
    week = int(comparisonData[1])-int(startData[2])
    print("補正週:"+str(week))
    # 開始年と比較年が異なる場合は週数を引き継ぐ
    if not int(startData[0]) == int(comparisonData[0]):
        week = ((52-int(startData[2])))+int(comparisonData[1])
        arr = numpy.array([startData[0], comparisonData[0]])
        diff = numpy.diff(arr)
        print(diff)
        # 2年以上の差がある場合は該当年数分週数(=52)を加算する
        if int(diff[0]) >=2:
            week += 52*(int(diff[0]-1) )               
    
    return week

test2 = resultDay()
print(test2)

# str = input()
# print(str)

# def test(a, b):
#     c = "yes"
#     if not a == b:
#         c="no"
#     print(c)

#     arr = numpy.array([1, 3])
#     diff = numpy.diff(arr)
#     print(int(diff[0]), str(diff[0]))

# test1 = test(1,1)