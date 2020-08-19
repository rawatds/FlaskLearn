from blog import User, Post, db


# Create the database
db.drop_all()
# re-create
db.create_all()

# Create two users
user1 = User(username = 'dsrawat', email = 'dsrawat@gmail.com', password = 'password')
user2 = User(username = 'anilk', email = 'anilk@gmail.com', password = 'passwordk')

db.session.add(user1)
db.session.add(user2)

db.session.commit()

# Query db
print(User.query.all())

print(User.query.first())

print(User.query.filter_by(username = 'dsrawat').all())

dsr =  User.query.filter_by(username = 'dsrawat').first()
print(dsr)
print(dsr.id, dsr.password, dsr.image_file, dsr.username, sep=":")

ak = User.query.get(2)
print(ak)

print(dsr.posts)

post1 = Post(title = 'Blog#1', contents = 'My first blog contents', user_id = dsr.id)
post2 = Post(title = 'Blog#2', contents = 'My second blog contents', user_id = dsr.id)
post3 = Post(title = 'Blog#3', contents = 'Anil first blog contents', user_id = ak.id)

db.session.add(post1)
db.session.add(post2)
db.session.add(post3)
db.session.commit()

print(post1, post2, post3)

print(dsr.posts)
print(ak.posts)

print(post1.id, post1.user_id)
print(post3.id, post3.user_id)

print(post2.author)
author = post3.author
print(author, author.id)







