from flask import Flask
from data.db_session import global_init, create_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    for i in create_session().query(Jobs).filter(Jobs.is_finished == 0, Jobs.work_size < 20):
        print(f'<Job> {i.job}')


if __name__ == '__main__':
    main()