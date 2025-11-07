// Custom JavaScript for Unmanned Vehicle Education Hub

// Add any custom interactive features here

// Example: Track external link clicks (if analytics enabled)
document.addEventListener('DOMContentLoaded', function() {
  // Add target="_blank" to external links
  const links = document.querySelectorAll('a[href^="http"]');
  links.forEach(link => {
    if (!link.href.includes(window.location.hostname)) {
      link.setAttribute('target', '_blank');
      link.setAttribute('rel', 'noopener noreferrer');
    }
  });
});
