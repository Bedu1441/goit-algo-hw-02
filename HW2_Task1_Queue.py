from queue import Queue
import time
from datetime import datetime


# Створюємо чергу заявок
requests_queue = Queue()
request_id = 0  # Рахуємо кількість створених заявок


def generate_request():
    """
    Створюємо нову заявку та додаємо її до черги.
    """
    global request_id
    request_id += 1

    # Формуємо заявку
    new_request = {
        "id": request_id,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

    # Додаємо заявку до черги
    requests_queue.put(new_request)
    print(f"[GENERATE] Створюємо заявку №{new_request['id']} о {new_request['created_at']}")


def process_request():
    """
    Обробляємо заявку з черги, якщо вона не порожня.
    """
    if not requests_queue.empty():
        # Беремо заявку на обробку
        current_request = requests_queue.get()
        print(f"[PROCESS] Обробляємо заявку №{current_request['id']}...")
        
        # Імітуємо час обробки
        time.sleep(1)
        
        print(f"[DONE] Завершуємо обробку заявки №{current_request['id']}.\n")
    else:
        print("[INFO] Черга порожня — немає заявок для обробки.\n")


def main():
    """
    Запускаємо головний цикл програми.
    Створюємо нові заявки та обробляємо їх, поки користувач не завершить роботу.
    """
    print("Система обробки заявок запущена.")
    print("Натисніть Enter, щоб створити й обробити наступну заявку.")
    print("Введіть 'q' для виходу.\n")

    while True:
        user_input = input(">>> ")
        if user_input.lower() == "q":
            print("Завершуємо роботу програми.")
            break

        # Створюємо нову заявку
        generate_request()

        # Обробляємо заявку
        process_request()


if __name__ == "__main__":
    main()
