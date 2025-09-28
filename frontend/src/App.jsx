import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import Inicio from "./pages/Inicio";
import PlantasInsumos from "./pages/PlantasInsumos";
import Carrito from "./pages/Carrito";
import { CartProvider } from "./context/CartContext";

function App() {
  return (
    <CartProvider>
      <Router>
        <Navbar />
        <main className="min-h-screen">
          <Routes>
            <Route path="/" element={<Inicio />} />
            <Route path="/plantas" element={<PlantasInsumos />} />
            <Route path="/carrito" element={<Carrito />} />
          </Routes>
        </main>
        <Footer />
      </Router>
    </CartProvider>
  );
}

export default App;
