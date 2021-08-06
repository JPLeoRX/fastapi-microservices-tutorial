FROM python:3.8

# Install dependencies
RUN pip install requests==2.25.1
RUN pip install injectable==3.4.4
RUN pip install fastapi==0.63.0
RUN pip install uvicorn==0.13.3
RUN pip install SQLAlchemy==1.3.23
RUN pip install yoyo-migrations==7.3.1
RUN pip install psycopg2-binary==2.8.6
RUN pip install simplestr==0.4.1

# Our message protocol
COPY ./shared-mp /shared-mp
WORKDIR /shared-mp
RUN python setup.py sdist bdist_wheel && pip install .

# Our utils
COPY ./shared-utils /shared-utils
WORKDIR /shared-utils
RUN python setup.py sdist bdist_wheel && pip install .

# Main app
COPY ./service-book /app
WORKDIR /app

# Run command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--workers", "1"]