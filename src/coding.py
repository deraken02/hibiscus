import binary_IO
"""
Programme d'encodage d'un mdp
"""
class coding:
    """
    The class who coding the password
    
    """
    def __init__(self,pin,code,wfor,mail,file):
        """
        :param pin:(int) the key of the code with 4 int
        :param code:(str) the code to coding
        :param wfor:(str) the target to the mdp
        """
        self.pin=pin
        self.code=code
        self.wfor='wfor:'+wfor.upper()
        self.mail='identity:'+mail
        self.file=file
        
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
    
    def encode(self):
        """
        Encode the code
        :return: (str)
        """
        name=self.file
        file=self.opensource(name)
        self.isolatin_to_utf8(file)
        file.close()
        
    def opensource(self,name):
        """
        Open a file
        :param name: (str) The name of the file
        :return: (stream) The stream of file
        """
        try:
            file=open("../code/"+name, 'ab')
            return file
        except FileNotFoundError:
            file=open("../code/"+name, 'wb')
            return file
        
    def coder(self):
        """
        Code the password
        """
        key=self.separation()
        ncode=''
        for i in self.code:
            ncode+=self.cesar(i,key)
        return 'password:'+ncode
    
    def cesar(self,a,key):
        """
        Code the letter a
        :param a: (str) The letter to encode
        :param key: (tuple) The key of the coding
        :return: (str)
        """
        return chr((ord(a)*key[0]+key[1])%255)
    
    def isolatin_to_utf8(self,outstream):
        """
        Converts the ISO-8859-1 input stream to a UTF-8 output stream
        :param instream: A stream opened with a binary_IO.Reader
        :param outstream: A stream opened with a binary_IO.Writer
        :return: none
        :UC: none
        """
        reader=binary_IO.Writer(stream=outstream)
        self.write(reader,self.wfor)
        reader.write_bytes([32])
        self.write(reader,self.mail)
        
        if len(self.mail)!=0:
            reader.write_bytes([32])
    
        self.write(reader,self.coder())
       
        reader.write_bytes([10])
        reader.close()
    
    def write(self,stream,all):
        """
        Write in the file
        :param stream: An IO stream
        :param all: (str) the str to write in the file
        :return: all
        """
        buff=''
        for i in range(len(all)):
            if i%2==0:
                buff=all[i]
            else:
                stream.write_bytes(self.bytes(buff,all[i]))
                buff=''
        if buff!='':
            stream.write_bytes(self.bytes(buff,chr(0)))
            
    def bytes(self,a,b):
        """
        Take two letters and create a list of bytes
        :param a,b: (str) the letters to tramsform
        :return: (list) list of three bytes
        >>> temp=coding(0000, 'hey', 'Amazon')
        >>> temp.bytes('a','b')
        [230, 133, 162]
        >>>temp.bytes('h','e')
        [230, 161, 165]
        """
        temp=ord(a)
        temp=(temp&(16-1))<<2
        return [224+(ord(a)>>4),128+temp+(ord(b)>>6),128+(ord(b)&63)]