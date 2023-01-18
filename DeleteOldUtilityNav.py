import re

# Open the HTML file
with open("file.html", "r") as f:
    html = f.read()

# Use regular expressions to search for the div containers
utility_nav_pattern = re.compile(r'<div class="utility-nav">.*?</div>', re.DOTALL)
trusted_site_pattern = re.compile(r'<div id="trusted-site">.*?</div>', re.DOTALL)

# Replace the div containers with an empty string
html = re.sub(utility_nav_pattern, "", html)
html = re.sub(trusted_site_pattern, "", html)

# Write the modified HTML to a new file
with open("file_modified.html", "w") as f:
    f.write(html)
