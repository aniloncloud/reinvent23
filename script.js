// Function to load and display data from output.json
function loadData() {
    fetch('output.json')
        .then(response => response.json())
        .then(data => {
            let tbody = document.getElementById('dataTable').getElementsByTagName('tbody')[0];
            tbody.innerHTML = ''; // Clear existing table data

            data.forEach(item => {
                let row = tbody.insertRow();
                let titleCell = row.insertCell(0);
                let viewsCell = row.insertCell(1);
                titleCell.textContent = item.title;
                viewsCell.textContent = item.views;
            });
        })
        .catch(error => console.error('Error:', error));
}

// Call loadData on page load
window.onload = loadData;

// Function to sort table
function sortTable(columnIndex) {
    // Sorting logic here
    // Similar to the previous example but adapted for Bootstrap's table structure
}
