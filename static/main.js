// Javascript is used to fetch the predicted price

const sizeOfHouse = document.getElementById("sizeOfHouse");
const appForm = document.getElementById("appForm");
const predictBtn = document.getElementById("predictBtn");

async function fetch_price(size) {
  let res = await fetch(`/predict?sizeOfHouse=${size}`);
  res = await res.json();
  return res;
}

function loading(isLoading = true) {
  if (isLoading) {
    predictBtn.disabled = true;
    predictBtn.classList.add("secondary");
    predictBtn.innerHTML = "Predicting...";
  } else {
    predictBtn.disabled = false;
    predictBtn.classList.remove("secondary");
    predictBtn.innerHTML = "Predict";
  }
}

appForm.addEventListener("submit", async (e) => {
  e.preventDefault();
//   if (sizeOfHouse.value < 120) {
// 	document.getElementById("error").innerHTML = "*Please enter a valid size";
//     return;
//   }

  loading();
  const res = await fetch_price(sizeOfHouse.value);
  loading(false);

  document.getElementById(
    "predictedPrice"
  ).innerHTML = `The price prediction is <mark>$${res.price}</mark>`;
});
