//Phone number
function sendMail(value) {
  var link = 'mailto: h82w84u@gmail.com'
  + '$subject=' + encodeURIComponent(document.getElementById('ph-number').value);
  window.location.href = link;
}

const renderPh = () => {
  const markup =
    `
    <div class="input-group col-sm-3">
      <input type="text" class="form-control" id='ph-number' placeholder="Ten Digit Phone#" aria-label="Phone number" aria-describedby="basic-addon2">
      <div class="input-group-append">
        <button onclick='sendMail(); return flase' class="btn btn-info" type="button">Call Me</button>
      </div>
    </div>
  `
  document.getElementById('index-container').insertAdjacentHTML('beforeend', markup);
};

//create ph entry box
document.getElementById('free-consultation').addEventListener('click', () => {
  document.getElementById('free-consultation').remove();
    renderPh();
});

//validate number and e-mail
(function () {
  const valuePh = document.getElementById('ph-number');
  if(valuePh) {
    valuePh.addEventListener('click', () => {
      if(valuePh.value.length === 10 && !isNaN(valuePh.value)){
        sendMail(valuePh.value);
      } else {
        alert('Ooops, something went wrong. Please double check your entry and try again!')
      }
    });
  }
})();
