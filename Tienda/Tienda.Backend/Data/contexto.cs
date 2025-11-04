using Microsoft.EntityFrameworkCore;
using Tienda.Backend.Models;

namespace Tienda.Backend.Data
{
    public class Contexto :DbContext
    {
        public Contexto(DbContextOptions<Contexto>options):base(options)
        {
            
        }
        public DbSet<Cliente> Clientes { get; set; }
    }
}
