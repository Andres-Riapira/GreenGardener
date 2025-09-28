import React, { useEffect, useState } from "react";
import api from "../api/axios";

function Comunidad() {
  const [posts, setPosts] = useState([]);
  const [nuevoPost, setNuevoPost] = useState("");

  useEffect(() => {
    const fetchPosts = async () => {
      try {
        const res = await api.get("/comunidad");
        setPosts(res.data);
      } catch (error) {
        console.error("Error cargando comunidad:", error);
      }
    };
    fetchPosts();
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("/comunidad", { mensaje: nuevoPost });
      setPosts([...posts, res.data]);
      setNuevoPost("");
    } catch (error) {
      console.error("Error al publicar:", error);
    }
  };

  return (
    <section className="p-6">
      <h2 className="text-2xl font-bold text-green-700">Comunidad</h2>

      <form onSubmit={handleSubmit} className="mt-4 flex gap-2">
        <input
          type="text"
          value={nuevoPost}
          onChange={(e) => setNuevoPost(e.target.value)}
          placeholder="Escribe tu mensaje..."
          className="border p-2 rounded flex-grow"
        />
        <button className="bg-green-600 text-white px-4 rounded">Publicar</button>
      </form>

      <div className="mt-6 flex flex-col gap-3">
        {posts.map((post) => (
          <div key={post.id} className="border rounded p-3 bg-green-50">
            💬 {post.mensaje}
          </div>
        ))}
      </div>
    </section>
  );
}

export default Comunidad;
