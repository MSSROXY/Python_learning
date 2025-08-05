const base = "./assets/img/";
const movies = [
    {title: "Duna parte 2", img: base+"dune.jpg"},
    {title: "Oppenheimer", img: base+"oppenheimer.jpg"},
    {title: "Barbie", img: base+"barbie.jpg"}
]


$(document).ready(function () {
    //renderizaremos las tarjetas de las peliculas
    movies.forEach(movie => {
        $("#movies-container").append(`
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <img src="${movie.img}" class="card-img-top" alt="${movie.title}">
                    <div class="card-body">
                        <h5 class="card-title">${movie.title}</h5>
                        <button class="btn btn-info reservar-btn" data-title="${movie.title}">Reservar</button>
                    </div>
                </div>
            </div>
            
            `);
    });

    // abrir modal con titulo pelicula
    $(document).on("click", ".reservar-btn", function (){
        // obtenemos el nombre de la pelicula a traves mdel atributo data-title del button
        const movie = $(this).data("title");
        // alert(movie);
        $("#movieName").val(movie);
        $("#reservationModal").modal("show");
    });
    $("#reservationForm").on("submit", (e) => {
        e.preventDefault();
        const movie = $("#movieName").val();
        const time = $("#movieTime").val();
        alert(`Reserva confirmada para ${movie} las ${time}`);

        $("#reservationModal").modal("hide");
        // esperamos q se cierre el modal antes de resetear
        setTimeout(() => {
            $("#reservationForm")[0].reset();
        }, 500);
    });
});