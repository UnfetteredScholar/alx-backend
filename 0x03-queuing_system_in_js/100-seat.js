import { createClient } from 'redis';
import { promisify } from 'util';
import { createQueue } from 'kue';

const express = require('express');

const app = express();
const PORT = 1245;
const client = createClient();
const queue = createQueue();
let reservationEnabled = true;

function reserveSeat(number) {
  const set = promisify(client.set).bind(client);

  return set('available_seats', number);
}

function getCurrentAvailableSeats() {
  const get = promisify(client.get).bind(client);

  return get('available_seats');
}

client.on('connect', () => {
  reserveSeat(50);
});

app.get('/available_seats', async (req, res) => {
  const seats = await getCurrentAvailableSeats();

  res.json({ numberOfAvailableSeats: (seats || 0) });
});

app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
  } else {
    try {
      const job = queue.createJob('reserve_seat');

      job.on('failed', (err) => {
        console.log(`Seat reservation job ${job.id} failed: ${err.message || err.toString()}`);
      });

      job.on('complete', () => {
        console.log(`Seat reservation job ${job.id} completed`);
      });

      job.save();
      res.json({ status: 'Reservation in process' });
    } catch (err) {
      res.json({ status: 'Reservation failed' });
    }
  }
});

app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    let seats = await getCurrentAvailableSeats();
    seats = Number.parseInt(seats || 0) - 1;

    if (seats <= 0) {
      reservationEnabled = false;
    }

    if (seats >= 0) {
      reserveSeat(seats);
      done();
    } else {
      done(new Error('Not enough seats available'));
    }
  });
});

app.listen(PORT);
