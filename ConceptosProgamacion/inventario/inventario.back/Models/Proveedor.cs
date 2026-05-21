// Models/Proveedor.cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Inventario.Models
{
    public class Proveedor
    {
        [Key]
        public int ProveedorId { get; set; }

        [Required(ErrorMessage = "El nombre es requerido")]
        [StringLength(100, ErrorMessage = "El nombre no puede exceder 100 caracteres")]
        public string Nombre { get; set; }

        [StringLength(200, ErrorMessage = "La dirección no puede exceder 200 caracteres")]
        public string Direccion { get; set; }

        [StringLength(20, ErrorMessage = "El teléfono no puede exceder 20 caracteres")]
        public string Telefono { get; set; }

        [EmailAddress(ErrorMessage = "Formato de email inválido")]
        [StringLength(100, ErrorMessage = "El email no puede exceder 100 caracteres")]
        public string Email { get; set; }

        public bool Activo { get; set; } = true;

        [DatabaseGenerated(DatabaseGeneratedOption.Computed)]
        public DateTime FechaCreacion { get; set; } = DateTime.UtcNow; // Cambiado de object a DateTime

        // Relación con Productos
        public virtual ICollection<Producto> Productos { get; set; } = new List<Producto>();
    }
}