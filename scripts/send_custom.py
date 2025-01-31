import requests
import os


html_file = input('Enter HTML file path: ')
if not os.path.isfile(html_file):
    print('File not found')
else:
    newsletter_num = input('Newsletter number: ')
    title = input('Newsletter title: ')
    testing = input('Send test? [Y|n] ')

    print()

    print(f'File path: {html_file}\nNumber: {newsletter_num}\nTitle: {title}\nSend testing: {testing}\n\n')
    cont = input('Continue? [Y|n] ')

    if cont.lower() == 'y':
        response = requests.post(
            'http://127.0.0.1:8000/send',
            files={'email': open(html_file)},
            data={
                'number': newsletter_num,
                'title': title,
                'testing': testing.lower() != 'n'
            }
        )

        if response.status_code == 200:
            print('Success!')
        else:
            print(f'Failed with code {response.status_code}')