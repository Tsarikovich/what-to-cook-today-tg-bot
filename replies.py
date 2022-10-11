discuss_with = {'eng': ['Omar Khayyam', 'Barack Obama', 'Cristiano Ronaldo',
                        'Lionel Messi', 'Joe Rogan', 'Donald Trump', 'Pavel Durov',
                        'Elon Musk', 'Lil Pump'],
                'ru': ['Омару Хайаму', 'Бараку Обаме', 'Криштиану Роналду',
                       'Лионелю Месси', 'Джо Рогану', 'Дональду Трампу', 'Павлу Дурову',
                       'Илону Маску', 'Лил Пампу']}

calls = {'eng': ['Discussing with {name} about solution on your complicated issue...',
                 "Okay I'm making a call to {name} he probably knows...",
                 "{name} good at predicting i'll text him and ask one sec"],

         'ru': ['Звоню {name}, обсудим твой выбор',
                "Написал сейчас {name}. Думаем..",
                "Спросил у знакомого моего кореша. {name} кажется что это должно быть.."]}

messages_chain = {'eng': {
    'Get': ["Okay, let me look into your meal list 👀",
            "Your list is empty!! Add something cmon man 😾",
            calls['eng'],
            "We decided. Your today's meal should be ",
            "LET'S GO BRUV COOK THAT SHIT!😋😋"],

    'Add': ['Send name of the meal:',
            'Added to your meal list!'],

    'Delete': ["You added no meals bruv", "Choose a meal to delete: ", "No longer in your list bro!"],
    'Show': ["You added no meals bruv", "Your meals: \n"],
    'LangSet': "Let's add a meal!!!!!",
    'Menu': "Menu!",
    '@inmeal': "\'@\' can't be in meal's name"
},
    'ru': {
        'Get': ["Окей, сейчас загляну в твой списочек 👀",
                "Он пуст!! Как я буду выбирать то мужик 😾",
                calls['ru'],
                "Решено! Твое сегодняшнее блюдо ",
                "ПОГНАЛ ПОГНАЛ!😋😋"],

        'Add': ['Напиши название блюда:',
                'Добавил в список!'],

        'Delete': ["Ты ничего не добавил мужик", "Выбери, что удалить: ", "Выкинул из списка!"],
        'Show': ["Ты ничего не добавил бро", "Список твоих блюд: \n"],
        'LangSet': "Здарова бро! Добавь че-нить в менюшку",
        'Menu': "Менюшка для братишки: ",
        '@inmeal': "\'@\' не может  быть в названии блюда"
    }
}
