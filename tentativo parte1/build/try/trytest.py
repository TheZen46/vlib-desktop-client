def write_dicts_to_file(user_dicts, file_path):
    with open(file_path, 'w') as file:
        for user_dict in user_dicts:
            for key, value in user_dict.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")


user_dicts = [
    {
        'username': 'thezen46',
        'password': 'password47sicura',
        'icon_image': 'F:/partizione alessandro/programmi+/tentativo parte1/build/assets/frame4/button_10.png',
        'birthday': '1990-01-01',
        'description': 'This is Alice\'s description.',
    },
    {
        'username': 'Bob',
        'password': 'bob_password',
        'icon_image': 'path/to/bob_icon.jpg',
        'birthday': '1985-05-15',
        'description': 'Bob\'s profile description.',
    }
]

file_path = 'users.txt'
write_dicts_to_file(user_dicts, file_path)
