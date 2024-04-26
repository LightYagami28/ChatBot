# IMPORTANT
Since the API has been [discontinued](https://t.me/Intellivoid/559), this will no longer work. 
![Discontinued](https://img.shields.io/badge/-DISCONTINUED-red?style=for-the-badge)

# About
A fun Telegram userbot originally written in Python 3, utilizing [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API.
Written by [this person](https://t.me/TheRealPhoenix)!

## Installation
Open your terminal and follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/rsktg/Chatbot.git
    ```

2. Navigate to the Chatbot directory:
    ```bash
    cd Chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Non-Heroku users
Edit the `NAME` variable in `generate_session.py` to your desired bot name.

Run the following command:
```bash
python3 generate_session.py
```

### Heroku users
Run the following command:
```bash
python3 string_session.py
```

You'll be prompted to enter your phone number and 2FA password (if applicable). Copy and save the string session generated at the end.
=======
# About ℹ️
Welcome to our Telegram userbot, meticulously crafted in Python 3 and powered by [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API. This masterpiece is the brainchild of [this illustrious individual](https://t.me/TheRealPhoenix)!

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

4. Duplicate the `sample_config.ini` file and rename the duplicate to `config.ini`. Then, fill in your `api_id` and `api_hash`, which you can obtain from [here](https://my.telegram.org).

5. Run the `string_session.py` script:
    ```bash
    python3 string_session.py
    ```

    Follow the prompts to enter your phone number and 2FA password (if applicable). Once completed, make sure to save the string session generated at the end.

### Configuration Options ⚙️
You have two pathways for configuration:

- **Using Environment Variables:**
    Set up a variable named `ENV` with any desired value. Now you can utilize environment variables. Include the following:

    - `STRING_SESSION`: The string session obtained earlier.
    - `CF_API_KEY`: Obtain this API key from [here](https://t.me/IntellivoidDev).
    - `DATABASE_URL`: Your SQL database URL, which should resemble something like this: `sqldbtype://username:pw@hostname:port/db_name`. PostgreSQL is recommended.
    - `NAME`: Your bot will respond to AI-enabled users whenever this name is mentioned.

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
>>>>>>> Stashed changes
=======
# IMPORTANT
Since the API has been [discontinued](https://t.me/Intellivoid/559), this will no longer work.

# About
A fun Telegram userbot originally written in Python 3, utilizing [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API.
Written by [this person](https://t.me/TheRealPhoenix)!

## Installation
Open your terminal and follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/rsktg/Chatbot.git
    ```

2. Navigate to the Chatbot directory:
    ```bash
    cd Chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Non-Heroku users
Edit the `NAME` variable in `generate_session.py` to your desired bot name.

Run the following command:
```bash
python3 generate_session.py
```

### Heroku users
Run the following command:
```bash
python3 string_session.py
```

You'll be prompted to enter your phone number and 2FA password (if applicable). Copy and save the string session generated at the end.

### Configuration Options
You have two pathways for configuration:

- **Using Environment Variables:**
  Set up a variable named `ENV` with any desired value. Now you can utilize environment variables. Include the following:

  - `SESSION_NAME`: If you ran `generate_session.py`, the name of the session you created.
  - `STRING_SESSION`: The string session (Only for Heroku users).
  - `CF_API_KEY`: You can get this API key from [here](https://coffeehouse.intellivoid.net).
  - `DATABASE_URL`: The URL of your SQL database. Postgres is recommended.
  - `NAME`: If someone sends this name, your bot will reply.

- **Editing the `config.ini` File:**
  Simply set the values mentioned above in the `config.ini` file, excluding `ENV`.

## Running the Bot
After configuring either through environment variables or the `config.ini` file, initiate the bot by running:
```bash
python3 -m chatbot
```
Congratulations! Your bot is now operational!

## Credits
Acknowledgments go to:

- [Intellivoid](https://github.com/intellivoid) for providing the indispensable API utilized in this project.
- [Pyrogram](https://github.com/pyrogram) for serving as the foundational library for this endeavor.
```