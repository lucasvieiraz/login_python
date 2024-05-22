from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class LoginScreen(BoxLayout):
    pass

class LoginApp(App):
    def build(self):
        return LoginScreen()

    def login(self, username, password):
        if username == "lucas" and password == "12345":
            self.root.ids.message.text = "Acessando sua Conta!"
            self.root.ids.message.color = (0, 1, 0, 1)  
        else:
            self.root.ids.message.text = "Nome de usuario ou Senha Incorreto, tente novamente"
            self.root.ids.message.color = (1, 0, 0, 1)  
if __name__ == '__main__':
    LoginApp().run()
