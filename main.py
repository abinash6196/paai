from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import speech_recognition as sr
import datetime

class AssistantApp(App):
    def build(self):
        self.title = "Voice Assistant"
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        self.label = Label(text='வணக்கம்! மைக் பட்டனை அழுத்தவும்.', font_size=20)
        layout.add_widget(self.label)

        self.btn = Button(text='Speak / பேசுங்கள்', font_size=22, background_color=(0.1, 0.6, 0.8, 1))
        self.btn.bind(on_press=self.start_listening)
        layout.add_widget(self.btn)

        return layout

    def start_listening(self, instance):
        self.label.text = "Listening... கேட்கிறது..."
        r = sr.Recognizer()

        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                audio = r.listen(source)

            query = r.recognize_google(audio, language='ta-IN')
            self.label.text = f"நீங்கள் சொன்னது: {query}"

            if "நேரம்" in query or "time" in query:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                self.label.text = f"நேரம்: {current_time}"
        except Exception as e:
            self.label.text = "மன்னிக்கவும், சரியாகப் புரியவில்லை."

if __name__ == '__main__':
    AssistantApp().run()
