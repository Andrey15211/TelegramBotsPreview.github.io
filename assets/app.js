async function loadComponents() {
  const mounts = [...document.querySelectorAll("[data-component]")];

  await Promise.all(
    mounts.map(async (mount) => {
      const source = mount.dataset.component;
      const response = await fetch(source);

      if (!response.ok) {
        throw new Error(`Cannot load component: ${source}`);
      }

      mount.outerHTML = await response.text();
    })
  );
}

function enhanceContactForm() {
  const form = document.querySelector("#contact form");

  if (!form) {
    return;
  }

  form.addEventListener("submit", (event) => {
    event.preventDefault();
    const button = form.querySelector("button");
    button.textContent = "Заявка подготовлена";
    button.classList.add("bg-emerald-500");
  });
}

loadComponents()
  .then(enhanceContactForm)
  .catch((error) => {
    console.error(error);
  });
