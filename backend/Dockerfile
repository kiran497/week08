# backend/Dockerfile
FROM node:20-alpine
WORKDIR /app

# If you have package.json in backend/
COPY package*.json ./
RUN npm ci --omit=dev || npm install --production

# Copy the app
COPY . .

EXPOSE 3000
CMD ["npm", "start"]
