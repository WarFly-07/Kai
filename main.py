from pathlib import Path
import re 
from datetime import datetime,date,time
import string
import sys
sys.stdout.reconfigure(encoding='utf-8')
cyber_dir = 'C:/Users/gornl/OneDrive/Рабочий стол/CyberOS'
def put_tasks(section,tasks):
    tasks = ''
    path = Path(cyber_dir) / '10 Command Center' / 'Daily' / f'{date.today()}.md'
    try:
        with open(path.read_text(encoding='utf-8').splitlines()) as f:
            for line in f:
                if line.startswith('#'):
                    current_section = line.lstrip('#🔥✅🌱').strip()
                    if section == current_section:
                        tasks += f'- [ ] {tasks}\n'
    except FileNotFoundError:
        print('Файла задач на сегодня нет.')
    except OSError as e:
        print(f'Не смог прочитать файл задач: {e}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')

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
        mission = input('> ').lower().split()
        for word in mission:
            match word:
                case 'задания' | 'задачи' | 'миссии' | 'задание' | 'миссия':
                    tasks = get_tasks()
                    if not tasks:
                        print('На сегодня задач нет.')
                    else:
                        print('Вот твои задачи на сегодня:')
                        for task in tasks:
                            print(task)
                case 'время':
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    print("Текущее время:", current_time)
                case 'время':
                    today = date.today()
                    print("Сегодняшняя дата:", today)
                case 'добавь' | 'запиши' | 'напиши':
                    left, sep, right = mission.partition(':')
                    match left.strip():
                        case 'обязательное' | 'обязаловка' | 'важное':
                            section = 'Обязательно'
                        case 'желательное' | 'желательно' :
                            section = 'Желательно'
                        case 'необязательное' | 'необязаловка' | 'если остается время':
                            section = 'Если остается время'
                        case _:
                            print("Не понял куда добавить задачу")
                            section = string(input("Введи раздел: "))
                            continue
                    if sep:
                        tasks = right.strip()
                        put_tasks(section, tasks)
                    else:
                        print("Не понял что добавить")
                        tasks = string(input("Введи задачу: ")).strip()
                        put_tasks(section, tasks)
                case 'выход' | 'exit':
                    print("До свидания!")
                    return
                case _:
                    continue
            break
        else:
            print("Не понял тебя")
if __name__ == "__main__":
    main()