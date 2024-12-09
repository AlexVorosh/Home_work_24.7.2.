from api import PetFriends
from settings import valid_email, valid_password
from settings import not_valid_email, not_valid_password
import os

pf = PetFriends()


def test_add_new_pet_without_photo_with_valid_data(name='Саймон', animal_type='Канарейка',
                                     age='6'):
    """Проверяем что можно добавить питомца без фото с корректными данными"""

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_add_photo_of_pet_with_valid_data(pet_photo='images/enot.jpg'):

    """Проверяем возможность добавления фото к имеющемуся питомцу"""

    #Получаем ключ, получаем список своих питомцев, указываем полный путь к файлу с картинкой.

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    pet_id = my_pets['pets'][0]['id']

    #Проверяем - список своих питомцев, если не пустой - добавляем фото питомцу:

    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, pet_id, pet_photo)

    #Проверяем список своих питомцев:

        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
    else:
        raise Exception('У вас пока нет питомцев!')


def test_get_api_key_for_not_valid_email(email=not_valid_email, password=valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и результат не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result


def test_get_api_key_for_not_valid_password(email=valid_email, password=not_valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и результат не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result


def test_get_api_key_for_not_valid_user(email=not_valid_email, password=not_valid_password):
    """ Проверяем что запрос api ключа не возвращает статус 200 и результат не содержится слово key"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status != 200
    assert 'key' not in result


def test_add_new_pet_without_name(name='', animal_type='собака', age='9', pet_photo='images/dog.jpeg'):
    """Проверяем что не возможно добавить питомца с пустым полем name"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['name'] != name


def test_add_new_pet_without_animal_type(name='Дружок', animal_type='', age='2', pet_photo='images/rabbit.jpg'):
    """Проверяем что не возможно добавить питомца с пустым полем animal_type"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['animal_type'] != animal_type


def test_add_new_pet_without_age(name='Дружок', animal_type='', age='', pet_photo='images/rabbit.jpg'):
    """Проверяем что не возможно добавить питомца с пустым полем age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['age'] != age


def test_add_new_pet_with_negative_age(name='Мурзик', animal_type='тигр', age='-5', pet_photo='images/tiger.jpg'):
    """Проверяем что не возможно добавить питомца с отрицательным значением в полем age"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['age'] != age


def test_add_new_pet_with_not_valid_photo(name='Барсик', animal_type='барсук',
                                     age='3', pet_photo='images/badger.gif'):
    """Проверяем что не возможно добавить питомца с некорректным фото формата GIF"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status != 200
    assert result['pet_photo'] == pet_photo



