const books = [
  {
    title: "El Principito",
    author: "Antoine de Saint-Exupéry",
    genre: "Ficción",
    description: "Una historia poética sobre un pequeño príncipe y sus viajes.",
  },
  {
    title: "Clean Code",
    author: "Robert C. Martin",
    genre: "Programación",
    description: "Una guía para hacer código limpio y mantenible.",
  },
  {
    title: "Cien Años de Soledad",
    author: "Gabriel García Márquez",
    genre: "Realismo mágico",
    description: "Una saga familiar ambientada en el mítico pueblo de Macondo",
  },
];

const containerBooks = document.querySelector(".container_libros");

function writeBooks(array) {
  array.map((book) => {
    console.log("book", book);
    const containerBook = document.createElement("div");
    containerBook.classList.add("each_libro");
    containerBook.innerHTML = `
    <h2>${book.title}</h2>
    <p><strong>Autor:</strong> ${book.author}</p>
    <p><strong>Género:</strong> ${book.genre}</p>
    <p>${book.description}</p>
    `;
    containerBooks.appendChild(containerBook);
  });
}
writeBooks(books);

function deleteContent(div) {
  div.innerHTML = "";
}

const inputBook = document.querySelector("#filter_book");
const btnSearch = document.querySelector("#form-filter-book button");
const result = document.getElementById("result-book");

function filterBook(filterWord) {
  return books.filter(
    (book) =>
      book.title.toLocaleLowerCase().includes(filterWord) ||
      book.author.toLocaleLowerCase().includes(filterWord) ||
      book.genre.toLocaleLowerCase().includes(filterWord)
  );
}

inputBook.addEventListener("change", (e) => {
  let filterWord = e.target.value.toLowerCase();
  const filterResult = filterBook(filterWord);
  if (filterWord.length == 0) {
    result.textContent = "";
  }
  console.log("filter", filterResult);
  deleteContent(containerBooks);
  writeBooks(filterResult);
});

btnSearch.addEventListener("click", (e) => {
  if (inputBook.value.length == 0) {
    result.textContent = "";
  } else {
    e.preventDefault();
    const lengthResult = filterBook(inputBook.value);
    result.textContent = `Total de resultados: ${lengthResult.length}`;
  }
});

const formRegister = document.querySelector("#form-register");
const userName = document.querySelector("#input-user-name");
const userEmail = document.querySelector("#input-user-email");
const userPass = document.querySelector("#input-user-pass");
const errorMessages = document.querySelector("#error-user-input");

function isStrongPass(password) {
  return /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/.test(password);
}
function displayError(message) {
  errorMessages.textContent = `${message}`;
}

formRegister.addEventListener("submit", (event) => {
  event.preventDefault();
  console.log("eventoo", userEmail.value, userName.value, userPass.value);
  if (!userPass.value.trim() || !isStrongPass(userPass.value)) {
    displayError(
      "❌ La contraseña debe tener al menos 8 caracteres y contener al menos una letra mayúscula, una letra minúscula, un dígito y un carácter especial."
    );
    return;
  }
  alert("Registro exitoso ✅");
  formRegister.reset();
});
