import { supabase } from '../config/supabase.js';

export class ProductosController {
  
  // GET /api/productos
  static async getProductos(req, res) {
    try {
      const { data, error } = await supabase
        .from('productos')
        .select('*')
        .order('id_producto', { ascending: true });
      
      if (error) throw error;
      res.json({ success: true, data });
    } catch (error) {
      res.status(500).json({ 
        success: false, 
        error: error.message 
      });
    }
  }

  // GET /api/productos/:id
  static async getProductoById(req, res) {
    try {
      const { id } = req.params;
      const { data, error } = await supabase
        .from('productos')
        .select('*')
        .eq('id_producto', id)
        .single();
      
      if (error) throw error;
      res.json({ success: true, data });
    } catch (error) {
      res.status(404).json({ 
        success: false, 
        error: 'Producto no encontrado' 
      });
    }
  }

  // POST /api/productos
  static async createProducto(req, res) {
    try {
      const { nombre, marca, modelo, tipo, precio_venta, costo } = req.body;
      
      const { data, error } = await supabase
        .from('productos')
        .insert([{ nombre, marca, modelo, tipo, precio_venta, costo }])
        .select();
      
      if (error) throw error;
      res.status(201).json({ success: true, data });
    } catch (error) {
      res.status(400).json({ 
        success: false, 
        error: error.message 
      });
    }
  }

  // PUT /api/productos/:id
  static async updateProducto(req, res) {
    try {
      const { id } = req.params;
      const { nombre, marca, modelo, tipo, precio_venta, costo } = req.body;
      
      const { data, error } = await supabase
        .from('productos')
        .update({ nombre, marca, modelo, tipo, precio_venta, costo })
        .eq('id_producto', id)
        .select();
      
      if (error) throw error;
      res.json({ success: true, data });
    } catch (error) {
      res.status(400).json({ 
        success: false, 
        error: error.message 
      });
    }
  }

  // DELETE /api/productos/:id
  static async deleteProducto(req, res) {
    try {
      const { id } = req.params;
      
      const { error } = await supabase
        .from('productos')
        .delete()
        .eq('id_producto', id);
      
      if (error) throw error;
      res.json({ success: true, message: 'Producto eliminado' });
    } catch (error) {
      res.status(400).json({ 
        success: false, 
        error: error.message 
      });
    }
  }

  // GET /api/productos/search/:query
  static async searchProductos(req, res) {
    try {
      const { query } = req.params;
      
      const { data, error } = await supabase
        .from('productos')
        .select('*')
        .or(`nombre.ilike.%${query}%,marca.ilike.%${query}%,modelo.ilike.%${query}%,tipo.ilike.%${query}%`);
      
      if (error) throw error;
      res.json({ success: true, data });
    } catch (error) {
      res.status(500).json({ 
        success: false, 
        error: error.message 
      });
    }
  }
}