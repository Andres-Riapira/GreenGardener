import React, { useState } from "react";
import api from "../api/axios";

function Registro() {
  const [form, setForm] = useState({ nombre: "", email: "", password: "" });
  const [mensaje, setMensaje] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post("/usuarios", form);
      setMensaje("✅ Usuario registrado con éxito");
    } catch (error) {
      setMensaje("❌ Error al registrar usuario");
    }
  };

  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-green-700">Registro de Usuario</h2>
      <form className="mt-4 flex flex-col gap-4 max-w-md" onSubmit={handleSubmit}>
        <input type="text" name="nombre" placeholder="Nombre completo"
          className="border p-2 rounded" onChange={handleChange} />
        <input type="email" name="email" placeholder="Correo electrónico"
          className="border p-2 rounded" onChange={handleChange} />
        <input type="password" name="password" placeholder="Contraseña"
          className="border p-2 rounded" onChange={handleChange} />
        <button className="bg-green-600 text-white py-2 rounded">Registrarse</button>
      </form>
      {mensaje && <p className="mt-4">{mensaje}</p>}
    </section>
  );
}

export default Registro;
