import sqlite3
from pathlib import Path

class TaskManager:
    def __init__(self):
        self.FILE = sqlite3.connect("tasks.db")
        self.path = Path('tasks.db')

        self.c = self.FILE.cursor()
        self.c.execute("""CREATE TABLE IF NOT EXISTS tasks (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    task text,
                    done INTEGER
                )""")
    def show_tasks(self):
        self.c.execute("SELECT * FROM tasks")
        items = self.c.fetchall()
        for i, el in enumerate(items, start=1):
            status = "✔" if el[2] else "✘"
            print(f"{i}. {el[1]} [{status}]")

    def add_task(self):
        user_task = input("Введіть ваше завдання: ").strip()
        self.c.execute("INSERT INTO tasks (task, done) VALUES (?, ?) ",
                       (user_task, 0))
        self.FILE.commit()

    def del_task(self):
        try:
            self.c.execute("SELECT * FROM tasks")
            items = self.c.fetchall()
            for el in items:
                print(el)
            n = int(input("Введіть номер завдання для видалення: "))
            self.c.execute("DELETE FROM tasks WHERE id = ?", (n,))
            print("Ваше завдання видалено!")
        except (ValueError, IndexError):
            print("Ви вийшли за межі, або ввели не число")
        self.FILE.commit()


    def done_task(self):
        try:
            self.c.execute("SELECT * FROM tasks")
            items = self.c.fetchall()
            for el in items:
                print(el)
            n = int(input("Введіть номер завдання для відмітки: "))
            self.c.execute(f"UPDATE tasks SET done = 1 WHERE id = ?", (n,))
            self.FILE.commit()

        except (ValueError, IndexError):
            print("Ви вийшли за межі, або ввели не число")

    def show_pending(self):
        self.c.execute("SELECT * FROM tasks WHERE done = 0")
        items = self.c.fetchall()
        for el in items:
            print(el)

    def clear_done(self):
        self.c.execute("DELETE FROM tasks WHERE done = 1")
        items = self.c.fetchall()
        for el in items:
            print(el)

        self.FILE.commit()


def main():
    manager = TaskManager()
    print("Ви у менеджері задач!")
    while True:
        print("\nОсь список доступних дій: ")
        print("1 - показати задачі")
        print("2 - додати задачу")
        print("3 - видалити задачу")
        print("4 - позначити задачу як виконану")
        print("5 - показати невиконані задачі")
        print("6 - очистити виконані задачі")
        print("0 - вийти")
        choice = input("Введіть номер дії: ")
        if choice not in ('0', '1', '2', '3', '4', '5', '6'):
            print("Помилка: інших дій немає")
        elif choice == '1':
            manager.show_tasks()
        elif choice == '2':
            manager.add_task()
        elif choice == '3':
            manager.del_task()
        elif choice == '4':
            manager.done_task()
        elif choice == '5':
            manager.show_pending()
        elif choice == '6':
            manager.clear_done()
        else:
            break

if __name__ == "__main__":
    main()