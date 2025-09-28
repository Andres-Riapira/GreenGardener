import React, { createContext, useState, useContext } from "react";

const CartContext = createContext();

export function CartProvider({ children }) {
  const [cart, setCart] = useState([]);

  // Agregar producto
  const addToCart = (item) => {
    setCart((prevCart) => {
      const exists = prevCart.find((p) => p.id === item.id);
      if (exists) {
        return prevCart.map((p) =>
          p.id === item.id ? { ...p, cantidad: p.cantidad + 1 } : p
        );
      }
      return [...prevCart, { ...item, cantidad: 1 }];
    });
  };

  // Eliminar producto
  const removeFromCart = (id) => {
    setCart((prevCart) => prevCart.filter((p) => p.id !== id));
  };

  // Vaciar carrito
  const clearCart = () => setCart([]);

  // Calcular total
  const getTotal = () =>
    cart.reduce((acc, item) => acc + item.precio * item.cantidad, 0);

  return (
    <CartContext.Provider
      value={{ cart, addToCart, removeFromCart, clearCart, getTotal }}
    >
      {children}
    </CartContext.Provider>
  );
}

export const useCart = () => useContext(CartContext);
