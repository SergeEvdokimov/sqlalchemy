from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    for i in create_session().query(User).filter(User.age < 18):
        print(f'<Colonist> {i.id} {i.surname} {i.name} {i.age} years')


if __name__ == '__main__':
    main()