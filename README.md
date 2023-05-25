

# Terminal Interface for Google_Bard

This script provides a terminal interface for interacting with Google_Bard. It allows you to give prompts and receive responses from Google Bard using a command-line interface.

> Note: This script has been tested on Linux only.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3 installed on your system
- The Bard library installed (`pip install bardapi`)
- Valid session Id

    Go to [https://bard.google.com/](https://bard.google.com/)
    - Press F12 to open the developer console
    - Navigate to Application → Cookies → `__Secure-1PSID`. Copy the value of that cookie.
    - Save the session Id for later use.

    ![Demo of getting token](https://github.com/dsdanielpark/Bard-API/blob/main/assets/bard_api.gif)

## Getting Started

1. Clone the script from the repository:

    ```bash
    $ git clone https://github.com/your-repo/bard-interface.git
    ```

2. Navigate to the script directory:

    ```zsh
    $ cd bard-interface
    ```

3. Insert the Session Id

    Open the script file `script.py` and replace the `token` variable with the session Id value you copied from the website.

    > Note: The API token is required to authenticate your requests with the Bard API. Make sure you have obtained a valid token from the Bard website.

4. Set up an alias (Optional)

    To run the script as a command from the terminal, you can set up an alias. Add the following line to your shell profile file (e.g., `~/.bashrc`, `~/.zshrc`):

    ```zsh
    $ alias bard='python3 /path/to/bard-interface/script.py'
    ```

    Replace `/path/to/bard-interface` with the actual path to the script directory.

5. Run the script

    ```bash
    $ bard [prompt]
    ```
    - If you provide a prompt as a command-line argument, the script will use it to generate a response.
        - Example: `bard "What is the capital of France?"`

    or

    ```bash
    $ bard
    ```
    - If no prompt is provided, the script will prompt you to enter a question or query.
        - Example: `bard`

## Examples

Here are some examples of how to use the script:

1. Just ask a question and exit:

    ```bash
    $ bard "What is the capital of France?"
    ```
    ![demo image](https://github.com/mr-alham/projects-of-alham/blob/abe697ac52bc68f95a74ca04c991c08da6ac2f0e/private/carbon(1).png)

2. Enter interactive mode:

    ```bash
    $ bard
    ```
    ![demo image of bard using interactive mode](https://github.com/mr-alham/projects-of-alham/blob/dffbebcd5548392a96c7ae0e14c06a6d1a823c16/private/Google_Bard%20terminal%20interface%20img2.png)

In interactive mode, you can ask multiple questions without restarting the script. Simply type your question or query and press Enter to get the response.

> Note: The script uses the Bard library for generating responses. For more details about the Bard library and its capabilities, please refer to the [GitHub repository](https://github.com/dsdanielpark/Bard-API).

For any further assistance or inquiries, please feel free to contact me at [alham@duck.com](mailto:alham@duck.com).
