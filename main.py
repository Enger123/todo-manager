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
        if len(items) == 0:
            print("\nЗадач немає.")
        else:
            for el in items:
                status = "✔" if el[2] else "✘"
                print(f"ID: {el[0]} | {el[1]} [{status}]")

    def add_task(self):
        user_task = input("Введіть ваше завдання: ").strip()
        self.c.execute("INSERT INTO tasks (task, done) VALUES (?, ?) ",
                       (user_task, 0))
        self.FILE.commit()
        print("\nЗадачу додано.")

    def del_task(self):
        self.c.execute("SELECT * FROM tasks")
        items = self.c.fetchall()
        for el in items:
            status = "✔" if el[2] else "✘"
            print(f"ID: {el[0]} | {el[1]} [{status}]")
        n = input("Введіть номер завдання для видалення: ")
        if not n.isdigit():
            print("Введіть число")
            return
        n = int(n)
        self.c.execute("DELETE FROM tasks WHERE id = ?", (n,))
        if self.c.rowcount == 0:
            print("\nЗадача не знайдена")
        else:
            print("\nЗавдання видалено")
        self.FILE.commit()


    def done_task(self):
        self.c.execute("SELECT * FROM tasks")
        items = self.c.fetchall()
        for el in items:
            status = "✔" if el[2] else "✘"
            print(f"ID: {el[0]} | {el[1]} [{status}]")
        n = input("Введіть номер завдання для відмітки: ")
        if not n.isdigit():
            print("Введіть число")
            return
        n = int(n)
        self.c.execute("UPDATE tasks SET done = 1 WHERE id = ?", (n,))
        if self.c.rowcount == 0:
            print("\nЗадача не знайдена")
        else:
            print("\nЗавдання позначене як виконане")
        self.FILE.commit()


    def show_pending(self):
        self.c.execute("SELECT * FROM tasks WHERE done = 0")
        items = self.c.fetchall()
        for el in items:
            status = "✔" if el[2] else "✘"
            print(f"ID: {el[0]} | {el[1]} [{status}]")

    def clear_done(self):
        self.c.execute("DELETE FROM tasks WHERE done = 1")
        self.FILE.commit()

    def show_done_tasks(self):
        self.c.execute("SELECT * FROM tasks WHERE done = 1")
        items = self.c.fetchall()
        for el in items:
            status = "✔"
            print(f"ID: {el[0]} | {el[1]} [{status}]")

    def edit_task(self):
        self.c.execute("SELECT * FROM tasks")
        items = self.c.fetchall()
        for el in items:
            status = "✔" if el[2] else "✘"
            print(f"ID: {el[0]} | {el[1]} [{status}]")
        id_to_edit = int(input("Введіть id для редагування: "))
        task_to_edit = input("Введіть нове питання: ").strip()
        self.c.execute("UPDATE tasks SET task = ? WHERE id = ?", (task_to_edit, id_to_edit))
        if self.c.rowcount == 0:
            print("\nЗадача не знайдена")
        else:
            print("\nЗавдання змінено на нове")
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
        print("7 - показати тільки виконані задачі")
        print("8 - редагувати завдання")
        print("0 - вийти")
        choice = input("Введіть номер дії: ")
        if choice not in ('0', '1', '2', '3', '4', '5', '6', '7', '8'):
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
        elif choice == '7':
            manager.show_done_tasks()
        elif choice == '8':
            manager.edit_task()

        else:
            break

if __name__ == "__main__":
    main()