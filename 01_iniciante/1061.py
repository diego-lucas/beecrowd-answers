import datetime

day_begin = input().split()[-1]
time_begin = input()

day_end = input().split()[-1]
time_end = input()

begin = datetime.datetime.strptime(f"2020-04-{day_begin} {time_begin}", "%Y-%m-%d %H : %M : %S")
end = datetime.datetime.strptime(f"2020-04-{day_end} {time_end}", "%Y-%m-%d %H : %M : %S")

duration = end - begin

days = duration.days
hours = duration.seconds // 3600
minutes = duration.seconds // 60 % 60
seconds = duration.seconds % 3600 % 60

print(f"{days} dia(s)")
print(f"{hours} hora(s)")
print(f"{minutes} minuto(s)")
print(f"{seconds} segundo(s)")
