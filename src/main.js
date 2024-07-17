"use strict";

import { app, BrowserWindow, globalShortcut } from "electron";
import path, { join } from "path";
import { fileURLToPath } from "url";
import { dirname } from "path";

// Define __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function createWindow() {
  const win = new BrowserWindow({
    width: 400,
    height: 600,
    webPreferences: {
      preload: join(__dirname, "preload.js"),
    },
  });

  win.loadFile(join(__dirname, "index.html"));

  //   // Hide the window when it loses focus
  //   win.on("blur", () => {
  //     setTimeout(() => {
  //       win.hide();
  //     }, 60000);
  //   });
}

app.whenReady().then(() => {
  createWindow();

  // Register a global shortcut to show the window
  globalShortcut.register("Alt+0", () => {
    const win = BrowserWindow.getAllWindows()[0];
    win.show();
    win.focus();
  });

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow();
    }
  });
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit();
  }
});
