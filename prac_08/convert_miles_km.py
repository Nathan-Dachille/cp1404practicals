from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_KM_CONVERSION_FACTOR = 1.61


class ConvertMilesKm(App):
    output_distance = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_distance = "Enter a distance and press enter"
        return self.root

    def handle_increment(self, increment):
        current_input = float(self.root.ids.input_distance.text)
        current_input += increment
        self.root.ids.input_distance.text = str(current_input)

    def convert(self):
        current_input = float(self.root.ids.input_distance.text)
        current_input *= MILES_KM_CONVERSION_FACTOR
        self.output_distance = str(current_input)


ConvertMilesKm().run()
