import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Завантажуємо дані з Excel-файлу
data = pd.read_excel("C:\\ALL\\time_line.xlsx")
data['StartDateTime'] = data['RunDate'] + pd.to_timedelta(data['RunTime'].astype(str))
data['EndDateTime'] = data['StartDateTime'] + pd.to_timedelta(data['RunDuration'], unit='m')

# Сортуємо дані за StartDateTime в порядку зростання
sorted_data = data.sort_values(by='StartDateTime', ascending=True)

# Функція для визначення кольору на основі тривалості
def get_color(duration):
    if duration <= 60:
        return "green"
    elif duration <= 120:
        return "yellow"
    else:
        return "red"

# Побудова вдосконаленої діаграми Ганта з кольорами на основі тривалості
fig, ax = plt.subplots(figsize=(12, len(sorted_data)*0.5))

# Додавання смуг діаграми Ганта з кольорами
for idx, row in sorted_data.iterrows():
    color = get_color(row['RunDuration'])
    ax.barh(row['JobName'], left=row['StartDateTime'], width=row['RunDuration']/1440, align='center', color=color, edgecolor='black')

# Додавання вертикальних ліній кожні 30 хвилин
start_time = sorted_data['StartDateTime'].min()
end_time = sorted_data['EndDateTime'].max()
current_time = start_time
while current_time <= end_time:
    ax.axvline(x=current_time, color='gray', linestyle='--', linewidth=0.5)
    current_time += timedelta(minutes=30)

# Налаштування осі X для відображення дати та часу
ax.xaxis_date()
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

plt.xlabel("Time")
plt.ylabel("Job Name")
plt.title("Gantt Chart")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', which='both', color='gray', linewidth=0.5)
plt.show()
