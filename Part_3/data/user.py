import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str
    current_address: str
    permanent_address: str


user_student = User(full_name='Роман Гороховик', email='roman_qa@gmail.com',
                    current_address='Кемерово, ул. Советсткая, д.6',
                    permanent_address='г. Анжеро-Судженск, пгт. Рудничный, ул. металлургов 5-32')
