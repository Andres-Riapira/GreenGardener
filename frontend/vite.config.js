import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173, // puedes cambiar el puerto si lo deseas
    open: true  // abre automáticamente el navegador
  },
  resolve: {
    alias: {
      '@': '/src' // permite importar con "@/components/Navbar"
    }
  }
})
