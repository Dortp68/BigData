# BigData
## Блок 1. Развертывание локального кластера Hadoop
С помощью [docker hadoop](https://github.com/big-data-europe/docker-hadoop) развернул локальный кластер в конфигурации: 1 NN, 2 DN + 2 NM, 1 RM, 1 History server.  Файл [docker-compose](https://github.com/Dortp68/BigData/blob/main/docker-compose%20(1).yml).
### Веб-интерфейс namenode
![](https://github.com/Dortp68/BigData/blob/main/Screenshots/cAZhsTHgo3c.jpg)
![](https://github.com/Dortp68/BigData/blob/main/Screenshots/PJXonAEPm7c.jpg)
### Веб-интерфейс resourcemanager
![](https://github.com/Dortp68/BigData/blob/main/Screenshots/wA4S7OITdP4.jpg)
## Блок 2. Написание map reduce на Python
Используя реализованные скрипты [mapper.py](https://github.com/Dortp68/BigData/blob/main/mapper.py) и [reducer.py](https://github.com/Dortp68/BigData/blob/main/reducer.py) рассчитал среднее значение и дисперсию по признаку "price". Сперва загрузил датасет на hdfs, для запуска mapreduce использовался hadoop streaming:

mapred streaming \
-files mapper.py,reducer.py \
-input /user/input/data.csv \
-output /user/output \
-mapper mean_mapper.py \
-reducer mean_reducer.py

Также среднее и дисперсия была посчитана в [блокноте](https://github.com/Dortp68/BigData/blob/main/Untitled.ipynb).

### Результаты:
python -
mean: 152.75505277800508
variance: 57681.75384084372

mapreduce -
mean: 152.75505277800508
variance: 57680.573868790685
