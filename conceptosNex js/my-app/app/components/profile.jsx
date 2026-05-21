export function profile({user}) {

    return(
        <>
        <h1>{user.name}</h1>
        <img src={user.imageUrl}
         alt ={"foto de " + user.name}
         style={{
            width:user.imageSize,
            height: "auto"
         }}/>
        </>
    );
}