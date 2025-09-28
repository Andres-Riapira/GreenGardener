import React from "react";
import { useCart } from "../context/CartContext";

function Carrito() {
  const { cart, removeFromCart, clearCart, getTotal } = useCart();

  return (
    <div className="p-6">
      <h2 className="text-2xl font-bold text-green-700 mb-4">🛒 Carrito</h2>

      {cart.length === 0 ? (
        <p className="text-gray-600">Tu carrito está vacío.</p>
      ) : (
        <div>
          <ul>
            {cart.map((item) => (
              <li
                key={item.id}
                className="flex justify-between items-center bg-white shadow rounded p-3 mb-2"
              >
                <span>
                  {item.nombre} x {item.cantidad}
                </span>
                <span className="font-bold text-green-600">
                  ${item.precio * item.cantidad}
                </span>
                <button
                  className="btn bg-red-600 hover:bg-red-700"
                  onClick={() => removeFromCart(item.id)}
                >
                  ❌
                </button>
              </li>
            ))}
          </ul>

          <div className="mt-4">
            <p className="text-lg font-semibold">
              Total: ${getTotal().toFixed(2)}
            </p>
            <button
              className="btn mt-2 bg-red-700 hover:bg-red-800"
              onClick={clearCart}
            >
              Vaciar Carrito
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Carrito;
