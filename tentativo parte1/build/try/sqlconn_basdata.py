from pathlib import Path
import os
import json
import hashlib

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    mysql = None
    MYSQL_AVAILABLE = False


class Mycon_basdata:
    def __init__(self, username=None, password=None, birthday=None, filedat=None, description=None, email=None, language=None):
        self.username = username
        self.password = password
        self.birthday = birthday
        self.language = language
        self.description = description
        self.filedat = filedat or "samurai1_png"
        self.email = email
        self.is_offline = False
        self.conn = None
        self.cursor = None

        # Resolve paths dynamically
        self.base_dir = Path(__file__).resolve().parent.parent.parent
        self.config_path = self._find_file("sqldatafile.json")
        self.users_json_path = self._find_file("users.json")

        config = {}
        if self.config_path and self.config_path.exists():
            try:
                with open(self.config_path, "r", encoding="utf-8") as config_file:
                    config = json.load(config_file)
            except Exception:
                config = {}

        self.host = config.get("DB_HOST", "sql11.freesqldatabase.com")
        self.user = config.get("DB_USER", "sql11674879")
        self.passcode = config.get("DB_PASSWORD", "cMFiYb63Vi")
        self.database = config.get("DB_DATABASE", "sql11674879")

        # Attempt MySQL connection with timeout, fallback to offline demo mode
        force_offline = os.getenv("VLIB_FORCE_OFFLINE") == "1"
        if force_offline:
            self.is_offline = True
        elif MYSQL_AVAILABLE:
            try:
                self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.user,
                    password=self.passcode,
                    database=self.database,
                    connection_timeout=3
                )
                self.cursor = self.conn.cursor()
            except Exception as e:
                print(f"[VLib Data Engine] Remote MySQL unavailable ({e}). Running in Offline Demo Mode.")
                self.is_offline = True
        else:
            self.is_offline = True

    def _find_file(self, filename: str) -> Path:
        candidates = [
            Path(filename),
            self.base_dir / filename,
            Path(__file__).resolve().parent / filename
        ]
        for c in candidates:
            if c.exists():
                return c
        return self.base_dir / filename

    def _load_local_users(self):
        if self.users_json_path.exists():
            try:
                with open(self.users_json_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                pass
        return [
            {"username": "thezen46", "password": "S/um17", "filedata": "samurai1_png"},
            {"username": "Poldo", "password": "C4L4br3$", "filedata": "V1_png"},
            {"username": "scandaloah", "password": "Sc4#", "filedata": "CasualBG1_png"}
        ]

    def find_and_verify(self):
        if self.is_offline or not self.cursor:
            users = self._load_local_users()
            for u in users:
                if u.get("username") == self.username:
                    stored_pass = u.get("password", "")
                    target_hash = hashlib.sha256(self.password.encode("utf-8")).hexdigest()
                    if stored_pass == self.password or stored_pass == target_hash:
                        return True
            return False

        try:
            self.cursor.execute("SELECT username, en_passcode FROM Vlib;")
            results = self.cursor.fetchall()
            target_hash = hashlib.sha256(self.password.encode("utf-8")).hexdigest()
            for row in results:
                username, en_pass = row[0], row[1]
                if username == self.username:
                    return en_pass == target_hash
            return False
        except Exception:
            self.is_offline = True
            return self.find_and_verify()

    def find_and_verify_noenc(self):
        if self.is_offline or not self.cursor:
            users = self._load_local_users()
            for u in users:
                if u.get("username") == self.username:
                    stored_pass = u.get("password", "")
                    if stored_pass == self.password:
                        return True
            return False

        try:
            self.cursor.execute("SELECT username, en_passcode FROM Vlib;")
            results = self.cursor.fetchall()
            for row in results:
                username, en_pass = row[0], row[1]
                if username == self.username:
                    return en_pass == self.password
            return False
        except Exception:
            self.is_offline = True
            return self.find_and_verify_noenc()

    def get_imagepath(self):
        if self.is_offline or not self.cursor:
            users = self._load_local_users()
            for u in users:
                if u.get("username") == self.username:
                    return u.get("filedata", "samurai1_png")
            return "samurai1_png"

        try:
            self.cursor.execute("SELECT username, filedata FROM Vlib;")
            results = self.cursor.fetchall()
            for row in results:
                if row[0] == self.username:
                    return row[1] or "samurai1_png"
            return "samurai1_png"
        except Exception:
            return "samurai1_png"

    def find_and_verify_name(self):
        if self.is_offline or not self.cursor:
            users = self._load_local_users()
            for u in users:
                if u.get("username") == self.username:
                    return False
            return True

        try:
            self.cursor.execute("SELECT username FROM Vlib;")
            results = self.cursor.fetchall()
            for row in results:
                if row[0] == self.username:
                    return False
            return True
        except Exception:
            self.is_offline = True
            return self.find_and_verify_name()

    def write_and_modify(self):
        encoded_pass = self.password.encode("utf-8")
        password_en = hashlib.sha256(encoded_pass).hexdigest()

        if self.is_offline or not self.cursor:
            users = self._load_local_users()
            users.append({
                "username": self.username,
                "password": self.password,
                "en_passcode": password_en,
                "filedata": self.filedat or "samurai1_png",
                "birthday": self.birthday,
                "description": self.description,
                "email": self.email,
                "language": self.language
            })
            try:
                with open(self.users_json_path, "w", encoding="utf-8") as f:
                    json.dump(users, f, indent=4)
            except Exception as e:
                print(f"[VLib Local Cache] Could not write user: {e}")
            return

        try:
            insert_query = "INSERT INTO Vlib (username, en_passcode, filedata, birthday, description, email, language) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            data = (self.username, password_en, self.filedat, self.birthday, self.description, self.email, self.language)
            self.cursor.execute(insert_query, data)
            self.conn.commit()
        except Exception as e:
            print(f"[VLib Database] Remote insert failed ({e}), saving to local cache.")
            self.is_offline = True
            self.write_and_modify()

    def close_all(self):
        if self.cursor:
            try:
                self.cursor.close()
            except Exception:
                pass
        if self.conn:
            try:
                self.conn.close()
            except Exception:
                pass
