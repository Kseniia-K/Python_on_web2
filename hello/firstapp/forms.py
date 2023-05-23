from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Имя клиента')
    age = forms.IntegerField(label='Возраст клиента')

class UserForm(forms.Form):
    basket = forms.BooleanField(label="Положить в корзину", required=False)

class UserForm(forms.Form):
    vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")

class UserForm(forms.Form):
   name = forms.CharField(label="Имя клиента", max_length=15, help_text="ФИО не более 15 символов")

class UserForm(forms.Form):
   email = forms.EmailField(label="Электронный адрес", help_text="Обязательный символ - @")

class UserForm(forms.Form):
   ip_adres = forms.GenericIPAddressField(label="IP адрес", help_text=" Пример формата 192.0.2.0")

class UserForm(forms.Form):
   reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")

class UserForm(forms.Form):
   slug_text = forms.SlugField(label="Введите текст")

class UserForm(forms.Form):
   url_text = forms.URLField(label="Введите URL", help_text="Например http://www.google.com")

class UserForm(forms.Form):
   uuid_text = forms.UUIDField(label="Введите UUID", help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")

class UserForm(forms.Form):
   combo_text = forms.ComboField(label="Введите URL",
                                fields=[forms.URLField(), forms.CharField(max_length=20)])

class UserForm(forms.Form):
    file_path = forms.FilePathField(label="Выберите файл", path="/Users/kseniyakhokhlova/Desktop/pythonProject/Web_1/hello/firstapp", allow_files="True", allow_folders="True")

class UserForm(forms.Form):
    file = forms.FileField(label="Файл")

class UserForm(forms.Form):
    file = forms.ImageField(label="Изображение")

class UserForm(forms.Form):
    date = forms.DateField(label="Введите дату")

class UserForm(forms.Form):
    time = forms.DateField(label="Введите время")

class UserForm(forms.Form):
    date_time = forms.DateTimeField(label="Введите дату и время")

class UserForm(forms.Form):
    time_delta = forms.DurationField(label="Введите промежуток времени")

class UserForm(forms.Form):
    date_time = forms.SplitDateTimeField(label="Введите дату и время")

class UserForm(forms.Form):
    num = forms.IntegerField(label="Введите целое число")

class UserForm(forms.Form):
    num = forms.DecimalField(label="Введите десятичное число", decimal_places=2)

class UserForm(forms.Form):
    num = forms.FloatField(label="Введите число")

class UserForm(forms.Form):
    ling = forms.ChoiceField(label="Выберите язык",
                             choices=((1, "Английский"),
                                      (2, "Немецкий"),
                                      (3, "Французский")))

class UserForm(forms.Form):
    city = forms.TypedChoiceField(label="Выберите город",
                                  empty_value=None,
                                  choices=((1, "Москва"),
                                           (2, "Воронеж"),
                                           (3, "Курск")))

class UserForm(forms.Form):
    country = forms.MultipleChoiceField(label="Выберите страны",
                                        choices=((1, "Англия"),
                                                 (2, "Германия"),
                                                 (3, "Испания"),
                                                 (4, "Россия")))


class UserForm(forms.Form):
    city = forms.TypedMultipleChoiceField(label="Выберите город",
                                          empty_value=None,
                                          choices=((1, "Москва"),
                                                   (2, "Воронеж"),
                                                   (3, "Курск"),
                                                   (4, "Томск")))

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО")
    age = forms.IntegerField(label="Возраст", initial=18)
    comment = forms.CharField(label="Комментарий", widget=forms.Textarea)

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО")
    age = forms.IntegerField(label="Возраст", initial=18)
    field_order = ["age", "name"]

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", initial="Введите ФИО")
    age = forms.IntegerField(label="Возраст", initial=18)

class UserForm(forms.Form):
    name = forms.CharField(label="Имя", help_text ="Введите ФИО")
    age = forms.IntegerField(label="Возраст", help_text ="Введите возраст")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")
    age = forms.IntegerField(label="Возраст")
    email = forms.EmailField(label="Электронный адрес")
    reklama = forms.BooleanField(label="Согласны получать рекламу")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента")
    age = forms.IntegerField(label="Возраст клиента")

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=3)
    age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=100)

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента", min_length=3)
    age = forms.IntegerField(label="Возраст клиента", min_value=1, max_value=100)
    required_css_class = "field"
    error_css_class = "error"

class UserForm(forms.Form):
    name = forms.CharField(label="Имя клиента",
                           widget=forms.TextInput(attrs={"class": "myfield"}))
    age = forms.IntegerField(label="Возраст клиента",
                             widget=forms.NumberInput(attrs={"class": "myfield"}))
