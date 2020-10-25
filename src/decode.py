import binary_IO
"""
The class to decode
"""
#32-126


class decodeError(Exception):
    '''
    Exception for Binary_IO classes
    '''
    def __init__(self, msg):
        self.message = msg
        
class decode:
    """
    The class who decode the password
    """
    def __init__(self,pin,name,wfor=''):
        """
        :param pin: (int) the pin code
        :param name: (str) the name of site or application
        :param wfor: (str) the site optionnal
        """
        self.pin=pin
        self.name=name
        self.wfor=wfor.upper()
        self.res=''
        
    def getres(self):
        """
        Getter of the result of the search
        """
        return self.res
    
    def setres(self,s):
        """
        Setter of the result of search
        :param s: (str) the string to add
        """
        self.res=self.res+s+'\n'
        
    def reset(self):
        """
        reset the res
        """
        self.res=''
        
    def separation(self):
        """
        Return a tuple of to int who separate the pin
        :return: tuple of to int
        >>> temp=coding(1234,'hey','Amazon')
        >>> temp.seperation()
        (12, 34)
        """
        assert self.pin>100, "Les deux premiers chiffres doivent etre différent de 00xx"
        return (self.pin//100,self.pin%100)
    
    def decode (self):
        """
        The function who decode
        """
        name=self.name
        try:
            file=open("../code/"+name,'rb')
            self.read(file)
        except FileNotFoundError:
            try:
                file=open("../code/"+name+".txt",'rb')
                self.read(file)
            except FileNotFoundError:
                raise decodeError("Le fichier n'existe pas ou n'est pas dans le dossier code")
    
    def read(self,input):
        """
        Read the file of the stream
        """
        reader=binary_IO.Reader(stream=input)
        if self.wfor!='':
            if not self.search(reader):
                raise decodeError("Le code pin ou le nom du site est erroné") 
        else:
            self.printall(reader)
            
    def printall(self,reader):
        """
        Print a the file in clear
        """
        buff=list()
        a=reader.get_bytes(1)
        while a!=list():
            if a==[32]:
                self.printline(self.unsolved(buff),reader)
                buff=list()
            else:
                temp=a+reader.get_bytes(2)
                buff.append(temp)
            a=reader.get_bytes(1)
    
    def search(self,reader): #a modifier pour la nouvelle structure de données
        """
        Search the good site
        :param reader: (IO stream)
        """
        bool=False
        buff=list()
        a=reader.get_bytes(1)
        while a!=list():
            if a==[32]:
                if self.unsolved(buff)=='wfor:'+self.wfor:
                    bool=True
                    self.printline('wfor:'+self.wfor,reader)
                else:
                    while a!=[10]:
                        a=reader.get_bytes(1) #va jusqu'au bout de la ligne
                buff=list()
            else:
                temp=a+reader.get_bytes(2)
                buff.append(temp)
            a=reader.get_bytes(1)
        return bool
    
    def printline(self,wfor,reader):
        """
        print the line
        """
        buff=list()
        res=wfor+' '
        a=reader.get_bytes(1)
        while a!=[10]:
            if a==[32]:
                res+=self.unsolved(buff)
                res+=' '
                buff=list()
            else:
                temp=a+reader.get_bytes(2)
                buff.append(temp)
            a=reader.get_bytes(1)
        res+=self.unsolved(buff,True)
        self.setres(res)
            
    def unsolved(self,line,coding=False):
        """
        Unsolved the string line
        :param line: (list of list)
        """
        key=self.separation()
        res=''
        test=0
        for i in line:
            temp=self.utf8_to_isolatin(i)
            for j in temp:
                if coding and test>8:
                    res+=chr(self.unsolved_letter(key,j))
                else:
                    res+=chr(j)
                    test+=1
        if line[-1][-1]==128:
            res=res[:-1]
        return res
                
    def utf8_to_isolatin(self,l):
        return [((l[0]&15)<<4)+((l[1]>>2)&15),((l[1]&3)<<6)+(l[2]&63)]
        
        
    def unsolved_letter(self,key,a):
        """
        Unsolved the coding
        :param key: (tuple) the key of the coding
        :param a: (int)
        """
        a=(a-key[1])%255
        while a%key[0]!=0:
            a+=255
        return a//key[0]
