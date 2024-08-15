// Function to show the form when the "Find Alumni" button is clicked
function showForm() {
    document.getElementById("alumniForm").style.display = "block";
}

// Handle form submission
document.getElementById("searchForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    const studentName = document.getElementById("studentName").value;
    const studentEmail = document.getElementById("studentEmail").value;
    const searchField = document.getElementById("searchField").value;

    // For demonstration, we'll just display the search query.
    // In a real project, you would connect to a backend to search alumni data.
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = `<p>Searching for alumni with query: "${searchField}"</p>`;
});
