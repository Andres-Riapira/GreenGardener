import React from "react";

function ConsejosPlantas() {
  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-green-700">Consejos de Plantas</h2>
      <article className="mt-4 border-b pb-4">
        <h3 className="font-semibold">💧 Riego adecuado</h3>
        <p>Evita encharcar las raíces y riega en la mañana o al atardecer.</p>
      </article>
      <article className="mt-4 border-b pb-4">
        <h3 className="font-semibold">☀️ Luz solar</h3>
        <p>Coloca las plantas de interior cerca de ventanas con luz indirecta.</p>
      </article>
    </section>
  );
}

export default ConsejosPlantas;
