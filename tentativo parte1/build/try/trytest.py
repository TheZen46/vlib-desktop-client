"""
VLib User Dictionary Serializer Test
Utility function for writing user dictionaries to flat text format.
"""

from pathlib import Path


def write_dicts_to_file(user_dicts, file_path):
    target = Path(file_path)
    with open(target, 'w', encoding='utf-8') as file:
        for user_dict in user_dicts:
            for key, value in user_dict.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")


if __name__ == "__main__":
    test_dicts = [
        {
            'username': 'thezen46',
            'password': 'password47sicura',
            'icon_image': str(Path(__file__).resolve().parent.parent / 'assets' / 'frame4' / 'button_10.png'),
            'birthday': '1990-01-01',
            'description': "This is Alice's description.",
        },
        {
            'username': 'Bob',
            'password': 'bob_password',
            'icon_image': 'path/to/bob_icon.jpg',
            'birthday': '1985-05-15',
            'description': "Bob's profile description.",
        }
    ]

    out_file = Path(__file__).resolve().parent.parent.parent / "users.txt"
    write_dicts_to_file(test_dicts, out_file)
    print(f"[trytest] Serialized user records to: {out_file}")
