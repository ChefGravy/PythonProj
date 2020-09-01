// //Phone number
// function sendMail(value) {
//   var link = 'mailto: h82w84u@gmail.com'
//   + '$subject=' + encodeURIComponent(document.getElementById('ph-number').value);
//   window.location.href = link;
// }

const renderPh = () => {
  const markup =
    `
      <button id='free-consultation' class="btn btn-info" disabled><b>GET FREE CONSULTATION</b></button>
      <p><span style="font-family: 'Baloo Tamma 2', cursive; font-size: 20px; color:black;"><b>Give me a call @ (206) 601-2325.</b></span>
    `

  document.getElementById('index-container').insertAdjacentHTML('beforeend', markup);
};

//create ph entry box
document.getElementById('free-consultation').addEventListener('click', () => {
  document.getElementById('free-consultation').remove();
    renderPh();
});
//
// //validate number and e-mail
// (function () {
//   const valuePh = document.getElementById('ph-number');
//   if(valuePh) {
//     valuePh.addEventListener('click', () => {
//       if(valuePh.value.length === 10 && !isNaN(valuePh.value)){
//         sendMail(valuePh.value);
//       } else {
//         alert('Ooops, something went wrong. Please double check your entry and try again!')
//       }
//     });
//   }
// })();

// const renderContactForm = () => {
//   const markup =
//   `
//     <h2 style="margin-top: 2rem">Contact Form</h2>
//     <p>
//       <form method="post">
//         {%csrf_token%}
//         <div class="row">
//         <div class="col-6">
//           {{ form.name|as_crispy_field }}
//         </div>
//         <div class="col-6">
//           {{ form.email|as_crispy_field }}
//         </div>
//         <div class="col-6">
//           {{ form.subject|as_crispy_field }}
//         </div>
//         <div class="col-6">
//           {{ form.category|as_crispy_field }}
//         </div>
//         <div class="col-12">
//           {{ form.body|as_crispy_field }}
//         </div>
//       </div>
//       <input type="submit" class="btn btn-primary btn-large" value="Submit">
//     </form>
//   `
//   document.getElementById('contact-form').insertAdjacentHTML('beforeend', markup);
// }
//
// document.getElementById('contact_form_nav').addEventListener('click', () => {
//   document.getElementById('contact_form_nav').remove();
//     renderContactForm();
// });
