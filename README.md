# Virtual Career Advisor Slackbot
## Features

- Utilizes the LangChain framework to integrate with the OpenAI API.
- Provides virtual career advice and guidance.
- Supports interactive conversations with users.
- Offers insights and recommendations on career planning and growth strategies.

## Usage

### Installation

1. Clone the repository:

   ```shell
   git clone git@github.com:agpai2/SlackGPT.git
   ```

2. Install the Python dependencies using pip:

   ```shell
   pip3 install -r requirements.txt
   ```

### Configuration

1. Copy the contents from `.env.local.example` to `.env`:

   ```shell
   cp .env.local.example .env
   ```

2. Edit the `.env` file and provide the necessary configuration values for your environment.

### Running the Slackbot

1. Start the Slackbot application:

   ```shell
   python3 app.py
   ```

2. Ensure that the Slack app is installed and configured in your Slack workspace.
3. Interact with the virtual career advisor by mentioning the bot in a channel or direct message.

### Notes

- The Slackbot uses the Socket mode handler from the Slack API, and therefore, the request URL is not being used at the moment. However, it may be utilized for specific cases in the future.

## Contributions

Contributions are welcome! If you would like to contribute to the project, please follow these steps:

1. Create a new branch for your feature/bug fix.
2. Make the necessary changes and commit them.
3. Submit a pull request detailing the changes you made.

Please ensure that your code adheres to the existing coding style and includes appropriate tests and documentation.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

Feel free to customize the README file according to your specific needs and add any additional information or sections as necessary.