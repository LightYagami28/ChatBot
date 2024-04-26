<<<<<<< HEAD
<<<<<<< Updated upstream
=======
>>>>>>> 79e2153a8319d46fb200e642438f2dfb9ee21c9c
# IMPORTANT
Since the API has been [discontinued](https://t.me/Intellivoid/559), this will no longer work. 

# About
A fun telegram userbot written in python3 using [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API.
Written by [this person](https://t.me/TheRealPhoenix)!
## Installation
Open up your terminal and run these commands.
=======
# About ℹ️
Welcome to our Telegram userbot, meticulously crafted in Python 3 and powered by [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API. This masterpiece is the brainchild of [this illustrious individual](https://t.me/TheRealPhoenix)!
>>>>>>> Stashed changes

## Installation 🔧
Let's embark on the installation journey together:

1. Clone the repository:
    ```bash
    git clone https://github.com/rsktg/Chatbot.git
    ```

2. Navigate into the Chatbot directory:
    ```bash
    cd Chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

<<<<<<< Updated upstream
### Non-Heroku users
Edit ```NAME``` in ```generate_session.py```

• ```python3 generate_session.py```

### Heroku users
• ```python3 string_session.py```

You'll be asked to enter your phone number and 2FA password (if any). Copy and save the string session you get in the end.
=======
4. Duplicate the `sample_config.ini` file and rename the duplicate to `config.ini`. Then, fill in your `api_id` and `api_hash`, which you can obtain from [here](https://my.telegram.org).
>>>>>>> Stashed changes

5. Run the `string_session.py` script:
    ```bash
    python3 string_session.py
    ```

    Follow the prompts to enter your phone number and 2FA password (if applicable). Once completed, make sure to save the string session generated at the end.

### Configuration Options ⚙️
You have two pathways for configuration:

<<<<<<< Updated upstream
• ```SESSION_NAME```: If you ran ```generate_session.py```, the name of the session you created.

• ```STRING_SESSION```: The string session (Only for Heroku users).

• ```CF_API_KEY```: You can get this API key from [here](https://coffeehouse.intellivoid.net)
=======
- **Using Environment Variables:**
    Set up a variable named `ENV` with any desired value. Now you can utilize environment variables. Include the following:

    - `STRING_SESSION`: The string session obtained earlier.
    - `CF_API_KEY`: Obtain this API key from [here](https://t.me/IntellivoidDev).
    - `DATABASE_URL`: Your SQL database URL, which should resemble something like this: `sqldbtype://username:pw@hostname:port/db_name`. PostgreSQL is recommended.
    - `NAME`: Your bot will respond to AI-enabled users whenever this name is mentioned.
>>>>>>> Stashed changes

- **Editing the `config.ini` File:**
    Simply set the values mentioned above in the `config.ini` file, excluding `ENV`.

## Running the Bot ▶️
After configuring either through environment variables or the `config.ini` file, initiate the bot by running:
```bash
python3 -m chatbot
```
Congratulations! Your bot is now operational!

## Credits 🌟
Acknowledgments go to:

- [Intellivoid](https://github.com/intellivoid) for providing the indispensable API utilized in this project.
- [Pyrogram](https://github.com/pyrogram) for serving as the foundational library for this endeavor.