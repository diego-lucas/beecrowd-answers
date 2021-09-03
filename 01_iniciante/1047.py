import datetime

hour_begin, minute_begin, hour_end, minute_end = map(int, input().split())

begin = datetime.datetime.strptime(f"2020-01-10 {hour_begin}:{minute_begin}", "%Y-%m-%d %H:%M")
end = datetime.datetime.strptime(f"2020-01-10 {hour_end}:{minute_end}", "%Y-%m-%d %H:%M")

if end <= begin:
    end += datetime.timedelta(1)

duration = end - begin
duration_minutes = duration.total_seconds() / 60
duration_hours = duration_minutes // 60
duration_minutes -= duration_hours * 60

print(f"O JOGO DUROU {duration_hours:.0f} HORA(S) E {duration_minutes:.0f} MINUTO(S)")
