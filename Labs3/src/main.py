import os

DATA_FILE = 'data/input_text.txt'
RESULT_FILE = 'data/result.txt'

def load_text(filepath):
    """Загрузка текста из файла с обработкой ошибок."""
    if not os.path.exists(filepath):
        print(f"Ошибка: Файл {filepath} не найден.")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def analyze_text(text, top_n=5):
    """Подсчёт частоты слов с использованием словаря."""
    cleaned_text = ""
    for char in text:
        if char.isalnum() or char.isspace():
            cleaned_text += char.lower()
        else:
            cleaned_text += " "
            
    words = cleaned_text.split()
    word_counts = {}
    
    for word in words:
        if len(word) > 2:  # Игнорируем короткие слова
            word_counts[word] = word_counts.get(word, 0) + 1
            
    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:top_n]

def save_result(results, filepath):
    """Сохранение результатов в файл."""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write("--- Анализ текста ---\n")
            for word, count in results:
                file.write(f"Слово: '{word}' - {count} раз(а)\n")
        print(f"Результат сохранён в {filepath}")
    except Exception as e:
        print(f"Ошибка при сохранении: {e}")

def main():
    while True:
        print("\n--- Анализатор текста ---")
        print("1. Загрузить текст и проанализировать")
        print("2. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            text = load_text(DATA_FILE)
            if text:
                top_words = analyze_text(text)
                if top_words:
                    print("\nТоп слов в тексте:")
                    for word, count in top_words:
                        print(f"- {word}: {count}")
                    save_result(top_words, RESULT_FILE)
                else:
                    print("Текст пуст или не содержит подходящих слов.")
        elif choice == '2':
            print("Выход.")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()
