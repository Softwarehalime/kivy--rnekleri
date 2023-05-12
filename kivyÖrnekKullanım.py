from kivy.app import App 
from kivy.uix.label import Label 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
'''

class Program(App):
    def build (self):
        #self.title = "kivy kütüphamesi"      #piksel olarak yazının buyuklugu ayarlanabilir
        yazi=Label(text= "merhabaaa dunyaaa",font_size = "30sp",color = [1,.5,.9,4])
        return yazi                                               #rgba formatinda deger alır renk için.

'''

#from kivy.uix.button import Button    EKLENMELİ.
'''
class Program(App):

    def build(self):
        dugme = Button(text ="tikla",size_hint = (.1,.1), background_color = [1,1,0,1] , pos = (100,100),)
        dugme.bind(on_press= self.degistir)   #butona tıklandıgında degiştir fonksiyonunu cagırır.
        return dugme
        #disabled = True
        #Butonun aktif olup olmama durumu. True değeri verilirse buton deaktif hale gelecektir.
        #  Bu durumda butona tıklama yapılamaz. Eğer False değeri verilirse buton aktif hale gelecektir

    def degistir(self,nesne): #içine aldıgı nesne bizim butonumuzu belirtir.
        nesne.text= "butona tiklandi"
'''


#from kivy.uix.boxlayout import BoxLayout   diyerek boxLayout fonksiyonunu kodumuza ekliyoruz 
'''
class Program(App):
    def build(self):
        #eger bir deger girilmezse yan yana yazar.
        #duzen = BoxLayout()
        duzen = BoxLayout(orientation = "vertical")   #alt alta yazdirir.
        
        yazi1 = Label(text = "Merhaba")
        yazi2 = Label(text = "Dünya")
        yazi3 = Label(text = "kivy ye hosgeldiniz")

        dugme1 = Button(text ="tikla")
        dugme2 = Button(text ="tikla")
        dugme3 = Button(text ="tikla")

        duzen.add_widget(dugme1)
        duzen.add_widget(dugme2)
        duzen.add_widget(dugme3)
        

       
        duzen.add_widget(yazi1)
        duzen.add_widget(yazi2)
        duzen.add_widget(yazi3)

        #butonlar icinde yapilabilir.
        
       
        return duzen
'''
#from kivy.uix.gridlayout import GridLayout
#gridLayot ızgara seklinde ekrana yazar.
'''
class Program(App):
    def build(self):

        govde = GridLayout(rows = 2)  #rows ilede istedimiz kadar sütun yaptırabiliriz cols
        # Max 2 sütundan oluşmasını istedik
        # 2 sütundan sonra alta kayacaktır

        # Birden fazla buton ekleyerek nasıl göründüğüne bakalım
        # for döngüsü ile ekleyelim
        for i in range(10):
             govde.add_widget(Button(text = "{}".format(i+1)))
                  
        return govde
'''
#kivy ile kullanıcıdan degerde alabiliriz bunun icinde TextInput fonk.kullanılır
#from kivy.uix.textinput import TextInput   ile fonksiyonu ekleriz


class Program(App):
    def build(self):
        # Bir TextInput widgeti oluştur
        text_input = TextInput(text='metin girin:',multiline = False, font_size=20, background_color=(1, 0, 0, 1))
        return text_input



if __name__=='__main__':
    Program().run()