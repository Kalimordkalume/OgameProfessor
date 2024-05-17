from classes.account import Account


class Main:
    def main():
        x = Account()
        x.gather_account_data()

        print(x.planet_list)


if __name__ == "__main__":
    Main.main()
