class authSystem:
    def __init__(self):
        self.users={
            "user1": "password1",
            "user2": "password2",
            "user3": "password3"
        }
    
    def sign_up(self, username, password):
        if username in self.users:
            return "Username sudah digunakan, silahkan masukan username lain"
        self.users[username] = password
        return "Sign up berhasil"


    def sign_in(self, username, password):
        if username not in self.users:
            return "Username tidak ditemukan"
        if self.users[username] != password:
            return "Password salah"
        return "Masuk berhasil"
