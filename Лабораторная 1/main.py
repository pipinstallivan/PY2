class Wifi:
    """класс описывает тип данных, которые нужны для подключения к wifi
    Примеры:
        >>> w = Wifi("500", "0")  # инициализация экземпляра класса

    """
    def __init__(self,ssid:str,psw:str):
        """
        Инициализация экземпляра класса
        :param ssid: ssid для подключения к wifi
        :param psw: пароль для подключения к wifi
        """
        if not isinstance(ssid, str):
            raise TypeError("ssid должен быть типа str, применено значение 2")
            self.ssid = "2"
        else:
            self.ssid = ssid
        if not isinstance(psw, str):
            raise TypeError("psw должен быть типа str,применено значение 1")
            self.psw = "1"
        else:
            self.psw = psw
         
    def get_ssid(self)->None:
        """метод печатает текущиий ssid
        Примеры:
        >>> w = Wifi("500", "0")
        >>> w.get_ssid()
        500
        """
        print(self.ssid)
    def get_psw(self)->str:
        """метод печатает текущиий пароль для wifi
        Примеры:
        >>> w = Wifi("500", "0")
        >>> w.get_psw()
        0
        """
        print(self.psw)    

class Fridge:
    """
    Метод описывает класс простых холодильников
    """
    def __init__(self, сapasity:float, temp:float):
        """
        Инициализация экземпляра класса
        Примеры:
        >>> f = Fridge(2,1)  # инициализация экземпляра класса
        """
        self.capasity = 200
        self.temp = 0
    def set_temp(self,new_temp:float)->None:
        """
        Метод обновляет текущую температуру экземпляра класса

        :param new_temp: Новая температура в холодильнике
        Примеры:
        >>> f = Fridge(2,1)  # инициализация экземпляра класса
        >>> f.set_temp(1)
        """
        if not isinstance(new_temp, (int, float)):
            raise TypeError("температура быть типа int или float")
        self.temp = new_temp
    def get_temp(self)->float:
        """
        Метод печатает текущую температуру экземпляра класса
        Примеры:
        >>> f = Fridge(2,1)  # инициализация экземпляра класса
        >>> f.get_temp()
        0
        """
        print(self.temp)
        
class FridgeWiFi(Fridge):#наследование методов от предыдущего(кроме init)
    """
    Класс продвинутых холодильников
    """
    def __init__(self,ssid:str ="0",psw:str ="2"):
        """
        Инициализация экземпляра класса
        :param ssid: ssid для подключения к wifi
        :param psw: пароль для подключения к wifi
        Примеры:
        >>> f = FridgeWiFi("2","1")  # инициализация экземпляра класса
        """
        self.wifi = Wifi(ssid,psw)
        #self.capasity = 200
        #self.temp = 0
    def connect_to_router(self,ssid:str,psw:str)->None:
        """
        Метод печатает сообщение о присоединениеи к сети wifi
        и обновляет записи
        :param ssid: Новый ssid для подключения к wifi
        :param psw: Новый пароль для подключения к wifi
        Примеры:
        >>> f = FridgeWiFi("2","1")  # инициализация экземпляра класса
        >>> f.connect_to_router("1","2")
        try connect to router
        """
        self.wifi.ssid = ssid
        self.wifi.psw = psw
        print('try connect to router')
    def disconnect_wifi(self)->None:
        """
        Метод печатает сообщение о присоединениеи к сети wifi
        Примеры:
        >>> f = FridgeWiFi()  # инициализация экземпляра класса
        >>> f.disconnect_wifi()
        disconnect from router
        """
        print('disconnect from router')
##fr = FridgeWiFi("2","1")
##fr.connect_to_router("1","2")
##fr.wifi.get_ssid()

import doctest
if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
