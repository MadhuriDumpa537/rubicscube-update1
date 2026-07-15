document.addEventListener("DOMContentLoaded", () => {
    const faceInputs = document.querySelectorAll(".face-input");

    for (const input of faceInputs) {
        input.addEventListener("change", (event) => {
            const target = event.currentTarget;
            const face = target.dataset.face;
            const file = target.files && target.files[0];

            if (!face) {
                return;
            }

            const preview = document.getElementById(`preview-${face}`);
            const card = target.closest(".upload-card");
            const placeholder = card ? card.querySelector(".preview-placeholder") : null;
            const status = card ? card.querySelector(".status-pill") : null;

            if (!file || !preview || !(preview instanceof HTMLImageElement)) {
                if (preview instanceof HTMLImageElement) {
                    preview.hidden = true;
                    preview.removeAttribute("src");
                }
                if (placeholder) {
                    placeholder.hidden = false;
                }
                if (status) {
                    status.textContent = "Pending";
                    status.classList.remove("is-ready");
                }
                return;
            }

            const reader = new FileReader();
            reader.onload = () => {
                preview.src = String(reader.result);
                preview.hidden = false;
                if (placeholder) {
                    placeholder.hidden = true;
                }
                if (status) {
                    status.textContent = "Ready";
                    status.classList.add("is-ready");
                }
            };
            reader.readAsDataURL(file);
        });
    }
});
