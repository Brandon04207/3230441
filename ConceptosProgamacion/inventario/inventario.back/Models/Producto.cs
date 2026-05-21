// Models/Producto.cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Inventario.Models
{
    public class Producto
    {
        [Key]
        public int ProductoId { get; set; }

        [Required(ErrorMessage = "El nombre del producto es requerido")]
        [StringLength(100, ErrorMessage = "El nombre no puede exceder 100 caracteres")]
        public string Nombre { get; set; }

        [StringLength(500, ErrorMessage = "La descripción no puede exceder 500 caracteres")]
        public string Descripcion { get; set; }

        [Required(ErrorMessage = "El precio es requerido")]
        [Range(0.01, double.MaxValue, ErrorMessage = "El precio debe ser mayor a 0")]
        [Column(TypeName = "decimal(18,2)")]
        public decimal Precio { get; set; }

        [Required(ErrorMessage = "El stock es requerido")]
        [Range(0, int.MaxValue, ErrorMessage = "El stock no puede ser negativo")]
        public int Stock { get; set; }

        [Range(0, int.MaxValue, ErrorMessage = "El stock mínimo no puede ser negativo")]
        public int StockMinimo { get; set; } = 10;

        [StringLength(50, ErrorMessage = "El código no puede exceder 50 caracteres")]
        public string Codigo { get; set; }

        public bool Activo { get; set; } = true;

        [DatabaseGenerated(DatabaseGeneratedOption.Computed)]
        public DateTime FechaCreacion { get; set; } = DateTime.UtcNow; // Cambiado de object a DateTime

        // Claves foráneas
        public int? CategoriaId { get; set; }
        public int? ProveedorId { get; set; }

        // Propiedades de navegación
        [ForeignKey("CategoriaId")]
        public virtual Categoria Categoria { get; set; }

        [ForeignKey("ProveedorId")]
        public virtual Proveedor Proveedor { get; set; }
    }
}