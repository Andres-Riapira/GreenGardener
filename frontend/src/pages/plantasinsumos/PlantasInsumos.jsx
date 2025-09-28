import React, { useEffect, useState } from "react";
import api from "../api/axios";

function PlantasInsumos() {
  const [plantas, setPlantas] = useState([]);

  useEffect(() => {
    const fetchPlantas = async () => {
      try {
        const res = await api.get("/plantas");
        setPlantas(res.data);
      } catch (error) {
        console.error("Error cargando plantas:", error);
      }
    };
    fetchPlantas();
  }, []);

  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-green-700">Plantas e Insumos</h2>
      <ul className="mt-4 grid grid-cols-2 md:grid-cols-3 gap-4">
        {plantas.length > 0 ? (
          plantas.map((planta) => (
            <li key={planta.id} className="border p-3 rounded shadow">
              🌱 {planta.nombre} - {planta.descripcion}
            </li>
          ))
        ) : (
          <p>No hay plantas registradas.</p>
        )}
      </ul>
    </section>
  );
}

export default PlantasInsumos;
