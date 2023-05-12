from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
import datetime
#Clock Olayları:
#Clock sınıfı, belirtilen süre sonunda bir fonksiyon çalıştırmak üzere tasarlanmıştır
#Clock sınıfını iki şekilde kullanabiliriz. Birincisi, fonksiyonun sadece bir kez çağrılması.
#  Yani belirtilen süre sonunda, fonksiyon çalıştırılır

class Program(App):
    def build(self):

        self.yazi = Label(text = "Merhaba")

        Clock.schedule_once(self.degistir,3) # 3 saniye sonra, self.degistir adlı fonksiyonu çalıştır

        return self.yazi

    def degistir(self,event):
        self.yazi.text = "Dünya"

#belli aralıklarla sürekli çalışmasıdır. Fonksiyonu çalıştırır, 
#sonra belirtilen süre kadar bekler ve sonra tekrar çalıştırır.
#Bunu, siz sonlandırana kadar veya program kapanana kadar yapmaya devam eder.



Program().run()