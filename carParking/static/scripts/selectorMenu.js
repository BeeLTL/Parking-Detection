document.addEventListener("DOMContentLoaded", () => {

    const modelOptionMenu = document.querySelector(".select-menu"),
        modelSelectBtn = modelOptionMenu.querySelector(".model-select-btn"),
        options = modelOptionMenu.querySelectorAll(".option"),
        sBtn_text = modelOptionMenu.querySelector(".sBtn-text"),
        modelInput = document.getElementById("model-input"),
        trackerMenu = document.querySelector(".select-menu-tracker");


    const trackerOptionMenu = document.querySelector(".select-menu-tracker"),
        trackerSelectBtn = trackerOptionMenu.querySelector(".tracker-select-btn"),
        trackerOptions = trackerOptionMenu.querySelectorAll(".option-tracker"),
        trackerSBtnText = trackerOptionMenu.querySelector(".sBtn-text"),
        trackerInput = document.getElementById("tracker-input");

    modelSelectBtn.addEventListener("click", () =>
        modelOptionMenu.classList.toggle("active")
    );

    options.forEach((option) => {
        option.addEventListener("click", () => {
            let selectedOption = option.querySelector(".option-text").innerText;
            sBtn_text.innerText = selectedOption;
            modelInput.value = selectedOption.toLowerCase(); // Set the value of the hidden input field

            // Remove the active class from all options
            options.forEach((opt) => opt.classList.remove("active"));
            // Add the active class to the selected option
            option.classList.add("active");

            // Show the tracker menu when a model is selected
            trackerMenu.style.display = "block";

            modelOptionMenu.classList.remove("active");
        });
    });

    trackerSelectBtn.addEventListener("click", () =>
        trackerOptionMenu.classList.toggle("active")
    );

    trackerOptions.forEach((option) => {
        option.addEventListener("click", () => {
            let selectedOption = option.querySelector(".option-text").innerText;
            trackerSBtnText.innerText = selectedOption;
            trackerInput.value = selectedOption.toLowerCase();

            trackerOptions.forEach((opt) => opt.classList.remove("active"));
            option.classList.add("active");

            trackerOptionMenu.classList.remove("active");
        });
    });
})