# Backend
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]

# Frontend (React)
FROM node:14
WORKDIR /usr/src/app
COPY ./frontend .
RUN npm install
CMD ["npm", "start"]
