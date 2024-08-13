function calculateBenefits() {
    const manualTime = parseFloat(document.getElementById('manualTime').value);
    const frequency = parseInt(document.getElementById('frequency').value);
    const automatedTime = parseFloat(document.getElementById('automatedTime').value);
    const hourlyRate = parseFloat(document.getElementById('hourlyRate').value);

    if (isNaN(manualTime) || isNaN(frequency) || isNaN(automatedTime) || isNaN(hourlyRate)) {
        alert("Please enter valid numbers for all fields.");
        return;
    }

    const totalManualTime = manualTime * frequency;
    const totalAutomatedTime = automatedTime * frequency;
    const timeSaved = totalManualTime - totalAutomatedTime;
    const costSavings = timeSaved * hourlyRate;

    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = `
        <p>Total manual time per month: ${totalManualTime} hours</p>
        <p>Total automated time per month: ${totalAutomatedTime} hours</p>
        <p>Time saved per month: ${timeSaved} hours</p>
        <p>Potential cost savings per month: $${costSavings.toFixed(2)}</p>
    `;
}
