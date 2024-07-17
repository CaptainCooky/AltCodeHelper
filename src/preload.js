"use strict";

import { clipboard } from "electron";

window.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".alt-code").forEach((item) => {
    item.addEventListener("click", () => {
      clipboard.writeText(item.textContent);
    });
  });
});
