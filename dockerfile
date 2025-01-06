# minimum python version
FROM python:3.13-slim

# setting environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# installing system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# setting work dir
WORKDIR /app

# installing application dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# copying the application code
COPY . /app/

# collecting static files
RUN python manage.py collectstatic --noinput

# launching gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "recruitment_task_nask.wsgi:application"]
