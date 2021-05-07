DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():
    all_py_devs=[worker["name"] for worker in DATA if worker["language"]=="python" ]
    all_platzi_workers=[worker["name"] for worker in DATA if worker["organization"]=="Platzi"]
    #creamos una variable adults para usar un filter y así traer todos los workers mayores de 18,
    #al hacer esto se obtienen diccionarios con todos los datos de los workers que cumplen la condición
    adults=list(filter(lambda worker: worker["age"]>= 18, DATA))
    #despues como queremos solo el nombre del worker, sobreescribimos la variable adults y usando un map
    #solo nos traemos el nombre
    adults=list(map(lambda worker: worker["name"], DATA))
    #old_workers = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA)) # |-> solo funciona en Python3.9
    #versiones menores a 3.9 y mayores a 3.5
    old_workers = list(map(lambda worker: {**worker, **{"old": worker["age"] > 70}}, DATA)) 
    for worker in all_platzi_workers:
        print(worker)
    for worker in adults:
        print(worker)
    print('-------------')
    for worker in old_workers:
        print(worker)

if __name__=='__main__':
    run()