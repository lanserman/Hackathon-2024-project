import { pestData, randBugFacts } from "./constants.js";
let calculateButton = document.querySelector("#calculate-button");

document.addEventListener("DOMContentLoaded", function () {
  const stateSelect = document.querySelector("#state");
  const citySelect = document.querySelector("#city");

  // Define cities for each state
  const stateCities = {
    KS: ["Manhattan", "Topeka", "Wichita"],
    IA: ["Des Moines", "Cedar Rapids", "Iowa City"],
    MO: ["Columbia", "Kansas City", "St. Louis"],
    AK: ["Juneau", "Anchorage", "Denali"],
  };

  // Function to update cities based on selected state
  function updateCities() {
    const selectedState = stateSelect.value;
    const cities = stateCities[selectedState] || [];

    // Clear current city options
    citySelect.innerHTML = "";

    // Populate city dropdown with new options
    cities.forEach((city) => {
      const option = document.createElement("option");
      option.value = city;
      option.textContent = city;
      citySelect.appendChild(option);
    });
  }

  // Initial call to populate cities based on the default state
  updateCities();

  // Event listener to update cities when state changes
  stateSelect.addEventListener("change", updateCities);
});

document
  .querySelector(".next-button-class")
  .addEventListener("click", function () {
    console.log("Got here!");
    var elems = document.getElementsByClassName("crop-info");
    for (var i = 0; i < elems.length; i += 1) {
      elems[i].classList.remove("hidden");
    }
    document.querySelector("#next-button").style.display = "none";
    document.getElementById("state").classList.add("disabled");
    document.getElementById("city").classList.add("disabled");

    // Random bug name stuff
    document.getElementsByClassName("random-bug-section")[0].style.display =
      "block";
    document.getElementsByClassName("about-section")[0].style.display = "block";
    let rand = Math.floor(Math.random() * pestData.length);
    document.getElementById("random-bug-name").textContent =
      pestData[rand].pest;

    //randome bug fact
    const randomIndex = Math.floor(Math.random() * randBugFacts.length);
    let randBugFact = randBugFacts[randomIndex];
    document.getElementById("random-bug-fact").textContent = randBugFact;
  });

calculateButton.addEventListener("click", function () {
  let hiddenLabel = document.getElementsByClassName("hidden-label");
  for (var i = 0; i < hiddenLabel.length; i += 1) {
    hiddenLabel[i].style.display = "block";
  }
  document.querySelector("#pests-present").style.display = "block";
});
