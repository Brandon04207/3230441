import express from 'express';
import cors from 'cors';
import productosRoutes from './routes/productosRoutes.js';

const app = express();
const PORT = 3000;

// Middlewares
app.use(cors());
app.use(express.json());

// Routes
app.use('/api', productosRoutes);

// Health check
app.get('/health', (req, res) => {
  res.json({ status: 'OK', message: 'API funcionando' });
});

// Manejo de errores 404
app.use('*', (req, res) => {
  res.status(404).json({ error: 'Endpoint no encontrado' });
});

app.listen(PORT, () => {
  console.log(`🚀 Servidor corriendo en http://localhost:${PORT}`);
});