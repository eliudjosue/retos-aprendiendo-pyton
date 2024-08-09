function getFunction() {
  fetch("https://pokeapi.co/api/v2/pokemon/ditto")
    .then((res) => res.json())
    .then((data) => {
      console.log(data.abilities[0].ability.name);
      const result = data;
      const body = document.getElementById("body");
      body.innerHTML = `lo que quiero mostra es: ${data.name}`;
    });
}
