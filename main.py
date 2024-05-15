from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget




class WidgetsExample(GridLayout):
    my_text = StringProperty("1")
    text_input_str = StringProperty("foo")
    counter = 1
    toggle_state = BooleanProperty(False)


    def on_button_click(self):
        if self.toggle_state:
            self.counter += 1
            self.my_text = str(self.counter)
        else:
            pass

    def on_toggle_button_state(self, widget):
        if widget.state == 'down':
            widget.text = 'ON'
            self.toggle_state = True
        elif widget.state == 'normal':
            widget.text = 'OFF'
            self.toggle_state = False

    def on_switch_active(self, widget):
        print("Switch: " + str(widget.active))

    def on_slider_value(self, widget):
        pass

    def on_text_validate(self, widget):
        self.text_input_str = widget.text




class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for i in range(0, 100):
            b = Button(text=str(i+1), size_hint=(.2, .2))
            self.add_widget(b)

# class GridLayoutExample(GridLayout):
#     pass


class AnchorLayoutExample(AnchorLayout):
    pass


class BoxLayoutExample(BoxLayout):
     pass
     """def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text='Hello')
        b2 = Button(text='Hello2')
        b3 = Button(text='Hello3')

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
    """


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

TheLabApp().run()
