from pathlib import Path
import re 
from datetime import datetime,date,time
import sys
sys.stdout.reconfigure(encoding='utf-8')
cyber_dir = 'C:/Users/gornl/OneDrive/Рабочий стол/CyberOS'
def get_tasks():
    tasks = []
    section = None
    SKIP = {'🌙 Evening Review', '⚡ Энергия'}
    path = Path(cyber_dir) / '10 Command Center' / 'Daily' / f'{date.today()}.md'
    try:
        with open(path, encoding='utf-8') as f:
            for line in f:
                line = line.rstrip('\n')
                if line.startswith('#'):
                    section = line.lstrip('#').strip()
                    continue
                if section in SKIP:
                    continue
                if line.lstrip().startswith('- [ ]'):
                    tasks.append(line.split(']', 1)[1].strip())
    except FileNotFoundError:
        print('Файла задач на сегодня нет.')
    except OSError as e:
        print(f'Не смог прочитать файл задач: {e}')
    return tasks
def main():
    print("Привет Саш , что хочешь узнать ?")
    while True:
        mission = str.split(str.lower(input('> ')))
        for i in range(len(mission)):
            match mission[i]:
                case 'задания' | "задачи" | "миссии" | "задание" | "миссия":
                    tasks = get_tasks()
                    print("Вот твои задачи на сегодня:")
                    for task in tasks:
                        print(task)
                case 'время':
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Текущее время:", current_time)
                case 'date':
                    today = date.today()
                    print("Сегодняшняя дата:", today)
                case 'выход' | 'exit':
                    print("До свидания!")
                    break
                case _:
                    print("Не понял")
                    continue
            break
if __name__ == "__main__":
    main()