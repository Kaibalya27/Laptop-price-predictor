document.getElementById('predict-form').addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(event.target);
    const data = {};
    formData.forEach((value, key) => {
        data[key] = value;
    });

    const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify([data]),  // Send data as an array
    });

    
    const result = await response.json();
    document.getElementById('prediction-result').innerText = "The predicted price of this configuration is ${result.predicted_price}";
});