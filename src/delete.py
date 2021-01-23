import binary_IO
import coding as c

class delete:
    """
    The class who decode the password
    """
    def __init__(self,line,file,pin):
        """
        :param pin: (int) the pin code
        :param name: (str) the name of site or application
        :param wfor: (str) the site optionnal
        """
        self.line=line
        self.file=file
        self.pin=pin
    
    def main(self):
        """
        The main of the class
        """
        listeligne=list()
        with open("../code/"+self.file,"rb") as f:
            filedescriptor=f.readlines()
            for i in filedescriptor:
                listeligne.append([c for c in i])
        w=open("../code/"+self.file,"wb") 
        writer=binary_IO.Writer(stream=w)
        suppr=self.deleter()
        print(suppr)
        for i in listeligne:
            print(i)
            if i not in suppr:
                writer.write_bytes(i)
            
        
    def deleter(self):
        """
        The function who delete the item
        """
        line=self.line
        aencoder=list()
        resultat=list()
        aencoder+=line.split(' identity:')
        aencoder=aencoder[0].split("wfor:")+aencoder[1].split(' password:')
        aencoder.remove('')
        resultat.append(self.encoder(aencoder))
        return resultat
    
    def encoder(self,l):
        """
        encode en utf8
        """
        a=c.coding(self.pin,l[2],l[0],l[1],self.file)
        buff=''
        res=list()
        for i in range(3):
            if i==0:
                ligne=a.getwfor()
            elif i==1:
                ligne=a.getmail()
            else:
                ligne=a.coder()
            for car in range(len(ligne)):
                if car%2==1:
                    res+=a.bytes(buff,ligne[car])
                    buff=''
                else:
                    buff=ligne[car]
            if i!=2:
                res.append(32)
            else :
                res.append(10)
                
        return res
