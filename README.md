Main telegram bot is in app.py

file ".env" contains: TOKEN=Put_Your_Token

Weather parser - Pamail.py (https://pogoda.mail.ru/)

News parser - Paria.py (https://ria.ru/)

Jokes parser - Panek.py (https://anekdoty.ru/pro-programmistov/)

Checking for user in the DB - check.py

File users.db has 5 columns for each user.

![image](https://github.com/Alanyle/studtgbot/assets/162821077/74867d09-1189-46cd-b412-e3494d1a691c)![image](https://github.com/Alanyle/studtgbot/assets/162821077/f9794d35-a5da-438b-a6e4-58a735ad5269)

/start добавляет нового пользователя в бд, /delete удаляет его из бд

![image](https://github.com/Alanyle/studtgbot/assets/162821077/13ea7ca2-2ebc-495e-9c8d-528f720ef024)

/help выводит список команд, 
/weather при имеющемся в бд городе выдаёт погоду в вашем городе, иначе спрашивает город и записывает его в бд, после чего выдаёт погоду

![image](https://github.com/Alanyle/studtgbot/assets/162821077/49a14d5e-22b1-41ef-af8e-e337fe2c01e7)
![image](https://github.com/Alanyle/studtgbot/assets/162821077/7858f4d9-5ca0-40b1-a4ba-574f00265f08)

/settings даёт выбор между настройкой города или категории новостей сохраняя их в базе данных и сразу же выдавая результат

![image](https://github.com/Alanyle/studtgbot/assets/162821077/7f63afb7-419f-4fa8-bc07-c8c508349c7c)
![image](https://github.com/Alanyle/studtgbot/assets/162821077/01428267-d477-4fc9-9357-55a01560b803)

/news даёт выбор между 11 категориями новостей и присылает новости, но при наличии категории в базе данных выдаёт новости сразу

![image](https://github.com/Alanyle/studtgbot/assets/162821077/20e49fc9-6972-4423-8c4b-2b2a56637130)

![image](https://github.com/Alanyle/studtgbot/assets/162821077/04458a78-cafc-471e-94f7-1e43930cad69)

![image](https://github.com/Alanyle/studtgbot/assets/162821077/41d86ea7-97ec-4e19-b3c9-b064e0d5abfe)

/joke выдаёт случайный анекдот с анекдоты.ру

![image](https://github.com/Alanyle/studtgbot/assets/162821077/aab502c5-45b0-45be-8804-5b6902ca6393)
