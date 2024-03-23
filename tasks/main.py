from flask import Flask

from data.users import User
from data.jobs import Jobs
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()

    # user = User()
    # user.surname = "Scott"
    # user.name = "Ridley"
    # user.age = 21
    # user.position = "captain"
    # user.speciality = "research engineer"
    # user.address = "module_1"
    # user.email = "scott_chief@mars.org"

    # user2 = User()
    # user2.surname = "gDsty"
    # user2.name = "Ol"
    # user2.age = 16
    # user2.position = "vice"
    # user2.speciality = "music"
    # user2.address = "module_2"
    # user2.email = "TOF@mars.org"

    # user3 = User()
    # user3.surname = "SmR"
    # user3.name = "Nkt"
    # user3.age = 16
    # user3.position = "trainee"
    # user3.speciality = "CS"
    # user3.address = "module_3"
    # user3.email = "2500elo@mars.org"

    # user4 = User()
    # user4.surname = "Kent"
    # user4.name = "Slavics"
    # user4.age = 16
    # user4.position = "coach"
    # user4.speciality = "gaming"
    # user4.address = "module_4"
    # user4.email = "200_by_day@mars.org"

    # job = Jobs()
    # job.team_leader = 1
    # job.job = "deployment of residential modules 1 and 2"
    # job.work_size = 15
    # job.collaborators = "1, 2"
    # job.is_finished = False

    # db_sess = db_session.create_session()
    # db_sess.add(user)
    # db_sess.add(user2)
    # db_sess.add(user3)
    # db_sess.add(user4)
    # db_sess.add(job)
    # db_sess.commit()


if __name__ == '__main__':
    main()
