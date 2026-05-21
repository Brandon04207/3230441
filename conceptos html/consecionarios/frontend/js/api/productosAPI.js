const API_BASE_URL = 'http://localhost:3000/api';

export class ProductosAPI {
  
  static async getAll() {
    try {
      const response = await fetch(`${API_BASE_URL}/productos`);
      const result = await response.json();
      
      if (!result.success) throw new Error(result.error);
      return result.data;
    } catch (error) {
      throw new Error(`Error al cargar productos: ${error.message}`);
    }
  }

  static async getById(id) {
    try {
      const response = await fetch(`${API_BASE_URL}/productos/${id}`);
      const result = await response.json();
      
      if (!result.success) throw new Error(result.error);
      return result.data;
    } catch (error) {
      throw new Error(`Error al obtener producto: ${error.message}`);
    }
  }

  static async create(producto) {
    try {
      const response = await fetch(`${API_BASE_URL}/productos`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(producto)
      });
      
      const result = await response.json();
      if (!result.success) throw new Error(result.error);
      return result.data;
    } catch (error) {
      throw new Error(`Error al crear producto: ${error.message}`);
    }
  }

  static async update(id, producto) {
    try {
      const response = await fetch(`${API_BASE_URL}/productos/${id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(producto)
      });
      
      const result = await response.json();
      if (!result.success) throw new Error(result.error);
      return result.data;
    } catch (error) {
      throw new Error(`Error al actualizar producto: ${error.message}`);
    }
  }

  static async delete(id) {
    try {
      const response = await fetch(`${API_BASE_URL}/productos/${id}`, {
        method: 'DELETE'
      });
      
      const result = await response.json();
      if (!result.success) throw new Error(result.error);
      return result.message;
    } catch (error) {
      throw new Error(`Error al eliminar producto: ${error.message}`);
    }
  }

  static async search(query) {
    try {
      const response = await fetch(`${API_BASE_URL}/productos/search/${encodeURIComponent(query)}`);
      const result = await response.json();
      
      if (!result.success) throw new Error(result.error);
      return result.data;
    } catch (error) {
      throw new Error(`Error en búsqueda: ${error.message}`);
    }
  }
}