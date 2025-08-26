document.addEventListener('DOMContentLoaded', function() {
    const searchForm = document.getElementById('searchForm');
    const searchBtn = document.getElementById('searchBtn');
    const btnText = document.querySelector('.btn-text');
    const btnLoading = document.querySelector('.btn-loading');
    const resultsSection = document.getElementById('resultsSection');
    const loadingMessage = document.getElementById('loadingMessage');
    const errorMessage = document.getElementById('errorMessage');
    const successResults = document.getElementById('successResults');
    const resultsText = document.getElementById('resultsText');
    const statusIndicator = document.getElementById('statusIndicator');
    
    let statusCheckInterval;

    searchForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        // Show loading state
        setLoadingState(true);
        showResultsSection();
        
        // Get form data
        const formData = new FormData(searchForm);
        const searchData = {};
        
        for (let [key, value] of formData.entries()) {
            searchData[key] = value;
        }
        
        try {
            // Start the search
            const response = await fetch('/api/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(searchData)
            });
            
            const result = await response.json();
            
            if (result.status === 'started') {
                // Start polling for status updates
                startStatusPolling();
            } else {
                throw new Error(result.message || 'Failed to start search');
            }
            
        } catch (error) {
            console.error('Error:', error);
            showError('Failed to start search. Please try again.');
            setLoadingState(false);
        }
    });

    function setLoadingState(isLoading) {
        if (isLoading) {
            searchBtn.disabled = true;
            btnText.style.display = 'none';
            btnLoading.style.display = 'flex';
        } else {
            searchBtn.disabled = false;
            btnText.style.display = 'inline';
            btnLoading.style.display = 'none';
        }
    }

    function showResultsSection() {
        resultsSection.style.display = 'block';
        loadingMessage.style.display = 'block';
        errorMessage.style.display = 'none';
        successResults.style.display = 'none';
        updateStatusIndicator('running', 'Searching...');
    }

    function startStatusPolling() {
        // Clear any existing interval
        if (statusCheckInterval) {
            clearInterval(statusCheckInterval);
        }
        
        // Poll for status updates every 2 seconds
        statusCheckInterval = setInterval(async () => {
            try {
                const response = await fetch('/api/status');
                const status = await response.json();
                
                if (status.status === 'completed') {
                    clearInterval(statusCheckInterval);
                    showSuccess(status.data);
                    setLoadingState(false);
                } else if (status.status === 'error') {
                    clearInterval(statusCheckInterval);
                    showError(status.error || 'An error occurred during the search');
                    setLoadingState(false);
                }
                // If status is 'running', continue polling
                
            } catch (error) {
                console.error('Error checking status:', error);
                clearInterval(statusCheckInterval);
                showError('Failed to check search status');
                setLoadingState(false);
            }
        }, 2000);
    }

    function showSuccess(data) {
        loadingMessage.style.display = 'none';
        errorMessage.style.display = 'none';
        successResults.style.display = 'block';
        
        // Format and display the results
        if (typeof data === 'string') {
            resultsText.textContent = data;
        } else {
            resultsText.textContent = JSON.stringify(data, null, 2);
        }
        
        updateStatusIndicator('completed', 'Completed');
        
        // Scroll to results
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function showError(message) {
        loadingMessage.style.display = 'none';
        successResults.style.display = 'none';
        errorMessage.style.display = 'block';
        errorMessage.querySelector('p').textContent = `❌ ${message}`;
        
        updateStatusIndicator('error', 'Error');
    }

    function updateStatusIndicator(status, text) {
        statusIndicator.textContent = text;
        statusIndicator.className = `status-indicator ${status}`;
    }

    // Add some nice form validation
    const inputs = searchForm.querySelectorAll('input, select');
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            if (this.hasAttribute('required') && !this.value.trim()) {
                this.style.borderColor = '#ef4444';
            } else {
                this.style.borderColor = '#e5e7eb';
            }
        });
        
        input.addEventListener('input', function() {
            if (this.style.borderColor === 'rgb(239, 68, 68)') {
                this.style.borderColor = '#e5e7eb';
            }
        });
    });

    // Price range validation
    const minPrice = document.getElementById('minimum_range');
    const maxPrice = document.getElementById('maximum_range');
    
    function validatePriceRange() {
        const min = parseInt(minPrice.value) || 0;
        const max = parseInt(maxPrice.value) || 0;
        
        if (min > max && max > 0) {
            maxPrice.style.borderColor = '#ef4444';
            return false;
        } else {
            maxPrice.style.borderColor = '#e5e7eb';
            return true;
        }
    }
    
    minPrice.addEventListener('input', validatePriceRange);
    maxPrice.addEventListener('input', validatePriceRange);
    
    // Add form submission validation
    searchForm.addEventListener('submit', function(e) {
        if (!validatePriceRange()) {
            e.preventDefault();
            alert('Maximum price must be greater than or equal to minimum price.');
            return false;
        }
    });
});
