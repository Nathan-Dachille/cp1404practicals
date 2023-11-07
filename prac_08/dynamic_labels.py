"""Dynamic Labels exercise."""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NAMES = ["Bob Brown", "Cat Cyan", "Oren Ochre"]


class DynamicLabels(App):
    """Creates labels in a Kivy GUI from NAMES list."""
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        for name in NAMES:
            label = Label(text=name, font_size='46')
            self.root.ids.main.add_widget(label)
        return self.root


DynamicLabels().run()
