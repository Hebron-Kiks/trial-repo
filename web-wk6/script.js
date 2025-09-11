document.addEventListener("DOMContentLoaded", function () {
    // ==========================
    // HELPER FUNCTIONS
    // ==========================
    function setError(input, message) {
        input.style.borderColor = "red";
        let msg = document.getElementById("formMessage");
        msg.style.color = "red";
        msg.textContent = message;
    }

    function setSuccess(input) {
        input.style.borderColor = "green";
    }

    // ==========================
    // FORM VALIDATION
    // ==========================
    const form = document.getElementById("signupForm");
    const usernameInput = document.getElementById("username");
    const emailInput = document.getElementById("email");
    const passwordInput = document.getElementById("password");
    const message = document.getElementById("formMessage");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        let valid = true;

        // Username
        if (usernameInput.value.trim().length < 3) {
            setError(usernameInput, "Username must be at least 3 characters.");
            valid = false;
        } else {
            setSuccess(usernameInput);
        }

        // Email
        if (!emailInput.value.includes("@") || !emailInput.value.includes(".")) {
            setError(emailInput, "Please enter a valid email address.");
            valid = false;
        } else {
            setSuccess(emailInput);
        }

        // Password
        if (passwordInput.value.trim().length < 6) {
            setError(passwordInput, "Password must be at least 6 characters.");
            valid = false;
        } else {
            setSuccess(passwordInput);
        }

        // If all good
        if (valid) {
            message.style.color = "green";
            message.textContent = "Form submitted successfully!";
            form.reset();

            // Reset borders after success
            usernameInput.style.borderColor = "#ddd";
            emailInput.style.borderColor = "#ddd";
            passwordInput.style.borderColor = "#ddd";
        }
    });

    // ==========================
    // LIVE INPUT VALIDATION
    // ==========================
    usernameInput.addEventListener("input", () => {
        if (usernameInput.value.trim().length >= 3) setSuccess(usernameInput);
    });
    emailInput.addEventListener("input", () => {
        if (emailInput.value.includes("@") && emailInput.value.includes(".")) setSuccess(emailInput);
    });
    passwordInput.addEventListener("input", () => {
        if (passwordInput.value.trim().length >= 6) setSuccess(passwordInput);
    });

    // ==========================
    // BACKGROUND COLOR CHANGER
    // ==========================
    document.getElementById("changeColorBtn").addEventListener("click", function () {
        const randomColor = "#" + Math.floor(Math.random() * 16777215).toString(16);
        document.body.style.backgroundColor = randomColor;
    });

    // ==========================
    // CLICK COUNTER
    // ==========================
    let count = 0;
    document.getElementById("countBtn").addEventListener("click", function () {
        count++;
        document.getElementById("counter").textContent = count;
    });
});
