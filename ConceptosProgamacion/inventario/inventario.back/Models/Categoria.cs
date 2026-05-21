// Models/Categoria.cs
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace Inventario.Models
{
    public class Categoria
    {
        [Key]
        public int CategoriaId { get; set; }

        [Required(ErrorMessage = "El nombre de la categoría es requerido")]
        [StringLength(50, ErrorMessage = "El nombre no puede exceder 50 caracteres")]
        public string Nombre { get; set; }

        [StringLength(200, ErrorMessage = "La descripción no puede exceder 200 caracteres")]
        public string Descripcion { get; set; }

        public bool Activa { get; set; } = true;

        [DatabaseGenerated(DatabaseGeneratedOption.Computed)]
        public DateTime FechaCreacion { get; set; } = DateTime.UtcNow; // Cambiado de object a DateTime

        // Relación con Productos
        public virtual ICollection<Producto> Productos { get; set; } = new List<Producto>();
    }
}