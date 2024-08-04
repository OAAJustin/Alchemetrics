document.getElementById('add').addEventListener('click',
    function(){document.getElementById('formOverlay').style.display = 'flex';
    });

document.getElementById("form_submit").addEventListener("click", submitForm, false);

async function submitForm(event) {
    event.preventDefault();

    const formData = {
        title: document.getElementById('Title').value,
        medium: document.getElementById('Medium').value,
        size: document.getElementById('Size').value,
        qty: document.getElementById('Qty').value,
        price: document.getElementById('Price').value,
        artist: document.getElementById('Artist').value
    };

    const response = await fetch('/add-item', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    });

    if (response.ok) {
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${formData.title}</td>
            <td>${formData.medium}</td>
            <td>${formData.size}</td>
            <td>${formData.qty}</td>
            <td>${formData.price}</td>
            <td>${formData.artist}</td>
        `;
        document.querySelector('.data_table').appendChild(newRow);
        document.getElementById('formOverlay').reset();
        document.getElementById('formOverlay').style.display = 'none';
    } else {
        console.error('Failed to add item');
    }
}