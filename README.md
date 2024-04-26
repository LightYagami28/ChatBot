# About
A fun Telegram userbot originally written in Python 3, utilizing [Intellivoid](https://github.com/intellivoid)'s Coffeehouse API.
Written by [this person](https://t.me/LightYagami28)!

# Important
We regret to inform you that the Coffeehouse API and associated services are currently offline. However, we are actively working to bring them back online as soon as possible. We apologize for any inconvenience this may cause.

If you're interested in contributing or staying updated on the progress, please feel free to reach out to us using the [Contact](Contact.md) file available in this repository.

Additionally, if you'd like to support our efforts, you can make a donation using the [Donation](Donation.md) file in the same repository. Any donation, no matter how small, is greatly appreciated.

## Installation
Open your terminal and follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/LightOSOFF/Chatbot.git
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

- [Intellivoid](https://github.com/intellivoid) for making the APIs public, enabling the development of this project.
- [Pyrogram](https://github.com/pyrogram) for serving as the foundational library for this endeavor.
- LightOSOFF and the team for redeveloping all the APIs from scratch.