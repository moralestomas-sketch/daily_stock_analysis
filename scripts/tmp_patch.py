import sys

p = ".github/workflows/00-daily-analysis.yml"
with open(p, encoding="utf-8") as f:
    s = f.read()

old1 = "# 定时触发 - 北京时间 09:05 (UTC 01:05)，周二至周六"
new1 = "# 定时触发 - 美股收盘后 30 分钟（UTC 21:30 = 北京时间次日 05:30），周二至周六"
old2 = "- cron: '5 1 * * 2-6'     # 周二到周六，UTC 01:05 = 北京时间 09:05"
new2 = "- cron: '30 21 * * 1-5'     # UTC 周一至周五 21:30 = 北京时间周二至周六 05:30（冬令时收盘后30分钟 / 夏令时收盘后90分钟）"

if s.count(old1) != 1:
    sys.exit("old1 count=%d" % s.count(old1))
if s.count(old2) != 1:
    sys.exit("old2 count=%d" % s.count(old2))

s = s.replace(old1, new1).replace(old2, new2)

if "cron: '30 21 * * 1-5'" not in s:
    sys.exit("cron line not applied")
if "cron: '5 1 * * 2-6'" in s:
    sys.exit("old cron still present")

with open(p, "w", encoding="utf-8", newline="") as f:
    f.write(s)
print("patched ok")
