from controller.MainController import MainController

def main():

    controller = MainController()
    result = controller.fetchUsers()
    print("hello")

if __name__ == "__main__":
    main()
    #controller.fetchUsers()