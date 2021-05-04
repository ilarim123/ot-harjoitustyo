from pathlib import Path
from config import USERS_FILE_PATH

class UserRepository:
    """Luokka, jonka avulla luodaan ja tutkitaan käyttäjiä sekä suorituksia.

    Attributes:
        _file_path: Polku tiedostolle johon käyttäjät tallennetaan.
    """

    def __init__(self, file_path):
        """Luokan konstruktori, jossa määritellään tiedoston polku.

        Args:
            file_path: Tiedoston polku.
        """

        self._file_path = file_path

    def _ensure_file_exists(self):
        """Tarkistaa tiedoston olemassaolon ja tarvittaessa luo tiedoston.

        """

        Path(self._file_path).touch()

    def does_user_exist(self, username):
        """Tarkastaa onko käyttäjä tiedostossa.

        Args:
            username: Haluttu käyttäjänimi.

        Returns:
            True jos käyttäjä löytyy tiedostosta, muutoin False.
        """

        self._ensure_file_exists()

        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                user = parts[0]

                if user == username:
                    return True

            return False

    def create_user(self, username, password):
        """Luo uuden käyttäjän tiedostoon

        Args:
            username: Käyttäjän käyttäjänimi
            password: Käyttäjän salasana
        """

        self._ensure_file_exists()

        with open(self._file_path, 'a') as file:
            row = f'{username};{password};add_done_false;sub_done_false;multi_done_false'

            file.write(row+'\n')

    def check_password(self, username, password):
        """Tarkistaa onko käyttäjän syöttämä salasana oikein

        Args:
            username: Käyttäjän käyttäjänimi
            password: Käyttäjän salasana

        Returns:
            True jos salasana on oikein, muutoin False
        """

        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                user = parts[0]

                if user == username:
                    correctpassword = parts[1]
                    if password == correctpassword:
                        return True

                    return False

    def check_completion(self, username, taskset: str):
        """Tarkistaa onko käyttäjä suorittanut kyseisen tehtäväsarjan

        Args:
            username: Käyttäjän käyttäjänimi
            taskset: Haluttu tehtäväsarja

        Returns:
            True jos tehtäväsarja on suoritettu, muutoin False
        """

        with open(self._file_path) as file:
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')

                user = parts[0]

                if user == username:
                    if taskset == 'add':
                        if 'add_done_true' in row:
                            return True
                    elif taskset == 'sub':
                        if 'sub_done_true' in row:
                            return True
                    elif taskset == 'multi':
                        if 'multi_done_true' in row:
                            return True

                    return False

    def mark_as_completed(self, username, taskset):
        """Merkitsee kyseisen tehtäväsarjan tehdyksi käyttäjälle

        Args:
            username: Käyttäjän käyttäjänimi
            taskset: Haluttu tehtäväsarja
        """

        with open(self._file_path) as file:
            rowlist = []
            for row in file:
                row = row.replace('\n', '')
                parts = row.split(';')
                rowlist.append(parts)

            for row in rowlist:
                if row[0] == username:
                    if taskset == 'add':
                        row[2] = 'add_done_true'
                    elif taskset == 'sub':
                        row[3] = 'sub_done_true'
                    elif taskset == 'multi':
                        row[4] = 'multi_done_true'

            rowlist2 = []

            for row in rowlist:
                newrow = ";".join(row)
                rowlist2.append(newrow)

            newtext = "\n".join(rowlist2)

            file.close()

        with open(self._file_path, "w") as file:
            file.write(newtext+'\n')

    def delete_all_users(self):
        """Tyhjentää tiedoston johon käyttäjiä lisätään

        """

        with open(self._file_path, "w") as file:
            file.write("")


user_repository = UserRepository(USERS_FILE_PATH)
