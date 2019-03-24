FROM node:8 as nodebuild
COPY ./client /client
WORKDIR /client
RUN npm install
RUN npm rebuild node-sass
RUN npm run build

FROM python:3.6.6
COPY ./server /app
COPY --from=nodebuild /build /app/build
WORKDIR /app
RUN pip install pipenv
RUN pipenv install --skip-lock

CMD ["pipenv", "run", "gunicorn", "-k", "gevent", "-b", "0.0.0.0:8080", "wsgi:app"]