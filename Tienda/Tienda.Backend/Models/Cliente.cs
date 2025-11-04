namespace Tienda.Backend.Models
{
    public class Cliente
    {

        public int Id { get; set; }
        public string Nombre { get; set; }   
        public string Email { get; set; }
        public int Telefono { get; set; }
        public int Direccion { get; set; }
        //gt:leer y set:escribir
    }
}
