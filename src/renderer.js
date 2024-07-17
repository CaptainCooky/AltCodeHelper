"use strict";

function openTab(evt, tabName) {
  let i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablinks");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }
  document.getElementById(tabName).style.display = "block";
  evt.currentTarget.className += " active";
}

function filterList() {
  const searchInput = document.getElementById("search").value.toUpperCase();
  const ul = document.getElementById("altList");
  const li = ul.getElementsByTagName("li");
  for (let i = 0; i < li.length; i++) {
    const textValue = li[i].textContent || li[i].innerText;
    li[i].style.display = textValue.toUpperCase().indexOf(searchInput) > -1 ? "" : "none";
  }
}

// Open default tab
document.addEventListener("DOMContentLoaded", () => {
  document.querySelector(".tablinks").click();
});
