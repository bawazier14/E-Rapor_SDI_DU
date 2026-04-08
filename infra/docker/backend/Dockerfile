FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libpango-1.0-0 \
    libpangoft2-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Install dependencies
COPY backend/requirements/base.txt backend/requirements/dev.txt ./
RUN pip install --upgrade pip
RUN pip install -r dev.txt

# Copy project
# In development, we use volumes to mount the code, but copying is good practice as a fallback
COPY ./backend /app/

# We don't specify CMD here, we let docker-compose manage it for dev
CMD ["flask", "run", "--host=0.0.0.0"]
