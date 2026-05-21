import express from 'express';
import { ProductosController } from '../controllers/productosController.js';

const router = express.Router();

router.get('/productos', ProductosController.getProductos);
router.get('/productos/search/:query', ProductosController.searchProductos);
router.get('/productos/:id', ProductosController.getProductoById);
router.post('/productos', ProductosController.createProducto);
router.put('/productos/:id', ProductosController.updateProducto);
router.delete('/productos/:id', ProductosController.deleteProducto);

export default router;