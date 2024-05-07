import { createClient } from 'redis';

// const redisClient = await reateClient()
// .on('error', (err) => {console.log(`Redis client not connected to the server: ${err}`)})

async function main() {
  const client = await createClient();

  client.on('error', (err) => { console.log(`Redis client not connected to the server: ${err}`); });
  client.on('connect', () => { console.log('Redis client connected to the server'); });
}

main();
