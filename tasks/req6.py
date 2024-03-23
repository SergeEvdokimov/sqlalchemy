from flask import Flask

from data.db_session import global_init, create_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    session = create_session()
    out = []
    mx = max([len(i.collaborators.split()) for i in session.query(Jobs)])
    for i in session.query(Jobs):
        if len(i.collaborators.split()) == mx:
            for j in session.query(User).filter(User.id == i.team_leader):
                x = j.name, j.surname
                if x not in out:
                    print(*x)
                    out.append(x)


if __name__ == '__main__':
    main()