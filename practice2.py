bcrypt.hashpw(passward, bcrypt.gensalt())
bcrypt.checkpw(password.encode('utf-8'), real_password.encode('utf-8'))