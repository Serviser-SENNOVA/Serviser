FROM node:14
LABEL authors="BMO"

WORKDIR /app
COPY package.json /app/

RUN npm install
COPY ../frontend-mio /app/

EXPOSE 3000

CMD ["npm", "start"]