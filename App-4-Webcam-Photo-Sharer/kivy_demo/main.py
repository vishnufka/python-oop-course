from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import requests
import wikipedia
import time
import os.path

Builder.load_file("frontend.kv")


class FirstScreen(Screen):

    def search_image(self):
        text = self.manager.current_screen.ids.txt.text
        page = wikipedia.page(text, auto_suggest=False)
        file_path = f'images/{text}.jpg'
        if page:
            if len(page.images) > 0:
                url = page.images[0]
                self.generate_file(url, file_path)
        self.display_image(file_path)

    def generate_file(self, url, file_path):
        headers = {'User-Agent':
                       'CoolBot/0.0 (https://example.org/coolbot/; '
                       'coolbot@example.org)'}
        res = requests.get(url, headers=headers)
        with open(file_path, 'wb') as f:
            print(res.content)
            f.write(res.content)

    def display_image(self, file_path):
        while not os.path.exists(file_path):
            time.sleep(0.1)
        if os.path.isfile(file_path):
            self.manager.current_screen.ids.img.source = file_path
        else:
            raise ValueError("%s isn't a file!" % file_path)


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
