import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="bg-green-700 text-white p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold">🌱 Green Gardener</h1>
      <ul className="flex gap-4">
        <li><Link to="/">Inicio</Link></li>
        <li><Link to="/registro">Registro</Link></li>
        <li><Link to="/plantas">Plantas e Insumos</Link></li>
        <li><Link to="/jardin">Jardín Virtual</Link></li>
        <li><Link to="/servicios">Servicios</Link></li>
        <li><Link to="/consejos">Consejos</Link></li>
        <li><Link to="/comunidad">Comunidad</Link></li>
        <li><Link to="/contacto">Contacto</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
