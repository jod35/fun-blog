class Config:
    my_pw="nathanoj35"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI='mysql://jon:{}@localhost/simple'.format(my_pw)
    SQLALCHEMY_ECHO=False
    SECRET_KEY='0043e3594ceb57e473b15e0b2c74e035e45a018533caddd8654a20b92a0f8f31'
    DEBUG=True
    AVATARS_GRAVATAR_DEFAULT='identicon'