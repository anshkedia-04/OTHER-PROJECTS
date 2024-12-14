const items = [
  { name: "Smartphone", price: 699, category: "electronics" },
  { name: "Laptop", price: 1299, category: "electronics" },
  { name: "Smartwatch", price: 199, category: "electronics" },
  { name: "Headphones", price: 149, category: "electronics" },
  { name: "Bluetooth Speaker", price: 99, category: "electronics" },
  { name: "T-Shirt", price: 25, category: "fashion" },
  { name: "Jeans", price: 50, category: "fashion" },
  { name: "Jacket", price: 100, category: "fashion" },
  { name: "Sneakers", price: 80, category: "fashion" },
  { name: "Handbag", price: 60, category: "fashion" },
  { name: "Sofa", price: 500, category: "home items" },
  { name: "Dining Table", price: 750, category: "home items" },
  { name: "Desk Lamp", price: 40, category: "home items" },
  { name: "Curtains", price: 70, category: "home items" },
  { name: "Rug", price: 120, category: "home items" },
  { name: "Tablet", price: 350, category: "electronics" },
  { name: "Blender", price: 150, category: "home items" },
  { name: "Sunglasses", price: 120, category: "fashion" },
  { name: "Gaming Console", price: 499, category: "electronics" },
  { name: "Bookshelf", price: 200, category: "home items" }
];

let category = document.getElementById("category");
let main_id = document.getElementById("main_div");

// Function to render cards
function showCards(products) {
  main_id.innerHTML = ""; // Clear previous cards
  products.forEach((item) => {
    let card = document.createElement("div");
    card.classList.add("card");
    card.innerHTML = `
      <img
          src="https://imgs.search.brave.com/WiQeGjFDRIKNhXkJfcHZQGfcmRPMxmjtg5DsSznWpno/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly91cGxv/YWQud2lraW1lZGlh/Lm9yZy93aWtpcGVk/aWEvY29tbW9ucy81/LzUwL1Nob3BwaW5n/Q2FydC5zdmc"
          alt="Avatar"
          style="width: 100%"
      />
      <div class="container">
        <h4>
          <b>${item.name}</b><br>
          <b>$${item.price}</b>
        </h4>
        <p>${item.category}</p>
      </div>`;
    main_id.appendChild(card);
  });
}

// Initial render of all cards
showCards(items);

// Event listener for category change
category.addEventListener("change", () => {
  const selectedCategory = category.value; // Get selected category
  if (selectedCategory === "all") {
    showCards(items); // Show all items if "all" is selected
  } else {
    const filteredArray = items.filter((item) => item.category === selectedCategory);
    showCards(filteredArray); // Show filtered items
  }
});