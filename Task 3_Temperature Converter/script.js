// script.js
document.getElementById('convert-btn').addEventListener('click', function() {
    const tempInput = document.getElementById('temperature').value;
    const unit = document.getElementById('unit').value;
    const resultDiv = document.getElementById('result');
    
    if (!tempInput || !unit) {
        resultDiv.textContent = 'Please enter a temperature and select a unit.';
        return;
    }

    const temperature = parseFloat(tempInput);
    let convertedTemp;
    let resultUnit;

    if (unit === 'C') {
        convertedTemp = (temperature * 9/5) + 32;
        resultUnit = 'Fahrenheit';
    } else if (unit === 'F') {
        convertedTemp = (temperature - 32) * 5/9;
        resultUnit = 'Celsius';
    }

    resultDiv.textContent = `Converted temperature: ${convertedTemp.toFixed(2)} ${resultUnit}`;
});
