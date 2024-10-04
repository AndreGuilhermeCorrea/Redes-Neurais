document.getElementById("uploadForm").addEventListener("submit", async function(event) {
    event.preventDefault();  // Impede o envio padrão do formulário

    const formData = new FormData(this);

    // Envia a imagem para o backend usando fetch
    const response = await fetch("/upload", {
        method: "POST",
        body: formData
    });

    const result = await response.json();

    // Exibe o resultado da previsão na página
    document.getElementById("result").innerHTML = `
        <h2>Resultado:</h2>
        <p>Animal detectado: ${result.class}</p>
    `;
});

function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "none") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}
