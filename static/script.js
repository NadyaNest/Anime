document.addEventListener("DOMContentLoaded", function() {
    var genreSelect = document.getElementById("genre-select");
    var randomButton = document.getElementById("random-button");
    var animeInfo = document.getElementById("anime-info");

    // Populate genre select options
    fetch("/genres")
        .then(response => response.json())
        .then(data => {
            data.forEach(genre => {
                var option = document.createElement("option");
                option.value = genre;
                option.textContent = genre;
                genreSelect.appendChild(option);
            });
        })
        .catch(error => console.error('Error:', error));

    // Add event listener to random button
    randomButton.addEventListener("click", function() {
        var genre = genreSelect.value;
        fetch("/random_anime?genre=" + genre)
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    animeInfo.innerHTML = "<p>" + data.error + "</p>";
                } else {
                    animeInfo.innerHTML = `
                        <h2>${data.name}</h2>
                        <p><strong>Genre:</strong> ${data.genre}</p>
                        <p><strong>Type:</strong> ${data.type}</p>
                        <p><strong>Episodes:</strong> ${data.episodes}</p>
                        <p><strong>Rating:</strong> ${data.rating}</p>
                        <p><strong>Members:</strong> ${data.members}</p>
                        <p><strong>Average Rating:</strong> ${data.average_rating}</p>
                        <p><strong>Rating Count:</strong> ${data.rating_count}</p>
                    `;
                }
            })
            .catch(error => console.error('Error:', error));
    });
});
