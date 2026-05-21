import { ProductosAPI } from './api/productosAPI.js';
import { UI } from './ui/ui.js';

class App {
  constructor() {
    this.ui = new UI();
    this.products = [];
    this.init();
  }

  async init() {
    this.setupEventListeners();
    await this.loadProducts();
  }

  setupEventListeners() {
    // 🔥 SOLO estos (coherentes con tu UI)
    this.ui.setAddProductListener((productData) => this.saveProduct(productData));
    this.ui.setSearchListener((query) => this.searchProducts(query));
    this.ui.setDeleteListener((id) => this.deleteProduct(id));
  }

  async loadProducts() {
    try {
      this.ui.showLoading();
      this.products = await ProductosAPI.getAll();
      this.ui.renderProducts(this.products);
    } catch (error) {
      this.ui.showError(error.message);
    } finally {
      this.ui.hideLoading();
    }
  }

  async searchProducts(query) {
    try {
      if (!query.trim()) {
        this.ui.renderProducts(this.products);
        return;
      }

      const filteredProducts = await ProductosAPI.search(query);
      this.ui.renderProducts(filteredProducts);
    } catch (error) {
      this.ui.showError(error.message);
    }
  }

  async saveProduct(productData) {
    try {
      if (productData.id) {
        await ProductosAPI.update(productData.id, productData);
        this.ui.showSuccess('Producto actualizado correctamente');
      } else {
        await ProductosAPI.create(productData);
        this.ui.showSuccess('Producto creado correctamente');
      }

      await this.loadProducts();
    } catch (error) {
      this.ui.showError(error.message);
    }
  }

  async deleteProduct(id) {
    try {
      await ProductosAPI.delete(id);
      this.ui.showSuccess('Producto eliminado correctamente');
      await this.loadProducts();
    } catch (error) {
      this.ui.showError(error.message);
    }
  }
}

// Inicializar la aplicación
document.addEventListener('DOMContentLoaded', () => {
  new App();
});