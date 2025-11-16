import sqlite3
from typing import Optional
from classes import Trigger_info


class DB:
    def __init__(self, db_path: str = "triggers.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Создает таблицу, если она не существует"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS triggers (
                trigger TEXT,
                info TEXT
            )
            """)
            conn.commit()

    def save(self, US: Trigger_info) -> bool:
        """Сохраняет или обновляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM triggers WHERE trigger = ?", (US.trigger,
                                                                            ))
                exists = cursor.fetchone()
                if exists:
                    query = """
                    UPDATE triggers SET
                        trigger = ?,
                        info = ?
                    WHERE trigger = ?
                    """
                    params = (
                        US.trigger, US.info, US.trigger,
                    )
                else:
                    # Создание нового профиля
                    query = """
                    INSERT INTO triggers (
                        trigger,info
                    ) VALUES (?, ?)
                    """

                    params = (
                        US.trigger, US.info,
                    )
                cursor.execute(query, params)
                conn.commit()
                return True

        except sqlite3.Error as e:
            print(e)
            return False

    def find(self, trigger: str) -> Optional[Trigger_info]:
        """Загружает профиль пользователя по ID"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()

                cursor.execute("SELECT * FROM triggers WHERE trigger = ?", (trigger,))
                row = cursor.fetchone()

                if row:
                    return Trigger_info(
                        row['trigger'], row['info']
                    )
                return None

        except sqlite3.Error as e:
            return None

    def delete(self, trigger: str) -> bool:
        """Удаляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM triggers WHERE trigger = ?", (trigger,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            return False

    def find_all(self):
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM triggers")
                rows = cursor.fetchall()
                a = []
                for row in rows:
                    a.append(Trigger_info(row['trigger'], row['info']))
                return a
        except sqlite3.Error as e:
            print(e)
            return None


class AdminIDS:
    def __init__(self, db_path: str = "triggers.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Создает таблицу, если она не существует"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
              CREATE TABLE IF NOT EXISTS AdminIDS (
                  id INTEGER PRIMARY KEY
              )
              """)
            conn.commit()

    def save(self, US: int) -> bool:
        """Сохраняет или обновляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM AdminIDS WHERE id = ?", (US,
                                                                       ))
                exists = cursor.fetchone()
                if exists:
                    return False
                else:
                    # Создание нового профиля
                    query = """
                    INSERT INTO AdminIDS (
                        id
                    ) VALUES (?)
                    """
                    params = (
                        US,
                    )
                cursor.execute(query, params)
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete(self, trigger: int) -> bool:
        """Удаляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM AdminIDS WHERE id = ?", (trigger,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            return False

    def find(self, _id: int) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM AdminIDS WHERE id = ?", (_id,))
                rows = cursor.fetchone()
                return rows
        except sqlite3.Error as e:
            print(e)
            return False


class AllowedCHATS:
    def __init__(self, db_path: str = "triggers.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Создает таблицу, если она не существует"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
              CREATE TABLE IF NOT EXISTS AllowedCHATS (
                  id INTEGER PRIMARY KEY
              )
              """)
            conn.commit()

    def save(self, US: int) -> bool:
        """Сохраняет или обновляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT 1 FROM AllowedCHATS WHERE id = ?", (US,
                                                                           ))
                exists = cursor.fetchone()
                if exists:
                    return False
                else:
                    # Создание нового профиля
                    query = """
                    INSERT INTO AllowedCHATS (
                        id
                    ) VALUES (?)
                    """
                    params = (
                        US,
                    )
                cursor.execute(query, params)
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(e)
            return False

    def delete(self, trigger: int) -> bool:
        """Удаляет профиль пользователя"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM AllowedCHATS WHERE id = ?", (trigger,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            return False

    def find(self, _id: int) -> bool:
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM AllowedCHATS WHERE id = ?", (_id,))
                rows = cursor.fetchone()
                return rows
        except sqlite3.Error as e:
            print(e)
            return False
