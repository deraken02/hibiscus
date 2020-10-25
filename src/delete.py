import decode as d

class delete:
    """
    The class who decode the password
    """
    def __init__(self,pin,name,wfor='',code='',id=''):
        """
        :param pin: (int) the pin code
        :param name: (str) the name of site or application
        :param wfor: (str) the site optionnal
        """
        self.id=id
        self.code=code
        self.pin=pin
        self.file=name
        self.wfor=wfor.upper()
        self.res=''
    
    def deleter(self):
        """
        The function who delete the item
        """
        a=d.decode(self.pin,self.file,self.wfor)
        a.decode()
        return a.getres()
