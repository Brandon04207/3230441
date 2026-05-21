// page -> contenido de la pagina

// importamos el componente MyButton para usarlo en esta página
import { MyButton } from "./components/MyButton";

import { profile } from "./components/profile";

const user = {
    name: "alejo",
    imageUrl: "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Slenderman_redacted_bg.jpg/960px-Slenderman_redacted_bg.jpg",
    imagesize : 200
}

//export default -> exportar por defecto, solo puede haber un default por archivo
export default function Home() {
    return (
        <div>
            <h1>Bienvenido a mi pagina</h1>
            <MyButton />

            <profile user={user}></profile>
        </div>
    );
}
