from flask import Flask
from data.db_session import global_init, create_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    session = create_session()
    for i in session.query(User).filter(User.address == 'module_1', User.age < 21):
        i.address = 'module_3'
    session.commit()


if __name__ == '__main__':
    main()