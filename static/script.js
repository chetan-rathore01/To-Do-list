// Simple confirmation before deleting a task
function confirmDelete(taskId) {
    if (confirm("Are you sure you want to delete this task?")) {
        window.location.href = `/delete/${taskId}`;
    }
}

// Add Enter key shortcut for adding a task
document.querySelector("input[name='task']").addEventListener("keypress", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        document.querySelector("form").submit();
    }
});
