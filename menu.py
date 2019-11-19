def menu_with_handlers(message, options='1235', handlers = []):
    answer = input(message)
    answer = answer.upper()
    if answer[0] in options.upper():
        if handlers != '' and (len(options) == len(handlers)):
            index = options.index(answer[0])
            print('calling', handlers[index].__name__)
            handlers[index]()

        return answer, True

    return answer, False


def d():
    print('d')


def a():
    print('a')


def main():
    handlers = [a, d, a]
    question = 'blerp? '
    answer, success = menu_with_handlers(question, '123', handlers)
    print(answer, success)


main()
