from flask import Flask
from data.db_session import global_init, create_session
from data.users import User
from data.jobs import Jobs
from data.departments import Department

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    global_init(input())
    arr = []
    session = create_session()
    dep = session.query(Department).filter(Department.id == 1).first()
    for member_id in dep.members.split(', ') + [str(dep.chief)]:
        hours = 0
        for job in session.query(Jobs):
            if member_id in job.collaborators.split(', '):
                hours += job.work_size
        if hours > 25:
            out = session.query(User).filter(User.id == int(member_id)).first()
            x = [out.surname, out.name]
            if x not in arr:
                arr.append(x)
    for x in arr:
        print(*x)
    session.commit()


if __name__ == '__main__':
    main()