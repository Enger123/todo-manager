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
        for el in self.tasks:
            print(el)

    def add_task(self):
        user_task = input("Введіть ваше завдання: ").strip().capitalize()
        self.tasks.append({"task": user_task, "done": False})


def main():
    manager = TaskManager()
    print("Ви у менеджері задач!")
    print("Ось список доступних дій: ")
    print("1 - показати задачі")
    print("2 - додати задачу")
    print("3 - видалити задачу")
    print("4 - позначити задачу як виконану")
    print("0 - вийти")
    choice = input("Введіть номер дії: ")
    if choice not in ('0', '1', '2', '3', '4'):
        print("Помилка: інших дій немає")
    elif choice == '1':
        manager.show_tasks()
    elif choice == '2':
        manager.add_task()
        manager.save_file()
    elif choice == '3':
        del_task()
    elif choice == '4':
        done_task()
    else:
        return

if __name__ == "__main__":
    main()