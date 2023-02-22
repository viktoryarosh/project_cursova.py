import random
import pyjokes
from art import text2art
from prettytable import PrettyTable
from colorama import Fore, Style


def recommend_movie():
    genres = ["екшн", "комедія", "драма", "жахи",]
    movies = {
        "екшн": ["Темний лицар", "Міцний горішок", "Початок", "Термінатор 2: Судний день", "Божевільний Макс: Дорога гніву"],
        "комедія": ["Літак!", "Великий Лебовскі", "Подружки нареченої", "Суперпоганий", "Це спинальний кран"],
        "драма": ["Втеча з Шоушенка", "Хрещений батько", "Список Шиндлера", "Форрест Гамп", "Мовчання ягнят"],
        "жахи": ["Сяйво", "Геть", "Спадковий", "Екзорцист", "Психо"]
    }

    genre = random.choice(genres)
    movie = random.choice(movies[genre])
    return f"{movie} ({genre})"


def recommend_music():
    genres = ["рок", "поп", "хіп-хоп", "електронна"]
    music = {
        "рок": ["Queen", "Led Zeppelin", "AC/DC", "Pink Floyd", "Nirvana"],
        "поп": ["Madonna", "Michael Jackson", "Whitney Houston", "Katy Perry", "Ariana Grande"],
        "хіп-хоп": ["Tupac", "Eminem", "Jay-Z", "Kendrick Lamar", "Notorious B.I.G."],
        "електронна": ["Daft Punk", "The Chemical Brothers", "Armin van Buuren", "Skrillex", "Deadmau5"]
    }
    genre = random.choice(genres)
    artist = random.choice(music[genre])
    return f"{artist} ({genre})"

def recommend_game():
    genres = ["стратегія", "рольова гра", "екшн", "пригоди"]
    games = {
        "стратегія": ["Civilization VI", "StarCraft II", "XCOM 2", "Europa Universalis IV", "Total War: Warhammer II"],
        "рольова гра": ["The Elder Scrolls V: Skyrim", "Fallout: New Vegas", "Divinity: Original Sin 2", "Mass Effect 2", "Witcher 3"],
        "екшн": ["Grand Theft Auto V", "Doom (2016)", "Dark Souls III", "Metal Gear Solid V: The Phantom Pain", "Max Payne 3"],
        "пригоди": ["Uncharted 4: A Thief's End", "The Last of Us Part II", "Life is Strange", "Gone Home", "Firewatch"]
    }
    genre = random.choice(genres)
    game = random.choice(games[genre])
    return f"{game} ({genre})"

def tell_joke():
    return pyjokes.get_joke()

def tell_story():
    stories = ["В 1969 році Ніл Армстронг став першим людиною, що крокнула на Місяць.",
               "Піраміди в Єгипті були збудовані приблизно в 2500 році до нашої ери.",
               "У 1903 році брати Райт здійснили перший керований польот людини.",
               "Гідроген - найбільш поширений елемент у Всесвіті.",
               "Жаба може прожити до 9 років в неволі."]
    return random.choice(stories)

def play_rps():
    print("Давайте зіграємо в гру камінь-ножиці-бумага!")
    user_choice = input("Виберіть камінь, ножиці або бумага:")
    computer_choice = random.choice(["камінь", "ножиці", "бумага"])
    print(f"Ви вибрали {user_choice}, а комп'ютер вибрав {computer_choice}.")

    if user_choice == computer_choice:
        print("Нічия!")
    elif user_choice == "камінь" and computer_choice == "ножиці" or \
            user_choice == "ножиці" and computer_choice == "бумага" or \
            user_choice == "бумага" and computer_choice == "камінь":
        print("Ви виграли!")
    else:
        print("Комп'ютер виграв.")


def main():
    print(Fore.YELLOW + text2art("Entertaining chat bot"))
    print("Привіт! Я Розважальний чат-бот і я можу порекомендувати вам фільми, музику, ігри, а також розповісти анекдоти та цікаві історії.")

    # Створюємо таблицю для вибору дії користувача
    options_table = PrettyTable()
    options_table.field_names = ["Варіант", "Опис"]
    options_table.add_row(["1.Фільм", "Порекомендувати фільм для перегляду"])
    options_table.add_row(["2.Музика", "Порекомендувати музику для прослуховування"])
    options_table.add_row(["3.Ігри", "Порекомендувати гру для гри"])
    options_table.add_row(["4.Анекдот", "Розповісти випадковий анекдот"])
    options_table.add_row(["5.Історія", "Розповісти цікаву історію"])
    options_table.add_row(["6.КНБ", "Грати в гру камінь-ножиці-бумага"])
    options_table.add_row(["7.Вихід", "Вийти з програми"])
    print(options_table)

    while True:
        user_input = input("Що б ви хотіли зробити? Введіть відповідний номер варіанту: ")
        if user_input == "1":
            print(f"Я рекомендую вам подивитися фільм '{recommend_movie()}'.")
        elif user_input == "2":
            print(f"Я рекомендую вам послухати музику від {recommend_music()}.")
        elif user_input == "3":
            print(f"Я рекомендую вам спробувати гру '{recommend_game()}'.")
        elif user_input == "4":
            print(tell_joke())
        elif user_input == "5":
            print(tell_story())
        elif user_input == "6":
            play_rps()
        elif user_input == "7":
            print(Fore.GREEN + "До побачення!")
            break
        else:
            print(
                Fore.RED + "На жаль, я не розумію вашого запиту. Будь ласка, введіть відповідний номер варіанту ще раз.")
        print(Style.RESET_ALL)

if __name__ == "__main__":
    main()