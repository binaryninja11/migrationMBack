from app.schemas import schema


variant1 = {
    "variant_id": 1,
    "body": {
        schema.SectionName.listing: [
            {
                "id":1,
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где они говорят. Выберите правильный ответ.",
                "file_name": "file11.mp3",
                "body": "Они говорят",
                "answers": ["в продуктовом магазине", "в кассе кинотеатра", "в магазине «Игрушки»"]
            },
            {
                "id":2,
                "task_name": "Задание 2",
                "header": "Прослушайте диалог и выберите правильный ответ.",
                "file_name": "file12.mp3",
                "body": "Что сделал Антон?",
                "answers": ["Он не дал мобильный телефон сестре.", "Он потерял мобильный телефон.", "Он дал мобильный телефон сестре."]
            }
        ],
        schema.SectionName.reading: [
            {
                "id":3,
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Уважаемые пассажиры!\nОплачивайте проезд при входе.\n\nТакое объявление можно прочитать",
                "answers": ["в кино", "в автобусе", "в магазине"]
            },
            {
                "id":4,
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Дорогой друг!\nПриглашаю тебя на мой День рождения!\nПраздник будет 19 ноября (в четверг) с 15 до 20 часов.\nЖду тебя в кафе «Уют».",
                "answers": ["в 15 часов", "в 19 часов", "в 20 часов"]
            }
        ],
        schema.SectionName.writing: [
             {
                 "id":5,
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Нариман приехал из Узбекистана. Нариман – врач.\n\nВпишите нужное слово в анкету.\nАнкета \n 1. Как Вас зовут? - Меня зовут Нариман. \n2. Откуда Вы приехали? - Я приехал из Узбекистана. \n 3.Кто Вы по профессии? - Я ____________________",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "id":6,
                "task_name": "Задание 6",
                "body": "Сегодня четверг, а брат приедет завтра, _____________________.",
                "answers": ["в среду", "в пятницу", "в субботу"]
            },
            {
                "id":7,
                "task_name": "Задание 7",
                "body": "Моя сестра _______________ в больнице.",
                "answers": ["живёт", "гуляет", "работает"]
            },
            {
                "id":8,
                "task_name": "Задание 8",
                "body": "– Как тебя зовут\n– _______________ зовут Олег.",
                "answers": ["Мне", "Меня", "Я"]
            },
            {
                "id":9,
                "task_name": "Задание 9",
                "body": "Друг спросил меня: «_______________ ты провёл выходные?»",
                "answers": ["Как", "Почему", "Что"]
            }
        ],
        schema.SectionName.history: [
            {
                "id":10,
                "task_name": "Задание 10",
                "body": "4 ноября в России празднуют?",
                "answers": ["Международный женский день", "День народного единства", "День Победы"]
            },
            {
                "id":11,
                "task_name": "Задание 11",
                "body": "Какой город в России называют «второй столицей»?",
                "answers": ["Екатеринбург", "Владивосток", "Санкт-Петербург"]
            },
            {
                "id":12,
                "task_name": "Задание 12",
                "body": "Союзник СССР в Великой Отечественной войне – это:",
                "answers": ["Япония", "Германия", "Великобритания"]
            },
            {
                "id":13,
                "task_name": "Задание 13",
                "body": "Знаменитый полководец Великой Отечественной войны – это",
                "answers": ["А.В. Суворов", "Г.К. Жуков", "Ю.А. Гагарин"]
            },
            {
                "id":14,
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img11.jpg", "img12.jpg", "img13.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "id":15,
                "task_name": "Задание 15",
                "body": "Что говорит Конституция России о правах иностранцев в России?",
                "answers": ["Иностранцы имеют все права и обязанности как граждане России","Иностранцы имеют права и обязанности, кроме случаев, установленных законом","Иностранцы не имеют прав в России"]
            },
            {
                "id":16,
                "task_name": "Задание 16",
                "body": "В какой форме заключается трудовой договор в России?",
                "answers": ["в письменной", "в устной", "в любой"]
            },
            {
                "id":17,
                "task_name": "Задание 17",
                "body": "Окажут ли срочную медицинскую помощь иностранцу?",
                "answers": ["за плату", "бесплатно", "если есть трудовой договор"]
            },
            {
                "id":18,
                "task_name": "Задание 18",
                "body": "Какую цель нужно указать в миграционной карте для получения патента?",
                "answers": ["отдых", "работа", "частная"]
            },
            {
                "id":19,
                "task_name": "Задание 19",
                "body": "Какой кодекс регулирует правила въезда иностранцев в Россию?",
                "answers": ["Трудовой кодекс", "Кодекс об административных правонарушениях", "Гражданский кодекс"]
            },
            {
                "id":20,
                "task_name": "Задание 20",
                "body": "Если иностранец вовремя не подал на патент, его депортируют. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant2 = {
    "variant_id": 2,
    "body": {
        schema.SectionName.listing: [
            {
                "id":1,
                "task_name": "Задание 1",
                "header": "Прослушайте объявление и определите, где можно его услышать. Выберите правильный ответ.",
                "file_name": "file21.mp3",
                "body": "Объявление можно услышать",
                "answers": ["в ресторане", "в магазине", "в библиотеке"]
            },
            {
                "id":2,
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file22.mp3",
                "body": "Спросите о потерянных вещах",
                "answers": ["у покупателей", "у администратора", "у директора магазина"]
            }
        ],
        schema.SectionName.reading: [
            {
                "id":3,
                "task_name": "Задание 3",
                "header": "Прочитайте киноафишу и выберите правильный ответ.",
                "body": "Осенью смотрите фильм о русском музыканте П.И. Чайковском!\n\nНовый фильм снят",
                "answers": ["о спорте", "о музыке", "о кино"]
            },
            {
                "id":4,
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Рушан. Летом я ездил в Узбекистан к родителям. Я увидел своего брата и его семью. А в конце лета я с женой и детьми\nпоехал на море.\n\nРушан поехал на море",
                "answers": ["с женой и детьми", "с родителями", "с братом"]
            }
        ],
        schema.SectionName.writing: [
            {
                "id":5,
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Анвар Рустамов хочет получить работу плотника.\nВпишите нужное слово в его заявление.\n\nЗаявление\nПрошу принять меня на должность __________",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "id":6,
                "task_name": "Задание 6",
                "body": "В магазине «Продукты» я купил _______________.",
                "answers": ["диван", "куртку", "фрукты"]
            },
            {
                "id":7,
                "task_name": "Задание 7",
                "body": "Мой папа любит _______________ исторические книги.",
                "answers": ["смотреть", "слушать", "читать"]
            },
            {
                "id":8,
                "task_name": "Задание 8",
                "body": "Сколько _______________ лет?",
                "answers": ["Вы", "Вам", "у Вас"]
            },
            {
                "id":9,
                "task_name": "Задание 9",
                "body": "Карим сказал, _______________ он приедет в отпуск весной.",
                "answers": ["что", "потому что", "когда"]
            }
        ],
        schema.SectionName.history: [
            {
                "id":10,
                "task_name": "Задание 10",
                "body": "12 июня в России празднуют",
                "answers": ["День России", "Праздник Весны и Труда", "День защитника Отечества"]
            },
            {
                "id":11,
                "task_name": "Задание 11",
                "body": "Какой из этих городов российский?",
                "answers": ["Будапешт", "Казань", "Братислава"]
            },
            {
                "id":12,
                "task_name": "Задание 12",
                "body": "Кто командовал русской армией в войне 1812 года?",
                "answers": ["Г.К. Жуков", "Дмитрий Донской", "М.И. Кутузов"]
            },
            {
                "id":13,
                "task_name": "Задание 13",
                "body": "Когда было создано СНГ?",
                "answers": ["в 1612 году", "в 1941 году", "в 1991 году"]
            },
            {
                "id":14,
                "task_name": "Задание 14",
                "body": "Укажите герб Российской Федерации.",
                "answers": ["img21.jpg", "img22.jpg", "img23.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "id":15,
                "task_name": "Задание 15",
                "body": "Какое право иностранцу гарантирует Конституция России?",
                "answers": ["голосовать на выборах","выбирать работу","занимать государственные должности"]
            },
            {
                "id":16,
                "task_name": "Задание 16",
                "body": "Как дети иностранцев учатся в России?",
                "answers": ["бесплатно, как и дети граждан России", "только платно", "не имеют права посещать школы и детсады"]
            },
            {
                "id":17,
                "task_name": "Задание 17",
                "body": "Куда обратиться, если ограбили?",
                "answers": ["в полицию", "в суд", "на работу"]
            },
            {
                "id":18,
                "task_name": "Задание 18",
                "body": "Что нужно получить и заполнить при въезде в Россию?",
                "answers": ["заявление на патент", "миграционную карту", "заявление на работу"]
            },
            {
                "id":19,
                "task_name": "Задание 19",
                "body": "Сколько дней у иностранца для подачи документов на патент?",
                "answers": ["30 дней", "20 дней", "10 дней"]
            },
            {
                "id":20,
                "task_name": "Задание 20",
                "body": "Eсли иностранец не уехал после окончания срока пребывания, он нарушает закон. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant3 = {
    "variant_id": 3,
    "body": {
        schema.SectionName.listing: [
            {
                "id":1,
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file31.mp3",
                "body": "Они говорят",
                "answers": ["в магазине", "в автомастерской", "в центре тестирования"]
            },
            {
                "id":2,
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file32.mp3",
                "body": "Вам нужно",
                "answers": ["ехать дальше", "сделать пересадку", "выйти из вагона"]
            }
        ],
        schema.SectionName.reading: [
            {
                "id":3,
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.\n\nСлужебное помещение: вход только для персонала!",
                "body": "Вы можете увидеть это объявление",
                "answers": ["в лифте","в ресторане","в автобусе"]
            },
            {
                "id":4,
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Тимур. Вчера я со своими друзьями ходил на концерт. Концерт был в парке. Нам очень понравилось. После концерта мы\nрешили поужинать в кафе.\n\nВчера Тимур и его друзья были",
                "answers": ["на концерте","в музее","в театре"]
            }
        ],
        schema.SectionName.writing: [
             {
                "id":5,
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Далер приехал из Таджикистана. Далер – кассир.\nВпишите нужное слово в анкету.\n\nАнкета \n1. Как Вас зовут? - Меня зовут Далер. \n 2. Откуда Вы приехали? - Я приехал из Таджикистана. \n 3. Кто Вы по профессии? - Я _______________",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "id":6,
                "task_name": "Задание 6",
                "body": "Я с друзьями поеду в горы _____________, чтобы кататься на лыжах.",
                "answers": ["зимой", "летом", "осенью"]
            },
            {
                "id":7,
                "task_name": "Задание 7",
                "body": "Скажите, пожалуйста, ___________ уже закончили?",
                "answers": ["работа", "рабочие", "работать"]
            },
            {
                "id":8,
                "task_name": "Задание 8",
                "body": "– Откуда ты приехал?\n– Я приехал _______________.",
                "answers": ["в Самарканде", "из Самарканда", "из Самарканд"]
            },
            {
                "id":9,
                "task_name": "Задание 9",
                "body": "Мы приехали в Россию, __________ найти работу.",
                "answers": ["чтобы", "поэтому", "потому что"]
            }
        ],
        schema.SectionName.history: [
            {
                "id":10,
                "task_name": "Задание 10",
                "body": "1 января в России празднуют",
                "answers": ["День России", "Новый год", "Международный женский день"]
            },
            {
                "id":11,
                "task_name": "Задание 11",
                "body": "Город, который является столицей России - __________.",
                "answers": ["Москва", "Екатеринбург", "Самара"]
            },
            {
                "id":12,
                "task_name": "Задание 12",
                "body": "Когда закончилась Великая Отечественная война?",
                "answers": ["в 1917 году", "в 1945 году", "в 1980 году"]
            },
            {
                "id":13,
                "task_name": "Задание 13",
                "body": "СНГ было образовано после",
                "answers": ["распада СССР в 1991 году", "Великой Отечественной войны", "Российской революции 1917 года"]
            },
            {
                "id":14,
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img31.jpg", "img32.jpg", "img33.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "id":15,
                "task_name": "Задание 15",
                "body": "Какое право Конституция РФ гарантирует иностранцам?",
                "answers": ["голосовать на выборах","участвовать в суде","пользоваться родным языком"]
            },
            {
                "id":16,
                "task_name": "Задание 16",
                "body": "Иностранец, работающий в России, должен платить налоги?",
                "answers": ["должен", "не должен", "может"]
            },
            {
                "id":17,
                "task_name": "Задание 17",
                "body": "На территории Российской Федерации в отношении иностранного гражданина совершено преступление. Куда он должен обратиться за помощью?",
                "answers": ["в полицию", "в МИД", "в посольство своей страны"]
            },
            {
                "id":18,
                "task_name": "Задание 18",
                "body": "Что нужно иметь иностранцу для постановки на учет в России?",
                "answers": ["только миграционную карту", "только паспорт", "паспорт и миграционную карту"]
            },
            {
                "id":19,
                "task_name": "Задание 19",
                "body": "Если иностранец нарушил правила учета, какая будет ответственность?",
                "answers": ["дисциплинарная", "уголовная", "административная"]
            },
            {
                "id":20,
                "task_name": "Задание 20",
                "body": "Административное выдворение из России для иностранцев устанавливает судья. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant4 = {
    "variant_id": 4,
    "body": {
        schema.SectionName.listing: [
            {
                "id":1,
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file41.mp3",
                "body": "Они говорят",
                "answers": ["на улице", "на остановке", "в автобусе"]
            },
            {
                "id":2,
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file42.mp3",
                "body": "У администратора магазина можно",
                "answers": ["взять свой потерянный телефон", "купить новый телефон", "позвонить по телефону"]
            }
        ],
        schema.SectionName.reading: [
            {
                "id":3,
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Уважаемые жильцы дома №7!\nЛифт временно не работает!\n\nТакое объявление можно прочитать",
                "answers": ["в аптеке","в подъезде","в парке"]
            },
            {
                "id":4,
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Меня зовут Динара. Я приехала с родителями из Таджикистана. Мой папа инженер, а мама учительница. В будущем я хочу быть доктором.\nДинара хочет быть",
                "answers": ["доктором","учительницей","инженером"]
            }
        ],
        schema.SectionName.writing: [
             {
                "id":5,
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Мадина приехала из Узбекистана. Мадина – швея.\nВпишите нужное слово в анкету.\n\nАнкета  \n1. Как Вас зовут? - Меня зовут Мадина. \n 2. Кто Вы по профессии? - Я швея. \n 3. 2. Откуда Вы приехали? - Я приехала из __________",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "id":6,
                "task_name": "Задание 6",
                "body": "А.С. Пушкин родился летом, _______________.",
                "answers": ["6 июня", "6 апреля", "6 декабря"]
            },
            {
                "id":7,
                "task_name": "Задание 7",
                "body": "В аптеке я купил __________.",
                "answers": ["телефон", "огурцы", "лекарство"]
            },
            {
                "id":8,
                "task_name": "Задание 8",
                "body": "Ты знаешь, _______________ есть брат и сестра?",
                "answers": ["к нему", "у его", "у него"]
            },
            {
                "id":9,
                "task_name": "Задание 9",
                "body": "Я не могу сегодня пойти на работу, _______________ я заболел.",
                "answers": ["чтобы", "потому что", "если"]
            }
        ],
        schema.SectionName.history: [
            {
                "id":10,
                "task_name": "Задание 10",
                "body": "7 января в России празднуют",
                "answers": ["День России", "Международный женский день", "Рождество Христово"]
            },
            {
                "id":11,
                "task_name": "Задание 11",
                "body": "Какой из этих городов находится в России?",
                "answers": ["София", "Владивосток", "Берлин"]
            },
            {
                "id":12,
                "task_name": "Задание 12",
                "body": "Противник России в Отечественной войне 1812 года был:",
                "answers": ["Швеция", "Великобритания", "Франция"]
            },
            {
                "id":13,
                "task_name": "Задание 13",
                "body": "Первый человек, полетевший в космос, был из",
                "answers": ["США", "СССР", "Китая"]
            },
            {
                "id":14,
                "task_name": "Задание 14",
                "body": "Укажите флаг Российской Федерации.",
                "answers": ["img41.jpg", "img42.jpg", "img43.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "id":15,
                "task_name": "Задание 15",
                "body": "Что имеет право делать иностранец в России?",
                "answers": ["быть пилотом гражданского самолета","работать на объектах, связанных с безопасностью","говорить на родном языке"]
            },
            {
                "id":16,
                "task_name": "Задание 16",
                "body": "Где регистрируют брак в России?",
                "answers": ["в суде", "в ЗАГСе", "в полиции"]
            },
            {
                "id":17,
                "task_name": "Задание 17",
                "body": "Потеряли паспорт. Куда обратиться?",
                "answers": ["в полицию и консульство", "в суд", "на работу"]
            },
            {
                "id":18,
                "task_name": "Задание 18",
                "body": "Сколько времени дается для постановки на учет в России?",
                "answers": ["3 рабочих дня", "7 рабочих дней", "10 рабочих дней"]
            },
            {
                "id":19,
                "task_name": "Задание 19",
                "body": "Какой кодекс регулирует наказание за преступление иностранца в России?",
                "answers": ["Уголовный кодекс России", "Уголовный кодекс страны иностранца", "Гражданский кодекс"]
            },
            {
                "id":20,
                "task_name": "Задание 20",
                "body": "Иностранцев с ВИЧ депортируют из России. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}

variant5 = {
    "variant_id": 5,
    "body": {
        schema.SectionName.listing: [
            {
                "id":1,
                "task_name": "Задание 1",
                "header": "Прослушайте диалог и определите, где происходит разговор. Выберите правильный ответ.",
                "file_name": "file51.mp3",
                "body": "Они говорят",
                "answers": ["в кинотеатре", "в магазине", "в гостинице"]
            },
            {
                "id":2,
                "task_name": "Задание 2",
                "header": "Прослушайте объявление и выберите правильный ответ.",
                "file_name": "file52.mp3",
                "body": "Теперь банк будет работать",
                "answers": ["до 9 часов вечера", "как обычно", "до 21 мая"]
            }
        ],
        schema.SectionName.reading: [
            {
                "id":3,
                "task_name": "Задание 3",
                "header": "Прочитайте объявление и выберите правильный ответ.",
                "body": "Технический перерыв 15 минут\n\nВы можете увидеть это объявление",
                "answers": ["в магазине","в самолёте","в парке"]
            },
            {
                "id":4,
                "task_name": "Задание 4",
                "header": "Прочитайте текст и выберите правильный ответ.",
                "body": "Сабине сорок три года. Она приехала с семьей из Узбекистана. Дома она работала поваром. Её муж работает таксистом. Сабина планирует работать в школе поваром.\nКем будет работать Сабина?",
                "answers": ["таксистом","поваром","продавцом"]
            }
        ],
        schema.SectionName.writing: [
            {
                "id":5,
                "task_name": "Задание 5",
                "header": "Прочитайте текст и вставьте пропущенное слово.",
                "body": "Карим Исмаилов хочет получить работу повара.\nВпишите нужное слово в его заявление.\n\nЗаявление\nПрошу принять меня на работу на должность __________",
                "answers": ["___"]
            }
        ],
        schema.SectionName.grammar: [
            {
                "id":6,
                "task_name": "Задание 6",
                "body": "– Автобусная остановка находится здесь?\n– Нет, ___________________.",
                "answers": ["там", "здесь", "тот"]
            },
            {
                "id":7,
                "task_name": "Задание 7",
                "body": "Мой брат работает в ресторане _____________________.",
                "answers": ["продавцом", "курьером", "инженером"]
            },
            {
                "id":8,
                "task_name": "Задание 8",
                "body": "Извините, это ________ телефон?",
                "answers": ["Ваша", "Ваши", "Ваш"]
            },
            {
                "id":9,
                "task_name": "Задание 9",
                "body": "Скажите, пожалуйста, _________ находится аптека?",
                "answers": ["где", "здесь", "там"]
            }
        ],
        schema.SectionName.history: [
            {
                "id":10,
                "task_name": "Задание 10",
                "body": "23 февраля в России празднуют",
                "answers": ["Праздник Весны и Труда", "День защитника Отечества", "День России"]
            },
            {
                "id":11,
                "task_name": "Задание 11",
                "body": "Какой из этих городов в России?",
                "answers": ["София", "Прага", "Новосибирск"]
            },
            {
                "id":12,
                "task_name": "Задание 12",
                "body": "Когда началась Великая Отечественная война?",
                "answers": ["в 1812 году", "в 1917 году", "в 1941 году"]
            },
            {
                "id":13,
                "task_name": "Задание 13",
                "body": "Кто участвовал в создании СНГ?",
                "answers": ["Иван Грозный", "Борис Ельцин", "Дмитрий Пожарский"]
            },
            {
                "id":14,
                "task_name": "Задание 14",
                "body": "Укажите герб Российской Федерации.",
                "answers": ["img41.jpg", "img42.jpg", "img43.jpg"]
            }
        ],
        schema.SectionName.low: [
            {
                "id":15,
                "task_name": "Задание 15",
                "body": "Иностранный гражданин в Российской Федерации имеет право:",
                "answers": ["ознакомиться с документами, касающимися его прав","самостоятельно составлять документы","вносить изменения в документы"]
            },
            {
                "id":16,
                "task_name": "Задание 16",
                "body": "Может ли иностранец купить недвижимость в России?",
                "answers": ["может", "не может", "только с разрешения суда"]
            },
            {
                "id":17,
                "task_name": "Задание 17",
                "body": "Иностранец может жениться в России?",
                "answers": ["да", "да, только на гражданке РФ", "нет"]
            },
            {
                "id":18,
                "task_name": "Задание 18",
                "body": "Если срок пребывания в России сокращен, за сколько дней нужно покинуть страну?",
                "answers": ["90 дней", "30 дней", "3 дня"]
            },
            {
                "id":19,
                "task_name": "Задание 19",
                "body": "Если иностранец нарушил правила учета, какую ответственность он понесет?",
                "answers": ["дисциплинарную", "уголовную", "административную"]
            },
            {
                "id":20,
                "task_name": "Задание 20",
                "body": "Иностранец, не уехавший из России вовремя, будет депортирован. Это верно?",
                "answers": ["верно", "неверно"]
            }
        ]

    }
}


variants = [variant1,variant2,variant3,variant4,variant5]
answers1 = {
    1:2,
    2:3,
    3:2,
    4:1,
    5:"врач",
    6:1,
    7:3,
    8:2,
    9:1,
    10:2,
    11:3,
    12:3,
    13:2,
    14:1,
    15:2,
    16:1,
    17:2,
    18:2,
    19:2,
    20:2
}

answers2 = {
    1:2,
    2:2,
    3:2,
    4:1,
    5:"плотника",
    6:3,
    7:3,
    8:2,
    9:1,
    10:1,
    11:2,
    12:3,
    13:3,
    14:1,
    15:2,
    16:1,
    17:1,
    18:2,
    19:1,
    20:1
}

answers3 = {
    1:3,
    2:3,
    3:2,
    4:1,
    5:"кассир",
    6:1,
    7:2,
    8:2,
    9:1,
    10:2,
    11:1,
    12:2,
    13:1,
    14:1,
    15:3,
    16:1,
    17:1,
    18:3,
    19:3,
    20:1
}

answers4 = {
    1:3,
    2:1,
    3:2,
    4:1,
    5:"Узбекистана",
    6:1,
    7:3,
    8:3,
    9:2,
    10:3,
    11:2,
    12:3,
    13:2,
    14:2,
    15:3,
    16:2,
    17:1,
    18:2,
    19:1,
    20:2
}

answers5 = {
    1:1,
    2:1,
    3:1,
    4:2,
    5:"повара",
    6:1,
    7:2,
    8:3,
    9:1,
    10:2,
    11:3,
    12:3,
    13:2,
    14:2,
    15:1,
    16:1,
    17:1,
    18:3,
    19:3,
    20:1
}

answers = [answers1,answers2,answers3,answers4,answers5]