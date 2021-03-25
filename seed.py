from application.extensions import db
from application.app import create_app
from models import Post, User


app = create_app('application.config.DevelopmentConfig')
app.app_context().push()

user1 = User(
    name="Bob marlin ",
    email='bob.marlin@gmail.com'
)
user2 = User(
    name="Leonardo cohen",
    email='leonardo.cohen@gmail.com'
)
user3 = User(
    name="Chris deburge",
    email='chris.deburge@gmail.com'
)

db.session.add(user1)
db.session.add(user2)
db.session.add(user3)
db.session.flush()

post1 = Post()
post1.title = "Blog Post Title 1"
post1.body = "This is the first blog post 1"
post1.author = user1
post1.user = user1

post2 = Post()
post2.title = "Blog Post Title 2"
post2.body = "This is the first blog post 2"
post2.author = user2
post2.user = user2

db.session.add(post1)
db.session.add(post2)
db.session.commit()

print(User.query.all())
print(Post.query.all())

