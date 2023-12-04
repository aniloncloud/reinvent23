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
                let thumbnailCell = row.insertCell(2);

                // Create hyperlink for title
                let titleLink = document.createElement('a');
                titleLink.href = item.url;  // Assuming 'url' is the attribute for the URL
                titleLink.textContent = item.title;
                titleLink.target = "_blank"; // Opens link in a new tab
                titleCell.appendChild(titleLink);

                viewsCell.textContent = item.views;

                // Create an image element for the thumbnail
                if (item.thumbnail) {
                    let thumbnailImage = document.createElement('img');
                    thumbnailImage.src = item.thumbnail;
                    thumbnailImage.alt = 'Thumbnail';
                    thumbnailImage.style.width = '100px'; // Set a width for the thumbnail (you can adjust as needed)
                    thumbnailCell.appendChild(thumbnailImage);
                } else {
                    thumbnailCell.textContent = 'No thumbnail';
                }
            });
        })
        .catch(error => console.error('Error:', error));
}

window.onload = loadData;
