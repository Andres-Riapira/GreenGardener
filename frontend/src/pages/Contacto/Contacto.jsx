import React from "react";

function Contacto() {
  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-green-700">Contacto</h2>
      <form className="mt-4 flex flex-col gap-4 max-w-md">
        <input type="text" placeholder="Nombre" className="border p-2 rounded" />
        <input type="email" placeholder="Correo" className="border p-2 rounded" />
        <textarea placeholder="Mensaje" className="border p-2 rounded"></textarea>
        <button className="bg-green-600 text-white py-2 rounded">Enviar</button>
      </form>
    </section>
  );
}

export default Contacto;
