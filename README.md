# Edulink

Edulink is a web application that provides access to educational videos from YouTube. It aims to offer users a platform to discover and learn from a variety of educational content available on YouTube.

## Overview

Edulink is a Flask-based web application that uses the YouTube API to fetch and display educational videos. The application is organized using blueprints and follows a modular structure to manage views, authentication, and database models.

## Features

- Landing page to introduce the concept of the platform.
- Home page for users to explore subjects and access educational content.
- Subject-specific pages (e.g., Math, Science, History) to view relevant videos.
- User registration and login functionalities.
- Integration with YouTube API to fetch educational videos dynamically.

## Prerequisites

Before running the application, make sure you have the following dependencies:

- Python 3.x
- Flask
- Flask SQLAlchemy
- Flask Login
- Werkzeug

Install the dependencies using:

```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (recommended).
4. Install the dependencies using the command mentioned in the prerequisites section.
5. Create the database by running the following command:

```bash
python app.py
```

## Usage

1. Run the application: http://carlhiramyaro.pythonanywhere.com/

## API Integration

Edulink integrates the YouTube API to fetch educational videos. The `fetch_youtube_data` function in the `views.py` file interacts with the API to retrieve relevant video data based on the subject.

## Authors

- Carl Hiram Yaro
- Noro Dung
