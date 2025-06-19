function togglePassword(fieldId) {
    const input = document.getElementById(fieldId);
    if (input) {
      input.type = input.type === "password" ? "text" : "password";
    }
  }
  