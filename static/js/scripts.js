document.addEventListener('DOMContentLoaded', function () {
    // Mock data for chart (should be dynamically fetched)
    const data = {
        labels: ['Flood', 'Earthquake', 'Unknown'],
        datasets: [{
            label: 'Disaster Types',
            data: [10, 5, 2],  // Example data, should be fetched dynamically
            backgroundColor: ['rgba(54, 162, 235, 0.6)', 'rgba(255, 99, 132, 0.6)', 'rgba(75, 192, 192, 0.6)']
        }]
    };

    const config = {
        type: 'bar',
        data: data,
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    };

    const ctx = document.getElementById('disasterChart').getContext('2d');
    new Chart(ctx, config);
});
