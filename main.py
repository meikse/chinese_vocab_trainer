from numpy import random 
import time 
import xlwings as xw
import kivy   
from kivy.app import App  
from kivy.uix.label import Label  
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

### DO CHANGES HERE IF YOU WANT DIFFERENT VOCAB ###
path = r'.\Hanyu.odt'
xw.Book(path).set_mock_caller()
wb = xw.Book.caller()
ws1 = wb.sheets['Tabelle1']

# initalize the font
font_size = int(50)
font_path = r".\DroidSansFallback.ttf"

# define a Girdlayout for the App
# here all widgets and all methods are placed
class MyGrid(GridLayout):
    
    # chose the right vocab from the sheet depending which lecture was chosen 
    # vocab is chosen randomly from the lecture
    row_list = [1]          
    def vocab(self):
        self.row = int(random.choice(self.row_list))
        self.german = str(ws1.range('b%d'%self.row).value)
        self.hanyu = str(ws1.range('d%d'%self.row).value)
        self.pinyin = str(ws1.range('c%d'%self.row).value)

    def __init__(self, **kwargs):

        # initialize first vocab
        self.vocab() 

        super(MyGrid, self).__init__(**kwargs)
        #### main grid
        # define column (and usually rows) for main grid
        self.cols= 1

        ### first cell
        # define columns inside the first cell
        self.first= GridLayout()
        self.first.cols = 2
        self.first.rows = 1

        # label to show vocab
        self.label = Label(text = self.pinyin, font_name = font_path, font_size = font_size)

        # textinput to enter vocab  
        self.textinput_vocab = TextInput(hint_text=u"german", font_name = font_path, font_size=font_size) 
        self.textinput_vocab.bind(on_text_validate=self.on_enter)
        self.textinput_vocab.multiline = False
        self.textinput_vocab.text_validate_unfocus = False
        self.textinput_vocab.write_tab = False

        # add all attributes in the first cell
        self.first.add_widget(self.label)
        self.first.add_widget(self.textinput_vocab)
        self.add_widget(self.first)

        ### second cell
        # define columns inside the second cell
        self.second= GridLayout()
        self.second.cols = 1
        self.second.rows = 2

        ## third cell
        # define columns inside third cell
        self.third = GridLayout()
        self.third.cols = 2 
        self.third.rows = 1

        # button for switching languages
        self.button_left = Button(text =u"chinese (pinyin)", font_name = font_path, font_size = font_size*0.5) 
        self.button_left.bind(on_press=self.pressed_left)

        # button for switching between hanyu and pinyin
        self.button_right = Button(text =u"german", font_name = font_path, font_size = font_size*0.5)
        self.button_right.bind(on_press=self.pressed_right)

        # add all attributes to the thrid cell
        self.third.add_widget(self.button_left)
        self.third.add_widget(self.button_right)
        # add the third to the second cell
        self.second.add_widget(self.third)

        # textinput to choose lecture
        self.textinput_lecture = TextInput(hint_text=u"choose lecture", font_size=font_size*0.5)
        self.textinput_lecture.bind(on_text_validate=self.choose_lecture)
        self.textinput_lecture.multiline = False
        self.textinput_lecture.write_tab = False

        # add all attributes to the second cell
        self.second.add_widget(self.textinput_lecture)
        # add second cell to the main grid
        self.add_widget(self.second)

    # set range which vocab shall be learned 
    def choose_lecture(self, instance):
        listvalue = int(self.textinput_lecture.text)
        self.row_list = []
        for row in range(1,2000):
            value = ws1.range('a%d'%row).value 
            if value == listvalue:
                self.row_list.append(row)

    # initialize flags for the languages
    flag_left= 2    # chose the right flag and than add 1 
    flag_right = 1
    flag_enter = 1

    # chose label language
    def pressed_left(self, instance):
        if self.flag_left== 0:
            self.button_left.text = "german"
            self.label.text = self.german
            self.flag_left = 1 
        elif self.flag_left== 1:
            self.button_left.text = "chinese (pinyin)"
            self.label.text = self.pinyin
            self.flag_left = 2
        elif self.flag_left == 2:
            self.button_left.text = "chinese (汉语)"
            self.label.text = self.hanyu
            self.flag_left = 0

    # chose language for the textinput
    def pressed_right(self, instance):
        if self.flag_right == 0:
            self.button_right.text = "german"
            self.textinput_vocab.hint_text = "german"
            self.flag_right = 1 
        elif self.flag_right == 1:
            self.button_right.text = "chinese (pinyin)"
            self.textinput_vocab.hint_text = "chinese (pinyin)"
            self.flag_right = 2
        elif self.flag_right == 2:
            self.button_right.text = "chinese (汉语)"
            self.textinput_vocab.hint_text = "chinese (汉语)"
            self.flag_right = 0

    # execute the comparison between the languages 
    def on_enter(self, instance):
        if self.flag_enter == 1:
            if self.flag_right == 1:
                answer = self.german
            elif self.flag_right == 2:
                answer = self.pinyin
            elif self.flag_right == 0:
                answer = self.hanyu
            # examine if vocab was chosen correctly
            if self.textinput_vocab.text == answer:
                self.label.color = [0, 1, 0, 1]
            else:
                self.label.color = [1, 0, 0, 1]
                self.label.text = self.label.text + "\n" + "[" + answer + "]"                
            self.flag_enter = 0
        else:
            self.vocab()
            if self.flag_left == 1:
                new_vocab = self.german
            elif self.flag_left == 2:
                new_vocab = self.pinyin
            elif self.flag_left == 0:
                new_vocab = self.hanyu
            self.label.text = new_vocab
            self.textinput_vocab.text = ""
            self.label.color = [1, 1, 1, 1]
            self.flag_enter= 1

# build the App
class MyApp(App): 
    def build(self):
        return MyGrid()
 
# run the App 
if __name__ == "__main__": 
    MyApp().run() 
