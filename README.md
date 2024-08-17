# **ОТДЫХАЙТЕ**

Project topic: Determining the sentiment of reviews of banks

It was necessary to create a machine learning model to determine the sentiment of text reviews of banks. Texts of reviews in Russian. The tone of the reviews can be positive or negative.

Dataset
The data includes reviews of the work of various banks collected from the website banki.ru. Each review has a sentiment label:

Positive - Review is positive
Negative - Negative review
Data format: csv file, tab delimited. Two columns:

Score - class label, positive or negative review.
Text - review text.

Example data:
Positive:

I am served on Tsvetnoy Boulevard. The product is a credit card. Everything is clear and precise. Competent call center workers - keep it up. I have been a client for 3 years now. I’m very pleased - well done! Last year there was a month and a half delay in payments, I spent the entire limit - the finances were difficult. situation and job change. No one bothered with calls - they called once, in a VERY TACTICAL AND POLITE manner, they reminded us about the overdue payment, and asked when it would be possible to pay off the debt. Answered - in 3 weeks. Everything is OK, we are waiting. NOT ONE more call. There was a problem with payment via the Internet. I called. They replied that this resource was blocked and the operation was canceled by the bank. I asked to unblock it - everything was resolved within 10 minutes. Polite operators. I caught myself that when I call the call center, I call people who will help solve my problem, and not with negativity and the desire to swear in advance, like some other banking institutions. In general, thank you for the good service and competent specialists!


Negative:

No hidden fees, the bank is good. Only after processing the loan does it become clear that for some reason they insured you, although I didn’t ask, and she didn’t say that we would insure you for 1,135 rubles. They also gave me stickers and said it was a gift. You put this sticker on your passport, they say, and if you lose it, everything will be okay, or we’ll return your passport, or 1000 rubles. Well, this gift cost me 1000 rubles. Next SMS informer 294 rub. I bought a PS3 from M-Video Nizhnekamsk. All these figures must be announced before applying for a loan. Administrator: Please specify the date the loan was issued. 9v3: I already closed the loan, and took it out on 10/09/13.

Metrics
Accuracy (proportion of correct answers) is used as a metric.

Accuracy=C/N

, Where

C – number of correctly classified objects.
N – total number of objects.
The score for the task is calculated using the formula:
Points = 400 * max(0, (Accuracy * 2 - 1))


, Where
Points – number of points.
Accuracy – percentage of correct answers.
max – used to prevent negative scores if the solution gives a metric < 0.5.
Thus, if the Accuracy metric value is < 0.5, 0 points will be awarded for the task.
And metric values ​​in the range 0.5 ≤ Accuracy < 1.0 are proportionally converted into points from 0.0 to 400.0

Data
train.csv
test.csv
sample_submission.csv
they forged their data, which was stolen from the same site

Project goal:
Development of a system for automatically determining the sentiment of reviews of banks, which will be able to analyze the texts of customer reviews and classify them as positive or negative.
Tasks:
 1. Data collection: Collection of a large volume of reviews about various banks from the online platform (Bank.ru).
 2. Pre-processing of data: Cleaning review texts from unnecessary information (Replace commas with tabs, remove empty lines, remove <...> and <...>, make each review in one line, make 1,2 - negative, 3 - delete, 4 ,5 - positive, remove duplicate reviews).
 3. Data annotation: Creating a labeled sample, where each review is assigned a sentiment label (positive, negative).
 4. Model development: Train a machine learning model to classify reviews by sentiment. Consideration of various algorithms such as linear and logistic regression,
 5. Assessing the quality of the model: Conducting experiments and evaluating the model based on metrics such as accuracy, recall, F1-measure. Optimizing parameters to improve prediction accuracy.
 6. Model integration: Development of an interface or API to integrate the model into a real system, which will be used by banks to analyze customer feedback.
 7. Visualization of results: Creation of dashboards to visualize analytics on reviews, including the distribution of sentiments, identifying key problems and positive aspects.
Expected results:
 • Increasing the efficiency of bank customer service departments through automatic analysis of reviews.
 • Improving the quality of customer service through timely response to negative reviews.
 • Identification of general trends and problem areas in the work of banks based on an analysis of the sentiment of reviews.
Technologies and tools:
 • Programming languages: Python
 • Files: inpynb, py, csv, txt, json, pkl
 • Libraries: numpy, pandas, seaborn, matplotlib, sklearn.model_selection, nltk.corpus, nltk.stem, rank_bm25, sklearn.linear_model, sklearn.metrics, matplotlib.pyplot, joblib, LogisticRegression
 • Platforms for data collection: Banki.ru
 • Tables: csv, json
 • Table types: id, title, userName, text, grade, commentCount, isCountable, dateCreate, resolutionIsApproved, agentAnswerText, agentId, company, hasDocuments, idx, Score, text
Risks and limitations:
 • Possibility of obtaining biased or biased data due to artificially created reviews.
 • Difficulties in determining tonality for complex and ambiguous texts.
 • The need for constant updating of the model to adapt to new trends in language and changing style of reviews
Avoiding Risks:
 • Train the model on real data
 • Process optimization
 • Maintaining the project indefinitely
-------------------------------------------------
Тема проекта: Определение тональности отзывов на банки

Было необходимо создать модель машинного обучения для определения тональности текстов отзывов на банки. Тексты отзывов на русском языке. Тональность отзывов может быть положительной или отрицательной.

Набор данных
Данные включают отзывы о работе различных банков, собранные с сайта banki.ru. Для каждого отзыва есть метка тональности:

Positive - Отзыв положительный
Negative - Отзыв отрицательный
Формат данных: файл csv, разделитель табуляция. Два столбца:

Score - метка класса, положительный или отрицательный отзыв.
Text - текст отзыва.
 
Пример данных:
Positive:

Обслуживаюсь на Цветном Бульваре. Продукт - кредитная карта. Все ясно и четко. Грамотные работники колл-центра - так держать. Являюсь клиентом уже 3-й год. Очень доволен - молодцы!В прошлом году была просрочка по платежам месяца полтора, истратил весь лимит - была сложная фин. ситуация и смена работы. Никто не парил мозг звонками - позвонили один раз, в ОЧЕНЬ ТАКТИЧНОЙ И ВЕЖЛИВОЙ форме напомнили о просрочке, спросили, когда БУДЕТ ВОЗМОЖНОСТЬ погасить задолженность. Ответил - через 3 недели. Все ОК, ждем. Больше НИ ОДНОГО звонка.Была проблема с оплатой через интернет. Позвонил. Ответили, что данный ресурс заблокирован и операция отменена банком. Попросил разблокировать - все решили в течение 10 минут. Вежливые операционисты. Поймал себя на том, что когда звоню в колл-центр, то звоню к людям, которые помогут решить мою проблему, а не с негативом и желанием ругаться уже заранее, как в некоторые другие банковские заведения.В общем, спасибо за хороший сервис и грамотных специалистов!


Negative:

Никаких скрытых комиссий, банк ништяк. Только после оформления кредита выясняется, что зачем-то застраховали тебя, хотя я и не просил, и она не говорила, что будем Вас страховать на 1135 руб. Ещё дали наклейки сказали, что подарок. Наклеишь, мол, на паспорт эту наклейку и в случае утери всё будет окей, или вернём паспорт, или 1000 рублей. Ну вот этот подарок обошёлся мне в 1000 руб. Дальше СМС-информатор 294 руб. Брал PS3 в М-Видео Нижнекамск. Все эти цифры должны быть озвучены до оформления кредита. Администратор: Уточните, пожалуйста, дату оформления кредита. 9v3: Закрыл я уже кредит, а брал 09.10.13.

Метрика
В качестве метрики используется Accuracy (доля правильных ответов).

Accuracy = C / N

, где

С – количество правильно классифицированных объектов.
N – общее количество объектов.
Балл за задачу рассчитывается по формуле:
Points = 400 * max(0, (Accuracy * 2 - 1))


, где
Points – количество баллов.
Accuracy – доля правильных ответов.
max – используется для того, чтобы не допустить отрицательных баллов, если решение дает метрику < 0.5.
Таким образом, при значении метрики Accuracy < 0.5, за задачу будет начислено 0 баллов.
А значения метрики в диапазоне 0.5 ≤  Accuracy < 1.0 пропорционально преобразуются в баллы от 0.0 до 400.0 

Данные
train.csv
test.csv
sample_submission.csv
сфоормирофали и свои данные, которые были запаршены из того же сайта

Цель проекта:
Разработка системы для автоматического определения тональности отзывов на банки, которая будет способна анализировать тексты отзывов клиентов и классифицировать их как положительные или отрицательные.
Задачи:
    1. Сбор данных: Сбор большого объема отзывов о различных банках с онлайн-платформы (Банк.ру).
    2. Пред обработка данных: Очистка текстов отзывов от лишней информации (Заменить запятые на табуляцию, удалить пустые строки, удалить <…> и <…>, сделать каждый отзыв в одну строку, сделать 1,2 — negative, 3 — удалить, 4,5 — positive, удалить повторяющие отзывы).
    3. Аннотирование данных: Создание размеченной выборки, где каждому отзыву присваивается метка тональности (положительная(positive), отрицательная(negative)).
    4. Разработка модели: Обучение модели машинного обучения для классификации отзывов по тональности. Рассмотрение различных алгоритмов, таких как линейная и логистическая регрессия, 
    5. Оценка качества модели: Проведение экспериментов и оценка модели по метрикам, таким как точность, полнота, F1-мера. Оптимизация параметров для повышения точности предсказаний.
    6. Интеграция модели: Разработка интерфейса или API для интеграции модели в реальную систему, которая будет использоваться банками для анализа отзывов клиентов.
    7. Визуализация результатов: Создание дашбордов для визуализации аналитики по отзывам, включая распределение тональностей, выявление ключевых проблем и положительных сторон.
Ожидаемые результаты:
    • Повышение эффективности работы отделов клиентского сервиса банков за счет автоматического анализа отзывов.
    • Улучшение качества обслуживания клиентов, благодаря своевременной реакции на негативные отзывы.
    • Выявление общих тенденций и проблемных зон в работе банков на основе анализа тональности отзывов.
Технологии и инструменты:
    • Языки программирования: Python
    • Файлы: inpynb, py, csv, txt, json, pkl
    • Библиотеки: numpy, pandas, seaborn, matplotlib,  sklearn.model_selection, nltk.corpus, nltk.stem, rank_bm25, sklearn.linear_model, sklearn.metrics, matplotlib.pyplot, joblib, LogisticRegression
    • Платформы для сбора данных: Банки.ру 
    • Таблицы: csv, json
    • Вид таблиц: id, title, userName, text, grade, commentCount, isCountable, dateCreate, resolutionIsApproved, agentAnswerText, agentId, company, hasDocuments, idx, Score, text
Риски и ограничения:
    • Возможность получения необъективных или предвзятых данных из-за искусственно созданных отзывов.
    • Трудности в определении тональности для сложных и неоднозначных текстов.
    • Потребность в постоянном обновлении модели для адаптации к новым трендам в языке и изменению стиля отзывов
Обход рисков: 
    • Обучить модель на реальных данных
    • Оптимизация процесса 
    • Поддержания проекта в течении неопределенного времени
