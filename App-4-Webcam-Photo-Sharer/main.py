from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import time

Builder.load_file("frontend.kv")


class FileSharer:

    def __init__(self, filepath, api):
        self.filepath = filepath
        self.api = api

    def share(self):
        print("file shared!")


class CameraScreen(Screen):

    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        self.filepath = f"snapshots/{time.strftime('%Y%m%d-%H%M%S')}.png"
        self.ids.camera.export_to_png(self.filepath)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filepath


class ImageScreen(Screen):
    pass


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
