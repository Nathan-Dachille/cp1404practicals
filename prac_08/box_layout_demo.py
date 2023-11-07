"""Modified version of Box Layout demo."""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Kivy App that contains for entering a name and responding with a greeting."""
    def build(self):
        """Build main app."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Respond with a greeting when called."""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Reset fields when called."""
        self.root.ids.output_label.text = 'Enter your name'
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
