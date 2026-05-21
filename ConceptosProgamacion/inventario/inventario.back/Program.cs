// Program.cs
using Inventario.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

// Configurar Entity Framework con LocalDB
builder.Services.AddDbContext<InventarioDBContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("InventarioConnection")));

// Configurar CORS para WASM
builder.Services.AddCors(options =>
{
    options.AddPolicy("WasmPolicy", policy =>
    {
        policy.WithOrigins("https://localhost:7123", "http://localhost:5123")
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseRouting();
app.UseCors("WasmPolicy");
app.UseAuthorization();
app.MapControllers();

// Crear y migrar la base de datos al iniciar
using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;
    try
    {
        var context = services.GetRequiredService<InventarioDBContext>();
        context.Database.Migrate();
        Console.WriteLine("Base de datos migrada exitosamente.");
    }
    catch (Exception ex)
    {
        Console.WriteLine($"Error al migrar la base de datos: {ex.Message}");
    }
}

app.Run();