// layout -> root (conectar las paginas)

//export default -> exportar por defecto, solo puede haber un default por archivo
export default function RootLayout({ children }) {
    return (
        <html lang="es">
            <body>{children}</body>
        </html>

    );
}