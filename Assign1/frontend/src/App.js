
/**
 * frontend/src/App.js
 *
 * Main React component for the Simple E-Commerce app.
 * Displays products, manages cart, and handles order placement.
 */
import React, { useEffect, useState } from 'react';

// App component
function App() {
  const [products, setProducts] = useState([]);
  const [cart, setCart] = useState([]);
  const [orderId, setOrderId] = useState(null);

  // Fetch products from backend API on mount
  useEffect(() => {
    fetch('http://localhost:4000/api/products')
      .then(res => res.json())
      .then(setProducts);
  }, []);

  // Add product to cart
  const addToCart = (product) => {
    setCart([...cart, product]);
  };

  // Place order by sending cart to backend
  const placeOrder = () => {
    const total = cart.reduce((sum, p) => sum + p.price, 0);
    fetch('http://localhost:4000/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ items: cart, total })
    })
      .then(res => res.json())
      .then(data => {
        setOrderId(data.orderId);
        setCart([]);
      });
  };

  // Render UI
  return (
    <div style={{ maxWidth: 600, margin: 'auto', fontFamily: 'Arial' }}>
  <h1>Urban Style Shop</h1>
  <h2>Products</h2>
  <p>Total products: {products.length}</p>
      <div style={{ display: 'flex', gap: 20 }}>
        {products.map(p => (
          <div key={p.id} style={{ border: '1px solid #ccc', padding: 10 }}>
            <img src={p.image} alt={p.name} width={100} />
            <h3>{p.name}</h3>
            <p>${p.price.toFixed(2)}</p>
            <button onClick={() => addToCart(p)}>Add to Cart</button>
          </div>
        ))}
      </div>
      <h2>Cart ({cart.length})</h2>
      <ul>
        {cart.map((item, i) => (
          <li key={i}>{item.name} - ${item.price.toFixed(2)}</li>
        ))}
      </ul>
      {cart.length > 0 && <button onClick={placeOrder}>Place Order</button>}
      {orderId && <p>Order placed! Your order ID is {orderId}.</p>}
    </div>
  );
}

export default App;
