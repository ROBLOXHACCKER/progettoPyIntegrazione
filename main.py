import numpy as np
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

"""
    PROGRAMMA REALIZZATO DA: PAOLO BROGI | ROSELLI SAMUELE | MOLINO ANTONIO
    
    Il programma riuscirà a eseguire l'integrazione numerica di funzioni definite su un intervallo specificato
    tramite l'utilizzo di 3 metodi:

    - RETTANGOLI
    - TRAPEZI
    - PARABOLE 

    LIBRERIE: 
    - 'numpy' -->  calcolo
    - 'kivy' --> grafica

"""

#IMPAGINAZIONE PROGRAMMA (grafica)
class IntegrationApp(App):
    def __init__(self, **kwargs):
        super(IntegrationApp, self).__init__(**kwargs)

    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        background = Background()

        # TITOLO PROGRAMMA
        titolo = Label(text="Calcolatore di Integrazione Numerica", font_size='28sp', size_hint=(1, None), height=50)
        layout.add_widget(titolo)

        # T-BOX PER FUNZIONE IN INPUT
        funzione_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=50)
        funzione_layout.add_widget(Label(text="Funzione (in x):", size_hint=(0.3, 1)))
        self.funzione_input = TextInput(text='', multiline=False, size_hint=(0.7, 1))
        funzione_layout.add_widget(self.funzione_input)
        layout.add_widget(funzione_layout)

        # T-BOX ESTREMO INFERIORE | SUPERIORE
        estremi_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1, None), height=50)
        estremi_layout.add_widget(Label(text="Estremo Inferiore (a):", size_hint=(0.3, 1)))
        self.estremo_inf_input = TextInput(text='', multiline=False, input_type='number', size_hint=(0.2, 1))
        estremi_layout.add_widget(self.estremo_inf_input)
        estremi_layout.add_widget(Label(text="Estremo Superiore (b):", size_hint=(0.3, 1)))
        self.estremo_sup_input = TextInput(text='', multiline=False, input_type='number', size_hint=(0.2, 1))
        estremi_layout.add_widget(self.estremo_sup_input)
        layout.add_widget(estremi_layout)

        # BUTTON CALCOLO INTEGRALE
        calcola_button = Button(text="Calcola", size_hint=(0.2, None), height=50)
        calcola_button.bind(on_press=self.calcola_integrale)
        layout.add_widget(calcola_button)

        # Risultati dell'integrale
        self.risultati_label = Label(text="", font_size='18sp', size_hint=(1, 1), halign="left", valign="top")
        layout.add_widget(self.risultati_label)

        layout.add_widget(background)
        return layout

#DEFINIZIONE FUNZIONI (calcolo  integrale)
    def calcola_integrale(self, instance):
        funzioneInserita = self.funzione_input.text
        a = float(self.estremo_inf_input.text) 
        b = float(self.estremo_sup_input.text)
        n = np.round((b - a) * 10)
        if not n % 2 == 0:  #check se pari
            n += 1
        if b <= a:
            self.risultati_label.text = "ERROR: ESTREMI POSIZIONATI NELL'ORDINE SBAGLIATO, RIPOSIZIONAMENTO AUTOMATICO"
            a, b = b, a  # Scambia le variabili

        f = lambda x: eval(funzioneInserita)
        
        rettangoli = self.metodoRettangoli(f, a, b, n)
        trapezi = self.metodoTrapezi(f, a, b, n)
        parabole = self.metodoParabole(f, a, b, n)
        #CHECK EROORE | STAMPA RISULTATO
        if rettangoli == "errore" or trapezi == "errore" or parabole == "errore":
            self.risultati_label.text = "Errore nel calcolo! La funzione potrebbe non essere continua nell'intervallo, controlla bene."
        else:
            self.risultati_label.text = ("Risultato (metodo dei rettangoli): {}\n"
                                          "Risultato (metodo dei trapezi): {}\n"
                                          "Risultato (metodo delle parabole): {}".format(rettangoli, trapezi, parabole))


#DEFINIZIONE FUNZIONI (calcolo  metodi)
    def metodoRettangoli(self, f, a, b, n):
        somma = 0
        for i in np.arange(a, b, (b - a) / n):
            try:
                somma += f(i)
            except:
                return "errore"

        somma += f(b)
        somma *= (b - a) / n
        return np.around(somma, 5)

    def metodoTrapezi(self, f, a, b, n):
        somma = 0
        for i in np.arange(a, b, (b - a) / n):
            try:
                somma += 2 * f(i)
            except:
                return "errore"
        somma += f(b)
        somma -= f(a)
        somma *= (b - a) / (2 * n)
        return np.around(somma, 5)

    def metodoParabole(self, f, a, b, n):
        somma = 0
        contatore = 0
        for i in np.arange(a, b, (b - a) / n):
            try:
                if contatore % 2 == 0:
                    somma += 2 * f(i)
                else:
                    somma += 4 * f(i)
                contatore += 1
            except:
                return "error"
        somma += f(b)
        somma -= f(a)
        somma *= (b - a) / (3 * n)
        return np.around(somma, 5)

#AGGIORNAMENTO INTERFACCIA GRAFICA PER DISPLAY RISULTATI

class Background(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Color(0.95, 0.95, 0.95, 1)  # COLORE SFONDO
            self.rect = Rectangle(size=self.size, pos=self.pos)
            self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, instance, value):
        self.rect.size = instance.size
        self.rect.pos = instance.pos

#RUNNABLE

if __name__ == "__main__":
    IntegrationApp().run()
