def exemplo01():
    print("\n\t\t\t\t------- EXEMPLO 01 -------\n")

    alien_0 = {
        'color': 'green',
        'points': 5
    }

    print(alien_0['color'])
    print(alien_0['points'])
    new_point = alien_0['points']
    print(f"You just earned {new_point} points!")
    print()

    alien_0['x_position'] = 0
    alien_0['y_position'] = 25

    print(alien_0)
    print()

    alien_0['color'] = 'yellow'
    print(f"The alien is now {alien_0['color']}.")
    print()

    alien_0['speed'] = 'medium'
    print(f"Original x_position {alien_0['x_position']}")

    if alien_0['speed'] == 'slow': x_increment = 1
    elif alien_0['speed'] == 'medium': x_increment = 2
    else: x_increment = 3
    alien_0['x_position'] += x_increment

    print(f"New x_position: {alien_0['x_position']}")

    del alien_0['points']

    print(alien_0)
    print('\n', 50*'=-=', '\n')

def exemplo02():
    print("\n\t\t\t\t------- EXEMPLO 02 -------\n")

    user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
    }
    for key, value in user_0.items():
        print( key, value)

    print()

    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for name, language in favorite_languages.items():
        print(f"{name.title()}'s favorite language is {language.title()}")

    print()
    frinds = ['phil', 'sarah']
    for name in favorite_languages.keys():
        print(name.title())
        if name in frinds:
            print(f" Hi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

    print()
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

    print()
    for name in sorted(favorite_languages.keys()):
        print(f"{name.title()}, thank you for taking the poll.")

    print()
    print("The following languages have been mentioned:")
    for languege in favorite_languages.values():
        print(languege.title())

    print()
    for languege in sorted(set(favorite_languages.values())):
        print(languege.title())

    print('\n', 50 * '=-=', '\n')

def exemplo03():
    print("\n\t\t\t\t------- EXEMPLO 03 -------\n")

    alien_0 = {'color': 'green',
               'points': 5
               }

    alien_1 = {'color': 'yellow',
               'points': 10
               }

    alien_2 = {'color': 'red',
               'points': 15
               }

    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)
    print()

    aliens = []
    for alien_number in range(30):
        new_alien = {'color': 'green',
                     'points': 5,
                     'speed': 'slow',
                     }
        aliens.append(new_alien)
    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['speed'] = 'mediun'
            alien['points'] = 10
    for alien in aliens[:5]:
        print(alien)
    print("...")

    print(f"\n{30*' * '}\n")

    for alien in aliens[0:3]:
        if alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['speed'] = 'fast'
            alien['points'] = 15
    for alien in aliens[:5]:
        print(alien)
    print("...")
    print(f"Total number of aliens: {len(aliens)}")

    print(f"\n{30 * ' * '}\n")

    pizza = {
        'crust': 'thick',
        'toppings': ['mushrooms', 'extra cheese'],
    }
    print(f"You ordered a {pizza['crust']}-crust pizza with the following toppings:")
    for topping in pizza['toppings']:
        print(f"\t{topping}")
    print()
    print(f"\n{30 * ' * '}\n")

    favorite_languages = {
        'jen': ['python', 'ruby'],
        'sarah': ['c'],
        'edward': ['ruby', 'go'],
        'phil': ['python', 'haskell'],
    }
    for name, languages in favorite_languages.items():
        print(f"\n{name.title()}'s favorite languages ", end='')
        if len(languages) == 1:
            print("is:")
            for language in languages:
                print(f"\t{language.title()}")
        else:
            print("are:")
            for language in languages:
                print(f"\t{language.title()}")
    print()
    print(f"\n{30 * ' * '}\n")

    users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
        },

        'mcurie': {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
        },
    }
    for username, user_info in users.items():
        print(f"\nUsername: {username}")
        full_name = f"{user_info['first']} {user_info['last']}"
        location = user_info['location']

        print(f"Full name: {full_name.title()}")
        print(f"\tLocatiom: {location.title()}")

    print('\n', 50 * '=-=', '\n')



exemplo01()
exemplo02()
exemplo03()
