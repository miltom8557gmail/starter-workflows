import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class AkameNexus(App):
    def build(self):
        self.title = 'AKAME OMEGA'
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        self.status_label = Label(text="👁️ AKAME: ONLINE", font_size='20sp', color=(1, 0, 0, 1))
        layout.add_widget(self.status_label)
        
        btn = Button(text='EXECUTAR VONTADE', size_hint=(1, 0.2))
        btn.bind(on_press=self.executar)
        layout.add_widget(btn)
        return layout

    def executar(self, instance):
        os.system("termux-tts-speak 'Sim, Mestre. Em tempo real.'")

if __name__ == '__main__':
    AkameNexus().run()
