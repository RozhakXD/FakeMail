try:
    import random, string, os, sys, names, time, requests, json
    from rich.console import Console
    from rich.panel import Panel
    from mimesis.locales import Locale
    from faker import Faker
    from mimesis import Person
    from rich import print as printf
    from randomuser import RandomUser
except (ModuleNotFoundError) as e:
    __import__("sys").exit(f"[Error] {str(e).capitalize()}!")

LIVE, LOOPING, DIE, UNKNOWN = [], 0, [], []


class FITUR:
    def __init__(self) -> None:
        pass

    def UTAMA(self):
        try:
            self.TAMPILKAN_LOGO()
            printf(
                Panel(
                    f"""[bold green]01[bold white]. Create Email from Random String
[bold green]02[bold white]. Create Email from Mimesis
[bold green]03[bold white]. Create Email from Faker
[bold green]04[bold white]. Create Email from Names
[bold green]05[bold white]. Create Email from RandomUser
[bold green]06[bold white]. Valid Email Checker
[bold green]07[bold white]. Keluar ([bold red]Exit[bold white])""",
                    style="bold bright_black",
                    width=59,
                    title="[bold bright_black]> [Fitur Utama] <",
                    subtitle="[bold bright_black]╭───────",
                    subtitle_align="left",
                )
            )
            CHOOSE = Console().input("[bold bright_black]   ╰─> ")
            if CHOOSE in ["1", "2", "3", "4", "5", "01", "02", "03", "04", "05"]:
                printf(
                    Panel(
                        f"[bold white]Please fill in the domain, you are free to use any domain, for example:[bold green] @gmail.com[bold white]\n*make sure you only fill in one domain, no more!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Domain] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.DOMAIN = Console().input("[bold bright_black]   ╰─> ")
                if "@" in str(self.DOMAIN) and "." in str(self.DOMAIN):
                    printf(
                        Panel(
                            f"[bold white]Please fill in the desired amount to dump emails, make sure the amount is more than 100, for\nexample:[bold green] 1000[bold white] *[bold red]remember to only fill in numbers[bold white]!",
                            style="bold bright_black",
                            width=59,
                            title="[bold bright_black]> [Jumlah Email] <",
                            subtitle="[bold bright_black]╭───────",
                            subtitle_align="left",
                        )
                    )
                    self.COUNT = int(Console().input("[bold bright_black]   ╰─> "))
                    if self.COUNT >= 100:
                        printf(
                            Panel(
                                f"[bold white]Creating fake email, please wait a moment and you can use[bold green] CTRL + C[bold white] to stop, do not use[bold red] CTRL + Z[bold white],\nif an error occurs please check the response log!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Catatan] <",
                            )
                        )
                        self.FILE_NAME = EMAILS().GENERATE_RANDOM_FILENAME()
                        if CHOOSE in ["1", "01"]:
                            self.STATUS = EMAILS().RANDOM_STRING(
                                self.DOMAIN, self.COUNT, self.FILE_NAME, 10
                            )
                        elif CHOOSE in ["2", "02"]:
                            self.STATUS = EMAILS().MIMESIS(
                                self.DOMAIN, self.COUNT, self.FILE_NAME
                            )
                        elif CHOOSE in ["3", "03"]:
                            self.STATUS = EMAILS().FAKER(
                                self.DOMAIN, self.COUNT, self.FILE_NAME
                            )
                        elif CHOOSE in ["4", "04"]:
                            self.STATUS = EMAILS().NAMES(
                                self.DOMAIN, self.COUNT, self.FILE_NAME
                            )
                        else:
                            self.STATUS = EMAILS().RANDOM_USER(
                                self.DOMAIN, self.COUNT, self.FILE_NAME
                            )
                        if bool(self.STATUS) == True:
                            printf(
                                Panel(
                                    f"[bold white]Successfully created a fake email and we managed to save it in[bold green] {self.FILE_NAME}",
                                    style="bold bright_black",
                                    width=59,
                                    title="[bold bright_black]> [Sukses] <",
                                )
                            )
                            sys.exit()
                        else:
                            printf(
                                Panel(
                                    f"[bold red]Failed to create fake email, please try again and make sure there is a Temporary folder!",
                                    style="bold bright_black",
                                    width=59,
                                    title="[bold bright_black]> [Gagal] <",
                                )
                            )
                            sys.exit()
                    else:
                        printf(
                            Panel(
                                f"[bold red]You entered too few numbers, please fill in at least more than 100 emails for optimal results!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Jumlah Salah] <",
                            )
                        )
                        sys.exit()
            elif CHOOSE in ["6", "06"]:
                printf(
                    Panel(
                        f"[bold white]You must fill in the name of the file you want to check whether the email is valid or not, for example:[bold green] Temporary/Example.txt[bold white] *make sure the file is available!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Nama File] <",
                        subtitle="[bold bright_black]╭───────",
                        subtitle_align="left",
                    )
                )
                self.FILE_NAME = Console().input("[bold bright_black]   ╰─> ")
                if os.path.exists(self.FILE_NAME) == True:
                    if len(open(self.FILE_NAME, "r").readlines()) >= 1:
                        self.SAVE_FILES = str(
                            EMAILS().GENERATE_RANDOM_FILENAME()
                        ).replace(".txt", "")
                        self.FILE_LIVE, self.FILE_DIE = (
                            f"{self.SAVE_FILES}_Live.txt",
                            f"{self.SAVE_FILES}_Die.txt",
                        )
                        printf(
                            Panel(
                                f"[bold white]You can wait for a few minutes, if there is an error, the service is probably not working properly.\nWe recommend registering with Gmail to make it work!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Catatan] <",
                            )
                        )
                        for EMAIL in open(self.FILE_NAME, "r").read().splitlines():
                            try:
                                CHECKER().EMAIL(
                                    [f"{EMAIL}"], self.FILE_LIVE, self.FILE_DIE
                                )
                            except (KeyboardInterrupt):
                                printf(
                                    f"\r                                       ",
                                    end="\r",
                                )
                                break
                        printf(
                            Panel(
                                f"[bold white]Congratulations, you have successfully obtained[bold green] {len(LIVE)}[bold white] live emails and[bold red] {len(DIE)}[bold white] dead emails, all results have been saved in[bold yellow] {self.FILE_LIVE}[bold white] and[bold yellow] {self.FILE_DIE}[bold white]!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [Selesai] <",
                            )
                        )
                        sys.exit()
                    else:
                        printf(
                            Panel(
                                f"[bold red]The file you entered is empty, please use another file and make sure it contains an email list!",
                                style="bold bright_black",
                                width=59,
                                title="[bold bright_black]> [File Kosong] <",
                            )
                        )
                        sys.exit()
                else:
                    printf(
                        Panel(
                            f"[bold red]The file name you entered is not available, please try again and fill in the file name correctly!",
                            style="bold bright_black",
                            width=59,
                            title="[bold bright_black]> [File Tidak Ada] <",
                        )
                    )
                    sys.exit()
            elif CHOOSE in ["7", "07"]:
                printf(
                    Panel(
                        f"[bold white]You have selected the exit option, thank you for using this program, hope you enjoy it!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Keluar] <",
                    )
                )
                sys.exit()
            else:
                printf(
                    Panel(
                        f"[bold red]The option you selected is not in the features, please try again and see the features list!",
                        style="bold bright_black",
                        width=59,
                        title="[bold bright_black]> [Pilihan Salah] <",
                    )
                )
                time.sleep(4.5)
                self.UTAMA()
        except (Exception) as e:
            printf(
                Panel(
                    f"[bold red]{str(e).capitalize()}!",
                    style="bold bright_black",
                    width=59,
                    title="[bold bright_black]> [Error] <",
                )
            )
            sys.exit()

    def TAMPILKAN_LOGO(self):
        os.system("cls" if os.name == "nt" else "clear")
        printf(
            Panel(
                r"""[bold red]    ______    _          __  __       _ _           
   |  ____|  | |        |  \/  |     (_) |          
   | |__ __ _| | _____  | \  / | __ _ _| | ___ _ __ 
   |  __/ _` | |/ / _ \ | |\/| |/ _` | | |/ _ \ '__|
   | | | (_| |   <  __/ | |  | | (_| | | |  __/ |   
   [bold white]|_|  \__,_|_|\_\___| |_|  |_|\__,_|_|_|\___|_|   
          [underline green]Fake Email Generator - by Rozhak""",
                style="bold bright_black",
                width=59,
            )
        )
        return False


class CHECKER:
    def __init__(self) -> None:
        pass

    def EMAIL(self, email, file_live, file_die):
        global LIVE, DIE, UNKNOWN, LOOPING
        try:
            for EMAIL in email:
                if "@" in EMAIL and "." in EMAIL:
                    with requests.Session() as session:
                        session.headers.update(
                            {
                                "Accept-Language": "en-US,en;q=0.9",
                                "Sec-Fetch-Site": "same-origin",
                                "Sec-Fetch-Mode": "cors",
                                "Sec-Fetch-Dest": "empty",
                                "Host": "ychecker.com",
                                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
                            }
                        )
                        params = {
                            "email": f"{EMAIL}",
                        }
                        response = session.get(
                            "https://ychecker.com/app/payload?",
                            params=params,
                            allow_redirects=True,
                        )
                        if '"items":' in str(response.text):
                            self.JSON_ITEMS = json.loads(response.text)["items"]
                            session.headers.update(
                                {
                                    "Sec-Fetch-Site": "cross-site",
                                    "Origin": "https://ychecker.com",
                                    "Host": "app.sonjj.com",
                                }
                            )
                            params = {
                                "payload": f"{self.JSON_ITEMS}",
                            }
                            response2 = session.get(
                                "https://app.sonjj.com/v1/check_email/?",
                                params=params,
                                allow_redirects=True,
                            )
                            if '"status":"Ok"' in str(response2.text):
                                try:
                                    self.DISPOSABLE, self.TYPE = (
                                        json.loads(response2.text)["disposable"],
                                        json.loads(response2.text)["type"],
                                    )
                                except (Exception):
                                    self.DISPOSABLE, self.TYPE = ("null", "null")
                                printf(
                                    Panel(
                                        f"""[bold white]Disposable :[bold green] {str(self.DISPOSABLE).capitalize()}
[bold white]Email :[bold red] {EMAIL}
[bold white]Type :[bold yellow] {str(self.TYPE).upper()}""",
                                        style="bold bright_black",
                                        width=59,
                                        title="[bold bright_black][bold bright_black]> [[bold green]Live[bold bright_black]] <",
                                    )
                                )
                                LIVE.append(f"{EMAIL}")
                                open(file_live, "a+").write(f"{EMAIL}\n")
                                break
                            elif '"status":"NotExist"' in str(response2.text):
                                try:
                                    self.DISPOSABLE, self.TYPE = (
                                        json.loads(response2.text)["disposable"],
                                        json.loads(response2.text)["type"],
                                    )
                                except (Exception):
                                    self.DISPOSABLE, self.TYPE = ("null", "null")
                                printf(
                                    Panel(
                                        f"""[bold white]Disposable :[bold green] {str(self.DISPOSABLE).capitalize()}
[bold white]Email :[bold red] {EMAIL}
[bold white]Type :[bold yellow] {str(self.TYPE).upper()}""",
                                        style="bold bright_black",
                                        width=59,
                                        title="[bold bright_black][bold bright_black]> [[bold red]Die[bold bright_black]] <",
                                    )
                                )
                                DIE.append(f"{EMAIL}")
                                open(file_die, "a+").write(f"{EMAIL}\n")
                                break
                            elif "Invalid credentials" in str(response2.text):
                                printf(
                                    f"[bold bright_black]   ──>[bold yellow] TURN ON AIRPLANE MODE FOR ONE SECOND!",
                                    end="\r",
                                )
                                time.sleep(7.5)
                            else:
                                UNKNOWN.append(f"{EMAIL}")
                                continue
                        else:
                            UNKNOWN.append(f"{EMAIL}")
                            continue
                else:
                    UNKNOWN.append(f"{EMAIL}")
                    continue
            LOOPING += 1
            printf(
                f"[bold bright_black]   ──>[bold green] @{str(EMAIL).split('@')[0].upper()}[bold white]/[bold blue]{LOOPING}[bold white] LIVE:-[bold green]{len(LIVE)}[bold white] DIE:-[bold red]{len(DIE)}[bold white] BAD:-[bold yellow]{len(UNKNOWN)}[bold white]     ",
                end="\r",
            )
        except (requests.exceptions.RequestException):
            printf(
                f"[bold bright_black]   ──>[bold red] YOUR CONNECTION HAS BEEN DISCONNECTED!",
                end="\r",
            )
            time.sleep(10.0)
        except (Exception) as e:
            printf(f"[bold bright_black]   ──>[bold red] {str(e).upper()}!", end="\r")
            time.sleep(5.5)


class EMAILS:
    def __init__(self) -> None:
        pass

    def RANDOM_STRING(self, domain, count, file_name, length):
        try:
            for _ in range(int(count)):
                self.USERNAME = "".join(
                    random.choices(string.ascii_lowercase + string.digits, k=length)
                )
                self.EMAIL = f"{self.USERNAME}{domain}"
                open(f"{file_name}", "a+").write(f"{self.EMAIL}\n")
                printf(
                    f"[bold bright_black]   ──>[bold white] DUMP[bold green] {self.EMAIL}[bold white]/[bold green]{len(open(file_name, 'r').readlines())}[bold white] EMAIL!     ",
                    end="\r",
                )
                time.sleep(0.007)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True
        except (KeyboardInterrupt):
            printf(
                f"[bold bright_black]   ──>[bold red] DUMP HAS STOPPED!              ",
                end="\r",
            )
            time.sleep(3.5)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True

    def MIMESIS(self, domain, count, file_name):
        try:
            for _ in range(int(count)):
                self.PERSON = Person(Locale.EN)
                self.EMAIL = self.PERSON.email(domains=[f"{domain}"])
                open(f"{file_name}", "a+").write(f"{self.EMAIL}\n")
                printf(
                    f"[bold bright_black]   ──>[bold white] DUMP[bold green] {self.EMAIL}[bold white]/[bold green]{len(open(file_name, 'r').readlines())}[bold white] EMAIL!     ",
                    end="\r",
                )
                time.sleep(0.007)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True
        except (KeyboardInterrupt):
            printf(
                f"[bold bright_black]   ──>[bold red] DUMP HAS STOPPED!              ",
                end="\r",
            )
            time.sleep(3.5)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True

    def FAKER(self, domain, count, file_name):
        try:
            for _ in range(int(count)):
                self.FAKE = Faker("id_ID")
                self.EMAIL = self.FAKE.email(domain=domain.replace("@", ""))
                open(f"{file_name}", "a+").write(f"{self.EMAIL}\n")
                printf(
                    f"[bold bright_black]   ──>[bold white] DUMP[bold green] {self.EMAIL}[bold white]/[bold green]{len(open(file_name, 'r').readlines())}[bold white] EMAIL!     ",
                    end="\r",
                )
                time.sleep(0.007)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True
        except (KeyboardInterrupt):
            printf(
                f"[bold bright_black]   ──>[bold red] DUMP HAS STOPPED!              ",
                end="\r",
            )
            time.sleep(3.5)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True

    def NAMES(self, domain, count, file_name):
        try:
            for _ in range(int(count)):
                self.GENDER = random.choice(["male", "female"])
                self.FIRST_NAME = names.get_first_name(gender=self.GENDER).lower()
                self.LAST_NAME = names.get_last_name().lower()

                self.EMAIL = f"{self.FIRST_NAME}.{self.LAST_NAME}{domain}"
                open(f"{file_name}", "a+").write(f"{self.EMAIL}\n")
                printf(
                    f"[bold bright_black]   ──>[bold white] DUMP[bold green] {self.EMAIL}[bold white]/[bold green]{len(open(file_name, 'r').readlines())}[bold white] EMAIL!     ",
                    end="\r",
                )
                time.sleep(0.007)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True
        except (KeyboardInterrupt):
            printf(
                f"[bold bright_black]   ──>[bold red] DUMP HAS STOPPED!              ",
                end="\r",
            )
            time.sleep(3.5)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True

    def RANDOM_USER(self, domain, count, file_name):
        try:
            for _ in range(int(count)):
                self.USER = RandomUser()
                self.EMAIL = str(self.USER.get_email()).replace("@example.com", domain)
                open(f"{file_name}", "a+").write(f"{self.EMAIL}\n")
                printf(
                    f"[bold bright_black]   ──>[bold white] DUMP[bold green] {self.EMAIL}[bold white]/[bold green]{len(open(file_name, 'r').readlines())}[bold white] EMAIL!     ",
                    end="\r",
                )
                time.sleep(0.007)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True
        except (KeyboardInterrupt):
            printf(
                f"[bold bright_black]   ──>[bold red] DUMP HAS STOPPED!              ",
                end="\r",
            )
            time.sleep(3.5)
            if len(open(file_name, "r").readlines()) == 0:
                return False
            else:
                return True

    def GENERATE_RANDOM_FILENAME(self, length=9, extension=".txt"):
        self.RANDOM_FILE_NAME = f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=length))}{extension}"
        with open(f"Temporary/{self.RANDOM_FILE_NAME}", "w") as W:
            W.write("")
        W.close()
        return f"Temporary/{self.RANDOM_FILE_NAME}"


if __name__ == "__main__":
    try:
        os.system("git pull")
        FITUR().UTAMA()
    except (Exception) as e:
        printf(
            Panel(
                f"[bold red]{str(e).capitalize()}!",
                style="bold bright_black",
                width=59,
                title="[bold bright_black]> [Error] <",
            )
        )
        sys.exit()
    except (KeyboardInterrupt):
        sys.exit()