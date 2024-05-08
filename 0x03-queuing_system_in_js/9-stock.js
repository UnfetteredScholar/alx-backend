import { createClient } from 'redis';
import { promisify } from 'util';

const express = require('express');

const app = express();
const port = 1245;
const client = createClient();

const listProducts = [
  {
    itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4,
  },
  {
    itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10,
  },
  {
    itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2,
  },
  {
    itemId: 4, itemName: 'Suitcase 1050', price: 450, initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  const item = listProducts.find((value) => value.itemId === id);

  return item;
}

async function reserveStockById(itemId, stock) {
  const set = promisify(client.set).bind(client);

  return set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
  const get = promisify(client.get).bind(client);

  return get(`item.${itemId}`);
}

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId(\\d+)', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    let reserved = await getCurrentReservedStockById(itemId);
    reserved = Number.parseInt(reserved || 0);
    item.currentQuantity = item.initialAvailableQuantity - reserved;

    res.json(item);
  }
});

app.get('/reserve_product/:itemId(\\d+)', async (req, res) => {
  const itemId = Number.parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    let reserved = await getCurrentReservedStockById(itemId);
    reserved = Number.parseInt(reserved || 0);
    item.currentQuantity = item.initialAvailableQuantity - reserved;
    if (item.currentQuantity >= 1) {
      reserveStockById(itemId, reserved + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    } else {
      res.json({ status: 'Not enough stock available', itemId });
    }
  }
});

app.listen(port);
