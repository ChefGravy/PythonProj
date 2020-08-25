//Data
const btnToggle = () => {
  const dataVarOne = document.getElementById('data-one').style
  const dataBtnOne = document.getElementById('data-btn-one')
  if(dataVarOne.height === '0px') {
    dataVarOne.width = '1000px';
    dataVarOne.height = '1000px';
    dataBtnOne.value = 'Hide'
  } else {
    dataVarOne.height = '0px';
    dataVarOne.width = '0px';
    dataBtnOne.value = 'NWMLS: July Residential + Condo recap by county'
  }
};
document.getElementById('data-btn-one').addEventListener('click', () => {
  btnToggle();
});

//Data2

const btnToggleTwo = () => {
  const dataVarTwo = document.getElementById('data-two').style
  const dataBtnTwo = document.getElementById('data-btn-two')
  if(dataVarTwo.height === '0px') {
    dataVarTwo.width = '1000px';
    dataVarTwo.height = '1000px';
    dataBtnTwo.value = 'Hide'
  } else {
    dataVarTwo.height = '0px';
    dataVarTwo.width = '0px';
    dataBtnTwo.value = 'NWMLS: Jul YTD Summary'
  }
};
document.getElementById('data-btn-two').addEventListener('click', () => {
  btnToggleTwo();
});

//Data3
const btnToggleThree = () => {
  const dataVarThree = document.getElementById('data-three').style
  const dataBtnThree = document.getElementById('data-btn-three')
  if(dataVarThree.height === '0px') {
    dataVarThree.width = '1000px';
    dataVarThree.height = '1000px';
    dataBtnThree.value = 'Hide'
  } else {
    dataVarThree.height = '0px';
    dataVarThree.width = '0px';
    dataBtnThree.value = 'NWMLS: July Price Range and Bedrooms'
  }
};
document.getElementById('data-btn-three').addEventListener('click', () => {
  btnToggleThree();
});

//Data4
const btnToggleFour = () => {
  const dataVarFour = document.getElementById('data-four').style
  const dataBtnFour = document.getElementById('data-btn-four')
  if(dataVarFour.height === '0px') {
    dataVarFour.width = '1000px';
    dataVarFour.height = '1000px';
    dataBtnFour.value = 'Hide'
  } else {
    dataVarFour.height = '0px';
    dataVarFour.width = '0px';
    dataBtnFour.value = 'NWMLS: July Summary Report'
  }
};
document.getElementById('data-btn-four').addEventListener('click', () => {
  btnToggleFour();
});
