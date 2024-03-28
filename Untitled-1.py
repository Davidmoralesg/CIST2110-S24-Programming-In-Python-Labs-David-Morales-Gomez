
input_snake = input(str("=====>~"))
print("a. Make snake bigger")
print("b. Make snake smaller")
print("q. Exit")
def main():
    snake = '=====>~'
    print(snake)
    while True:
        print('a. Make snake bigger')
        print('b. Make snake smaller')
        print('q. Exit')
        choice = input('Enter your choice: ')
        if choice == 'a':
            snake += '='
        elif choice == 'b':
            if len(snake) > 1:
                snake = snake[:-1]
            else:
                print("Snake can't get any smaller!")
        elif choice == 'q':
            break
        else:
            print('Invalid choice')
        print('snake is now:')
        print(snake)
    
main()
print("Goodbye!")