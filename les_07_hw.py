class TaskManager:
    def __init__(self):
        """Инициализация менеджера задач"""
        self.__tasks: list[dict] = []

    def add_task(self, title: str, description: str) -> None:
        """Добавляет новую задачу в список"""
        self.__tasks.append({"title": title, "description": description, "done": False})

    def remove_task(self, title: str) -> None:
        """Удаляет задачу по названию"""
        self.__tasks = [task for task in self.__tasks if task['title'] != title]

    def mark_as_done(self, title: str) -> None:
        """Отмечает задачу как выполненную"""
        for task in self.__tasks:
            if task['title'] == title:
                task['done'] = True
                return
        print(f"Задача '{title}' не найдена!")

    def show_tasks(self) -> None:
        """Выводит все текущие задачи"""
        if not self.__tasks:
            print(" Все задачи выполнены! Делать нечего.")
        else:
            for task in self.__tasks:
                status = " Выполнено" if task['done'] else " Не выполнено"
                print(f"Задача: {task['title']}\nОписание: {task['description']}\nСтатус: {status}\n")

    def __str__(self) -> str:
        """Возвращает строковое представление количества задач"""
        return f"Количество задач: {len(self.__tasks)}"


if __name__ == "__main__":
    task_manager = TaskManager()

    # Добавляем задачи
    task_manager.add_task("Сделать ДЗ по школе", "Сделать дз по алгебре и русскому")
    task_manager.add_task("Сделать ДЗ по айти школе", "Сделать проект и загрузить в MyStat")

    # Отмечаем задачу как выполненную
    task_manager.mark_as_done("Сделать ДЗ по школе")

    # Выводим список задач
    task_manager.show_tasks()

    # Удаляем выполненную задачу
    task_manager.remove_task("Сделать ДЗ по школе")

    # Показываем оставшиеся задачи
    task_manager.show_tasks()

    print(f"{task_manager}\nСпасибо за внимание к моему проекту! ")
