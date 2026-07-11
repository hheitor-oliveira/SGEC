class SystemUser:
    def __init__(self,
                 id: int,
                 name: str,
                 login: str,
                 password: str,
                 role: str):
                 
        self.id = id
        self.name = name
        self.login = login
        self.password = password
        self.role = role