// Program.cs
using Inventario.Data;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();

// Configurar Entity Framework
builder.Services.AddDbContext<InventarioDBContext>(options =>
    options.UseSqlServer(builder.Configuration.GetConnectionString("InventarioConnection")));

// Configurar CORS para WASM
builder.Services.AddCors(options =>
{
    options.AddPolicy("WasmPolicy", policy =>
    {
        policy.WithOrigins("https://localhost:7123", "http://localhost:5123") // URLs de tu frontend WASM
              .AllowAnyHeader()
              .AllowAnyMethod();
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
}

app.UseRouting();
app.UseCors("WasmPolicy");
app.UseAuthorization();
app.MapControllers();

// Crear y migrar la base de datos al iniciar
using (var scope = app.Services.CreateScope())
{
    var context = scope.ServiceProvider.GetRequiredService<InventarioDBContext>();
    context.Database.Migrate();
}

app.Run();