class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartament): #— метод, принимающий в качестве аргументов улицу, дом и квартиру, и добавляющий в список адресов эти данные в виде кортежа:(<улица>, <дом>, <квартира>)
        self.delivery_data.append((street, house, apartament))
                  
    def get_houses_for_street(self, street):  #— метод, принимающий в качестве аргумента улицу и возвращающий список всех домов на этой улице, в которые требуется доставить письма
        result = [tup[1] for tup in self.delivery_data if street == tup[0]]
        dict_keys = {}.fromkeys(result)
        new_list = list(dict_keys.keys())
        return new_list
    
    def get_flats_for_house(self, street, house): #— метод, принимающий в качестве аргументов улицу и дом и возвращающий список всех квартир в этом доме, в которые требуется доставить письма
        result = [tup[2] for tup in self.delivery_data if street == tup[0] and house == tup[1]]
        dict_keys = {}.fromkeys(result)
        new_list = list(dict_keys.keys())
        return new_list