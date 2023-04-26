class Vacancy():
    ''' Класс для работы и хранения данных о вакансии'''

    def __init__(self, data: dict):
        self.__id_vac = data['id_vac']
        self.__name = data['name']
        self.__salary = data['salary']
        self.__id_emp = data['id_emp ']
        self.__emp_name = data['emp_name']
        self.__url = data['url']

    def __repr__(self):
        return f'Название вакансии: {self.__name} \n Ссылка на вакансию: {self.__url} \n Работадатель: {self.__emp_name} \n Зарплата: {self.__salary} \n id вакансии: {self.__id_vac}\n id работадателя: {self.__id_emp}'

