import React from "react";
import { useCart } from "../context/CartContext";

function PlantCard({ id, nombre, descripcion, imagen, precio }) {
  const { addToCart } = useCart();

  return (
    <div className="card flex flex-col items-center text-center">
      {imagen && (
        <img
          src={imagen}
          alt={nombre}
          className="w-32 h-32 object-cover rounded-lg mb-3"
        />
      )}
      <h3 className="text-lg font-semibold text-green-700">{nombre}</h3>
      <p className="text-sm text-gray-600">{descripcion}</p>
      {precio && (
        <p className="mt-2 font-bold text-green-600">💲{precio.toFixed(2)}</p>
      )}
      <button
        className="btn mt-3"
        onClick={() =>
          addToCart({ id, nombre, precio, descripcion, imagen })
        }
      >
        Agregar al carrito
      </button>
    </div>
  );
}

export default PlantCard;
