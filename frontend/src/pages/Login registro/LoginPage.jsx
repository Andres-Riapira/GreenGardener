import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [form, setForm] = useState({ email: "", password: "" });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Aquí llamas al backend con fetch o axios
    console.log("Iniciando sesión con:", form);
    navigate("/home");
  };

  return (
    <div className="bg-green-900 min-h-screen flex flex-col items-center justify-center text-white">
      <h1 className="text-2xl mb-6 font-bold">Iniciar Sesión</h1>
      <form onSubmit={handleSubmit} className="flex flex-col w-64 space-y-4">
        <input
          type="email"
          name="email"
          placeholder="Correo"
          className="p-2 rounded text-black"
          onChange={handleChange}
        />
        <input
          type="password"
          name="password"
          placeholder="Contraseña"
          className="p-2 rounded text-black"
          onChange={handleChange}
        />
        <button type="submit" className="bg-lime-400 text-black py-2 rounded font-bold">
          Ingresar
        </button>
        <button
          type="button"
          onClick={() => navigate("/register")}
          className="bg-lime-600 py-2 rounded font-bold"
        >
          Crear Cuenta
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
