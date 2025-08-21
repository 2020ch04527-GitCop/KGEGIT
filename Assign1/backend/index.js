/**
 * backend/index.js
 *
 * Express.js backend server for the Simple E-Commerce app.
 * Handles product and order APIs, and manages SQLite database.
 */
// Import dependencies
const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const PORT = 4000;

app.use(cors());
app.use(bodyParser.json());

// Initialize SQLite DB
// Connect to SQLite database
const db = new sqlite3.Database('./ecommerce.db', (err) => {
  if (err) return console.error(err.message);
  console.log('Connected to SQLite database.');
});

// Initialize tables and seed products if needed
db.serialize(() => {
  db.run(`CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    image TEXT
  )`);
  db.run(`CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    items TEXT,
    total REAL
  )`);
  // Seed initial products
  db.run(`INSERT INTO products (name, price, image) VALUES
    ('T-shirt', 19.99, 'https://via.placeholder.com/150'),
    ('Jeans', 39.99, 'https://via.placeholder.com/150'),
    ('Sneakers', 59.99, 'https://via.placeholder.com/150'),
    ('Jacket', 79.99, 'https://via.placeholder.com/150'),
    ('Hat', 14.99, 'https://via.placeholder.com/150'),
    ('Socks', 4.99, 'https://via.placeholder.com/150')
  `, () => {});
});

// API endpoint: Get all products
app.get('/api/products', (req, res) => {
  db.all('SELECT * FROM products', [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
});

// Place an order
app.post('/api/orders', (req, res) => {
  const { items, total } = req.body;
  db.run('INSERT INTO orders (items, total) VALUES (?, ?)', [JSON.stringify(items), total], function(err) {
    if (err) return res.status(500).json({ error: err.message });
    res.json({ orderId: this.lastID });
  });
});

app.listen(PORT, () => {
  console.log(`Backend running on http://localhost:${PORT}`);
});
