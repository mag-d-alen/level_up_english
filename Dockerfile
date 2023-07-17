# Pull base image
FROM python:3.10.4-slim-bullseye
# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /code
# Install Chrome and ChromeDriver
RUN apt-get update && apt-get install -yq \
    curl \
    unzip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb \
    && dpkg -i chrome.deb || apt-get -fy install \
    && rm -f chrome.deb

RUN CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && curl -sSL "https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip" -o chromedriver.zip \
    && unzip chromedriver.zip \
    && chmod +x chromedriver \
    && mv chromedriver /usr/local/bin/chromedriver \
    && rm -f chromedriver.zip

# Set up your app and dependencies
WORKDIR /app
# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your code into the container
COPY . .

# Set the entrypoint or CMD to run your application
CMD ["python", "your_script.py"]




COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Copy project
COPY . .