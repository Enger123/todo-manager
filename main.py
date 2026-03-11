import os
import json

class TaskManager:
    FILE = "tasks.json"
    def __init__(self):
        self.tasks = self.load_file()
    def load_file(self):
        if os.path.isfile(self.FILE):
            try:
                with open(self.FILE, "r") as file:
                    return json.load(file)
            except (ValueError, json.JSONDecodeError):
                return self.default_tasks()
        else:
            return self.default_tasks()

    def default_tasks(self):
        return [
                {"task": "Купити молоко", "done": False},
                {"task": "Піти погуляти", "done": True}
            ]

    def save_file(self):
        with open(self.FILE, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, indent=4, ensure_ascii=False)

    def show_tasks(self):
        if not self.tasks:
            print("Задач немає")
            return
        for i, task in enumerate(self.tasks, start=1):
            status = "✔" if task["done"] else "✘"
            print(f"{i}. {task['task']} [{status}]")

    def add_task(self):
        user_task = input("Введіть ваше завдання: ").strip()
        self.tasks.append({"task": user_task, "done": False})
        print("Нове завдання додано!")

    def del_task(self):
        try:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            n = int(input("Введіть номер завдання для видалення: "))
            task_to_del = n - 1
            del self.tasks[task_to_del]
            print("Ваше завдання видалено!")
        except (ValueError, IndexError):
            print("Ви вийшли за межі, або ввели не число")

    def done_task(self):
        try:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
            n = int(input("Введіть номер завдання для відмітки: "))
            task_to_true = n - 1
            task = self.tasks[task_to_true]
            if not task["done"]:
                task["done"] = True
                print("Ваше завдання відмічено як виконане!")
            else:
                print("Завдання вже виконане.")
                return

        except (ValueError, IndexError):
            print("Ви вийшли за межі, або ввели не число")

    def show_pending(self):
        for i, task in enumerate(self.tasks, start=1):
            if not task["done"]:
                print(f"{i}. {task['task']}")

    def clear_done(self):
        self.tasks = [task for task in self.tasks if not task['done']]
        print("Виконані завдання очищено")

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
            manager.save_file()
        elif choice == '3':
            manager.del_task()
            manager.save_file()
        elif choice == '4':
            manager.done_task()
            manager.save_file()
        elif choice == '5':
            manager.show_pending()
        elif choice == '6':
            manager.clear_done()
            manager.save_file()
        else:
            break

if __name__ == "__main__":
    main()