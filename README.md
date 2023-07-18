# what2drive

What2Drive is a Python-based tool that helps you efficiently manage and organize your documents by automatically saving them to Google Drive and providing relevant insights.

## Features

- **Automated Document Saving**: Save document images to Google Drive with appropriate file names.
- **Content Detection**: Detect and suggest updates for image file names based on the content of invoices.
- **Summarization**: Generate summaries of document contents to quickly grasp essential information.
- **Efficient Tracking**: Keep track of invoices and other important documents effortlessly.
- **Customizable**: Easily adapt the tool to your specific document management needs.

#  Prerequisite are  Node.js and Google Drive api 

To install Node.js, follow these steps:

1. Visit the official Node.js website at [nodejs.org](https://nodejs.org).

2. On the homepage, you will see two versions available for download: LTS (Long Term Support) and Current. 

   - For most users, it is recommended to download the LTS version, as it provides stability and long-term support. Click on the "LTS" button to download the latest LTS version.
   
   - If you specifically require the latest features and updates, you can choose the Current version.

3. Once you click on the download button, the installer package will start downloading based on your operating system (Windows, macOS, or Linux).

4. After the download is complete, locate the installer package in your downloads folder and run it.

5. Follow the instructions provided by the installer. By default, the installer will install Node.js and npm (Node Package Manager) on your system.

6. During the installation process, you may be asked to accept the terms and conditions and choose the installation location. You can generally leave the default settings as they are.

7. Once the installation is complete, you can verify the installation by opening a new terminal or command prompt window and running the following commands:

   - To check the installed version of Node.js:
     ```
     node --version
     ```

   - To check the installed version of npm:
 -------------------------------------------------------------------------------------------------------------

to setting upgoogle drive you can watch this you tube video : https://youtu.be/G_4KUbuwtlM


## Installation

1. Clone the repository:

   ```
   git clone https://github.com/onk2cell/what2drive.git
   ```

2. Navigate to the project directory:

   ```
   cd what2drive
   ```

3. Create and activate a virtual environment (optional but recommended):

   ```
   python -m venv env
   source env/bin/activate
   ```

4. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set up Google Drive API credentials:
   
   - Follow the instructions in the  to create and obtain the necessary API credentials.
   - Save the credentials file as `credentials.json` in the project directory.

2. Customize the configuration:

   - Open `config.json` and update the settings as per your requirements.

3. Run the program:

   ```
   python watchbitch.py
   ```

   This will start the What2Drive tool and perform the necessary operations based on your configuration.

## Contribution

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to submit a pull request or open an issue in the GitHub repository.


.


