// public/js/script.js

document.getElementById("uploadForm").addEventListener("submit", async function(event) {
    event.preventDefault();  
    const formData = new FormData(this);

    try {
        // Envia a imagem para o backend usando fetch
        const response = await fetch("/upload-imagem", {
            method: "POST",
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Resposta do backend:', data); 
            document.getElementById("result").innerHTML = `
                <h2>Resultado:</h2>
                <p>Local: ${data.path}</p>
                
                <img src="/uploads/${data.filename}" alt="Imagem enviada" />
            `;
        } else {
            const error = await response.json();
            console.error('Erro na resposta:', error);  // Loga o erro no console para inspeção
            document.getElementById("result").innerHTML = `
                <h2>Erro:</h2>
                <p>${JSON.stringify(error)}</p>  <!-- Mostra o objeto de erro como string -->
            `;
        }
    } catch (e) {
        console.error('Erro ao enviar a requisição:', e);  // Loga qualquer outro erro que possa ocorrer
        document.getElementById("result").innerHTML = `
            <h2>Erro:</h2>
            <p>${e.message}</p>
        `;
    }
});

function toggleDropdown() {
    var dropdown = document.getElementById("dropdown");
    if (dropdown.style.display === "none") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}
