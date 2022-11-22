# Directory Protection Tool for Linux
## By ProsecShane

_(На русском языке ниже)_

This program allows you to lock certain files in a directory from editing, viewing and even executing.
Made in Python and Shell using bcrypt.

## Installation

- Install [Python 3][pyinstall] on your PC.
- Check if Python 3 has been installed correctly by typing this into the command prompt or terminal:
```sh
python --version
```
or
```sh
python3 --version
```
- Install the bcrypt library. Wait until it fully installs.
```sh
pip install bcrypt
```
or
```sh
pip3 install bcrpyt
```
- Clone this git repo (or install it's contents) and get ready to use it!

## Usage

- Supports only UTF-8 encoding!
- Please, do NOT rename the file names that are being used by the program.
- Do NOT alter the salt file in the assets folder. Do this only if you know what you are doing.
- Do NOT alter the state file in the assets folder nor the script and the run files in the main folder.
- Set-up the block.tbl like so: the first line contains encrypted password (do NOT alter it, you can change the password through this application), all the lines after that contain file names or file name masks that you need to put restrictions onto.
- Run the shell file through terminal like so:
```sh
./run.sh
```
- You will be prompted to enter the password. The default one is "__itmo_fbit__".
- From there, use the UI as you like. The instructions will come as you use it!

**If you have any questions, you can contact me through _prosecshane@yandex.ru_**

# Защита Папки и Ее Содержимого в Линуксе
## Сделал ProsecShane

Эта программа позволяет вам ограничить доступ к некоторым файлам в папке. Пользователь не сможет редактировать файлы, просматривать их содержимое и даже запускать их.
Сделано в Python и Shell с помощью библиотеки bcrypt.

## Установка

- Установите [Python 3][pyinstall] на ваш компьютер.
- Проверьте, правильно ли установился Python 3. Сделать это можно с помощью команды для командной строки:
```sh
python --version
```
или
```sh
python3 --version
```
- Установите библиотеку bcrypt. Подождите, пока она полностью установится.
```sh
pip install bcrypt
```
или
```sh
pip3 install bcrypt
```
- Склонируйте эту репозиторию (или скачайте её содержимое) и вы можете начинать пользоваться программой!

## Использование

- Поддерживает только кодировку UTF-8!
- Пожалуйста, НЕ переименовывайте файлы, которые используются в работе программы.
- НЕ редактируйте salt-файл в папке assets. Можете редактировать его только если знаете, что вы делаете.
- НЕ редактируйте state-файл в папке assets, script-файл и run-файл в главной папке проекта.
- Вот как должно выглядет содержимое файла block.tbl: первая строка содержит зашифрованный пароль (НЕ изменяйте его, вы можете поменять пароль используя эту программу), каждая линия после этой должна содержать имена или их маски, принадлежащие файлам, которые надо ограничить в доступе.
- Запустите программу следующей командой через командную строку:
```sh
./run.sh
```
- Вас попросят ввести пароль. Пароль по умолчанию установлен как "__itmo_fbit__".
- Дальше вы можете использовать программу так, как вам надо. Инструкции, как ей пользоваться, будут объяснены при ииспользовании!

**Если есть вопросы по работе программы, можете писать мне сюда: _prosecshane@yandex.ru_**

> "Фанклуб Ищенко <3"

[pyinstall]: <https://www.python.org/>