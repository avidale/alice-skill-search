# STEP 1: Install base image. Optimized for Python.
FROM python:3.7-slim-buster
RUN pip install flask mongomock nltk pymongo pyyaml dialogic>=0.3.20 requests sentry-sdk razdel dnspython

# STEP 2: Copy the source code in the current directory to the container.  Store it in a folder named /app.
ADD . /app

# STEP 3: Set working directory to /app so we can execute commands in it
WORKDIR /app

# STEP 4: Install necessary requirements (Flask, etc)
RUN pip install -r requirements.txt

# STEP 5: Declare environment variables
ENV PORT=5000

# STEP 6: Expose the port that Flask is running on
EXPOSE 5000

# STEP 7: Run Flask!
CMD ["python", "main.py"]
