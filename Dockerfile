FROM python:3.6.6
COPY ./server /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python ./app.py

FROM node:8 as nodebuild
COPY ./client /client
WORKDIR /client
RUN npm install
RUN npm rebuild node-sass
RUN npm run build
WORKDIR /client/dist
EXPOSE 8080
