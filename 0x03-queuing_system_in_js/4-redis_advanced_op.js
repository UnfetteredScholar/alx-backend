import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => { console.log(`Redis client not connected to the server: ${err}`); });

function updateHash(hashKey, key, value) {
  client.hset(hashKey, key, value, print);
}

function printHash(hashKey) {
  client.hgetall(hashKey, (err, res) => { console.log(res); });
}

function main() {
  const dict = {
    Portland: 50,
    Seattle: 80,
    'New York': 20,
    Bogota: 20,
    Cali: 40,
    Paris: 2,
  };

  for (const [key, val] of Object.entries(dict)) {
    updateHash('HolbertonSchools', key, val);
  }

  printHash('HolbertonSchools');
}

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  main();
});
