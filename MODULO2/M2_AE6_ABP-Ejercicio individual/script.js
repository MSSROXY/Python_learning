$(document).ready(function () {
  let images = [];
  let currentIndex = 0; // idx de la imagen actual

  let randomPage = Math.floor(Math.random() * 10) + 1;
  let apiUrl = `https://picsum.photos/v2/list?page=${randomPage}&limit=20`;
  $.ajax({
    url: apiUrl,
    method: "GET",
    success: function (data) {
      images = data;
      //   console.log(data); // Datos obtenidos correctamente
      $(data).each(function (index, img) {
        let newDiv = $("<div>").addClass("container_imagen").attr("id", img.id);
        let newImg = $("<img>")
          .attr("src", img.download_url)
          .attr("class", "imagen");
        newDiv.append(newImg);
        $(".container_gallery").append(newDiv);

        newDiv.on("click", function () {
          currentIndex = index;
          showModal();
        });
      });
    },
    error: function (error) {
      console.error("Error:", error); // Maneja errores
    },
  });

  function showModal() {
    $("#modal").fadeIn(300);
    $(".modal-img").attr("src", images[currentIndex].download_url);
    console.log("img", images[currentIndex]);
  }
  $("#modal").on("click", function (e) {
    if ($(e.target).hasClass("overlay")) {
      $("#modal").fadeOut(300);
    }
  });
  $(".close-modal").on("click", function () {
    $("#modal").fadeOut(300);
  });
  $(".next").on("click", function (e) {
    e.stopPropagation();
    currentIndex = (currentIndex + 1) % images.length;
    showModal();
  });
  $(".prev").on("click", function (e) {
    e.stopPropagation();
    currentIndex = (currentIndex - 1) % images.length;
    showModal();
  });
});
