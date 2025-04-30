# Pyonta Mail

## Secret info

* Ask for `.env` file and move to root directory
* Retrieve recipient lists and store in `jpch_data/recipients`
* Make sure not to push the `.env` file to Github (if you do by accident, change the password)

## How to run

### Prerequisites

> **Note:** You should only need to do this once!

1. Install Python 3.10+
2. Install pip
3. In the root directory, create a virtual environment with `python3 -m venv venv`
4. Activate the environment with `source venv/bin/activate`
5. Install deps with `pip3 install requirements.txt`

### Starting/using server

1. Activate virtual environment with `source venv/bin/activate`
2. In terminal 1, start the server with `python3 app.py`
3. In terminal 2, activate venv and run the client script with `python3 scripts/send_custom.py`
4. Follow the prompts in `send_custom.py`
    a. Enter the relative path to the HTML newsletter file (you will get an error if it is not found)
    b. Enter the current newsletter number (check Pyonta's inbox if you've forgotten)
    c. Enter the newsletter title (follow format `Newsletter #XX: Title`)
    d. Always send a test version first! (this will send only to accounts listed as testers)
    e. After confirming the email displays correctly in your inbox, run the script again and confirm no (`n`) for the `Send test?` prompt to send to subscribers

### Adding a subscriber

1. `cd jpch_data/recipients`
2. `python3 add_recipient.py`
3. Follow prompts (add to all, admin, and/or beta testers list)

## Formatting the newsletter

Example base newsletter template is in `templates/base.html`. Feel free to add any extra modifications/templates that might be helpful to have.
