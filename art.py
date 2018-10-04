import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import AsyncImage
from kivy.uix.gridlayout import GridLayout

# sample of how to upload image to center of canvas
class ScreenWithImage(GridLayout):

    def __init__(self, **kwargs):
        self.cols = 1
        super(ScreenWithImage, self).__init__(**kwargs)
        self.image = AsyncImage(source='hello world.png')
        self.add_widget(self.image)



class MyApp(App):

    def build(self):
        return ScreenWithImage()


if __name__ == '__main__':
    MyApp().run()