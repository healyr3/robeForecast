FROM node:16-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --configuration production

FROM nginx:alpine
COPY --from=build /app/dist/robe-forecast-frontend /usr/share/ngix/html
EXPOSE 80
CMD ["ngix", "-g", "daemon off;"]
