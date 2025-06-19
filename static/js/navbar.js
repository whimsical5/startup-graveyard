

//   document.addEventListener("DOMContentLoaded", function () {
//     const dropdown = document.getElementById("profile-dropdown");
//     const icon = document.getElementById("profile-icon");
  
//     if (icon && dropdown) {
//       icon.addEventListener("click", function (event) {
//         event.stopPropagation(); // Prevent closing immediately
//         dropdown.classList.toggle("hidden");
//       });
  
//       document.addEventListener("click", function (e) {
//         if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
//           dropdown.classList.add("hidden");
//         }
//       });
//     }
//   });
  
document.addEventListener("DOMContentLoaded", function () {
  // 👤 Profile Dropdown
  const icon = document.getElementById("profile-icon");
  const dropdown = document.getElementById("profile-dropdown");

  if (icon && dropdown) {
    icon.addEventListener("click", () => dropdown.classList.toggle("hidden"));
    document.addEventListener("click", (e) => {
      if (!icon.contains(e.target) && !dropdown.contains(e.target)) {
        dropdown.classList.add("hidden");
      }
    });
  }

  // 🔍 Search Dropdown
  const input = document.getElementById("navbarSearch");
  const results = document.getElementById("searchResults");

  if (input && results) {
    const items = results.querySelectorAll("li");

    input.addEventListener("input", () => {
      const query = input.value.trim().toLowerCase();
      let anyShown = false;

      items.forEach(item => {
        if (item.dataset.name.includes(query)) {
          item.classList.remove("hidden");
          anyShown = true;
        } else {
          item.classList.add("hidden");
        }
      });

      results.classList.toggle("hidden", !anyShown || query === "");
    });

    items.forEach(item => {
      item.addEventListener("click", () => {
        window.location.href = item.dataset.url;
      });
    });

    // Hide dropdown if clicking outside
    document.addEventListener("click", (e) => {
      if (!input.contains(e.target) && !results.contains(e.target)) {
        results.classList.add("hidden");
      }
    });

    // Show dropdown on input focus if text exists
    input.addEventListener("click", () => {
      if (input.value.trim() !== "") {
        results.classList.remove("hidden");
      }
    });
  }
});

