# Warden-OF-theSouth @ IECA
# A random IP address reconnaissance tool

import random
import socket

# Generate a random IP address
ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))

# Print the random IP address
print("Random IP address:", ip_address)

# Perform a reverse DNS lookup to get the domain name associated with the IP address
try:
    domain_name = socket.gethostbyaddr(ip_address)[0]
    print("Domain name:", domain_name)
except socket.herror:
    print("No domain name found for", ip_address)
