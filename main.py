from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from auth import AuthSystem



KV = """
ScreenManager:
    LoginScreen:
    SignupScreen:

<LoginScreen>:
    name: "login"
    MDLabel:
        text: "AI-Driven Intelligent Attendance System"
        halign: "center"
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"

    MDCard:
        size_hint: 0.8, 0.5
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: "vertical"
        padding: 20
        spacing: 20
        md_bg_color: 0.1, 0.1, 0.1, 1
        elevation: 8
        radius: [20]

        MDTextField:
            id: reg_id
            hint_text: "Registration ID"
            icon_right: "account"
            mode: "rectangle"

        MDTextField:
            id: password
            hint_text: "Password"
            password: True
            icon_right: "lock"
            mode: "rectangle"

        MDRaisedButton:
            text: "Sign In"
            md_bg_color: 0, 0.5, 1, 1
            on_release: app.sign_in(reg_id.text, password.text)

        MDFlatButton:
            text: "Sign Up (New User)"
            theme_text_color: "Custom"
            text_color: 0, 0.6, 1, 1
            on_release: app.switch_to_signup()

<SignupScreen>:
    name: "signup"
    MDLabel:
        text: "Register New User"
        halign: "center"
        pos_hint: {"center_y": 0.9}
        theme_text_color: "Custom"
        text_color: 1, 1, 1, 1
        font_style: "H5"

    MDCard:
        size_hint: 0.85, 0.6
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        orientation: "vertical"
        padding: 20
        spacing: 15
        md_bg_color: 0.1, 0.1, 0.1, 1
        elevation: 8
        radius: [20]

        MDTextField:
            id: name
            hint_text: "Full Name"
            icon_right: "account"

        MDTextField:
            id: reg_id
            hint_text: "Registration/ID"
            icon_right: "badge-account"

        MDTextField:
            id: course
            hint_text: "Course"
            icon_right: "book"

        MDRaisedButton:
            text: "Capture Face & Register"
            md_bg_color: 0, 0.6, 1, 1
            on_release: app.register_user(name.text, reg_id.text, course.text)

        MDFlatButton:
            text: "Back to Login"
            text_color: 0, 0.6, 1, 1
            on_release: app.switch_to_login()
"""

class LoginScreen(MDScreen):
    pass

class SignupScreen(MDScreen):
    pass

class AttendanceApp(MDApp):
    def build(self):
        self.auth = AuthSystem()
        return Builder.load_string(KV)

    def sign_in(self, reg_id, password):
        if self.auth.sign_in(reg_id, password):
            print(f"✅ Welcome {reg_id} — Attendance Recorded.")
        else:
            print("❌ Invalid credentials or face not recognized.")

    def register_user(self, name, reg_id, course):
        self.auth.sign_up(name, reg_id, course)
        print("✅ Registration complete! Face saved.")

    def switch_to_signup(self):
        self.root.current = "signup"

    def switch_to_login(self):
        self.root.current = "login"

if __name__ == "__main__":
    AttendanceApp().run()
