import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from application.extensions import db, ma


engine = create_engine('postgres://postgres:postgres@localhost/graphql_dev')
Session = sessionmaker(bind=engine)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % self.email


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User


class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    body = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship(
        'User',
        backref='user'
    )

    def __repr__(self):
        return '<Post %r>' % self.title


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post


# Objects Schema
class UserObject(SQLAlchemyObjectType):
    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)


class PostObject(SQLAlchemyObjectType):
    class Meta:
        model = Post
        interfaces = (graphene.relay.Node,)


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    all_posts = SQLAlchemyConnectionField(PostObject)
    all_users = SQLAlchemyConnectionField(UserObject)

    def resolve_all_posts(self, info):
        posts = Post.query.all()
        for post in posts:
            user = User.query.get(post.author_id)
            if user:
                post.user = user

        return Post.query.all()


# noinspection PyTypeChecker
schema_query = graphene.Schema(query=Query)


# Mutation Objects Schema
class CreatePost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        email = graphene.String(required=True)

    post = graphene.Field(lambda: PostObject)

    def mutate(self, info, title, body, email):
        user = User.query.filter_by(email=email).first()
        post = Post(title=title, body=body)
        if user is not None:
            post.author = user
        db.session.add(post)
        db.session.commit()
        return CreatePost(post=post)


class Mutation(graphene.ObjectType):
    save_post = CreatePost.Field()


# noinspection PyTypeChecker
schema_mutation = graphene.Schema(query=Query, mutation=Mutation)

