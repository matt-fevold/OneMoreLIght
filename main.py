from OneMoreLight.OneMoreLight.user_input import clean_user_input

def main():
    terminate = False

    while not terminate:
        user_input = input("> ")

        user_input = clean_user_input(user_input)




if __name__ == "__main__":
    main()
