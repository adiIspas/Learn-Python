while True:
    try:
        number = int(input('Your number: '))
        print('Your number is', number)
        print('Division', 10/number)
    except ValueError:
        print('Is not a number')
        break
    except ZeroDivisionError:
        print('Not division with 0')
        break
    except:
        break
    finally:
        print('Finish')