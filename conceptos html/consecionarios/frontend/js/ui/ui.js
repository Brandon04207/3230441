export class UI {
  constructor() {
    this.initializeElements();
  }

  initializeElements() {
    this.elements = {
      productsTableBody: document.getElementById('productsTableBody'),
      productForm: document.getElementById('productForm'),
      searchInput: document.getElementById('searchInput'),
      btnSearch: document.getElementById('btnSearch'),
      loadingIndicator: document.getElementById('loadingIndicator'),
      successAlert: document.getElementById('successAlert'),
      errorAlert: document.getElementById('errorAlert')
    };
  }

  // =========================
  // 🎯 EVENTOS
  // =========================

  setAddProductListener(callback) {
    const form = this.elements.productForm;

    if (!form) return;

    form.addEventListener('submit', (e) => {
      e.preventDefault();

      const producto = {
        nombre: document.getElementById('nombre').value,
        precio: document.getElementById('precio').value,
        stock: document.getElementById('stock').value
      };

      callback(producto);
      form.reset();
    });
  }

  setDeleteListener(callback) {
    this.elements.productsTableBody.addEventListener('click', (e) => {
      if (e.target.classList.contains('btn-delete')) {
        const id = e.target.dataset.id;
        callback(id);
      }
    });
  }

  setEditListener(callback) {
    this.elements.productsTableBody.addEventListener('click', (e) => {
      if (e.target.classList.contains('btn-edit')) {
        const id = e.target.dataset.id;
        callback(id);
      }
    });
  }

  setSearchListener(callback) {
    const btn = this.elements.btnSearch;

    if (!btn) return;

    btn.addEventListener('click', () => {
      const query = this.elements.searchInput.value;
      callback(query);
    });
  }

  // =========================
  // 📊 RENDER
  // =========================

  renderProducts(productos) {
    const tbody = this.elements.productsTableBody;

    tbody.innerHTML = '';

    if (!productos || productos.length === 0) {
      tbody.innerHTML = `
        <tr>
          <td colspan="4">No hay productos</td>
        </tr>
      `;
      return;
    }

    productos.forEach(producto => {
      const row = document.createElement('tr');

      row.innerHTML = `
        <td>${producto.id_producto}</td>
        <td>${producto.nombre}</td>
        <td>${producto.precio}</td>
        <td>${producto.stock}</td>
        <td>
          <button class="btn-edit" data-id="${producto.id_producto}">Editar</button>
          <button class="btn-delete" data-id="${producto.id_producto}">Eliminar</button>
        </td>
      `;

      tbody.appendChild(row);
    });
  }

  // =========================
  // 🔄 ESTADOS
  // =========================

  showLoading() {
    if (this.elements.loadingIndicator) {
      this.elements.loadingIndicator.style.display = 'block';
    }
  }

  hideLoading() {
    if (this.elements.loadingIndicator) {
      this.elements.loadingIndicator.style.display = 'none';
    }
  }

  // =========================
  // 🚨 ALERTAS
  // =========================

  showSuccess(message) {
    if (!this.elements.successAlert) return;

    this.elements.successAlert.textContent = message;
    this.elements.successAlert.style.display = 'block';

    setTimeout(() => {
      this.elements.successAlert.style.display = 'none';
    }, 3000);
  }

  showError(message) {
    if (!this.elements.errorAlert) return;

    this.elements.errorAlert.textContent = message;
    this.elements.errorAlert.style.display = 'block';

    setTimeout(() => {
      this.elements.errorAlert.style.display = 'none';
    }, 3000);
  }
}