from collections import deque


def is_palindrome(text: str) -> bool:
    """
    Перевіряємо, чи є рядок паліндромом.
    Ігноруємо регістр та пробіли.
    """
    # Нормалізуємо рядок: переводимо в нижній регістр та прибираємо пробіли
    normalized = "".join(ch.lower() for ch in text if not ch.isspace())

    # Створюємо дек з символів нормалізованого рядка
    chars = deque(normalized)

    # Поступово порівнюємо символи зліва та справа
    while len(chars) > 1:
        left = chars.popleft()   # Беремо символ зліва
        right = chars.pop()      # Беремо символ справа

        # Порівнюємо символи
        if left != right:
            return False

    # Якщо всі пари збігаються — це паліндром
    return True


def main():
    """
    Запускаємо перевірку паліндромів у консольному режимі.
    """
    print("Перевіряємо рядки на паліндром.")
    print("Вводимо рядок і натискаємо Enter.")
    print("Вводимо 'q', щоб вийти.\n")

    while True:
        text = input("Введіть рядок: ")

        # Перевіряємо, чи користувач хоче завершити роботу
        if text.lower() == "q":
            print("Завершуємо роботу програми.")
            break

        # Викликаємо функцію перевірки паліндрому
        if is_palindrome(text):
            print("✅ Це паліндром.\n")
        else:
            print("❌ Це не паліндром.\n")


if __name__ == "__main__":
    main()
