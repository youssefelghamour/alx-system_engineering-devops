# 0x11. What happens when you type google.com in your browser and press Enter

When you type “google.com” into your browser’s address bar and hit Enter, complex but fast processes are set up in the background. Let’s explore the intricacies of this journey from the moment you hit Enter to the point where you see the Google homepage loaded on your screen.

## URL:

The Uniform Resource Locator (URL) is basically the address of the web page you want to visit. In this case, “google.com” acts as the URL. However, in order for your computer to communicate with the web server in Google’s web browser, you need to know the IP address of that server. This is where the Domain Name System (DNS) comes into play.

## DNS requests:

When you type “google.com” into your browser and press Enter, the browser initiates a DNS query to resolve the domain name “google.com” to an IP address. This request is sent to a DNS server, which then returns the corresponding IP address to your browser, allowing it to connect to Google’s servers.

## TCP/IP:

Once your browser obtains the “google.com” IP address through the DNS, it establishes a TCP/IP connection to Google’s web server. TCP/IP, which stands for Transmission Control Protocol/Internet Protocol, is a set of communications protocols that manage the transmission of data over the Internet. This connection forms the standard for sending and receiving data between your browser and the web server.

## Firewall:

With the TCP/IP connection established, data packets traveling between your browser and the web server may encounter firewalls along the way, which act as a barrier between your computer and potentially harmful data from the Internet. Network traffic is monitored and modified based on predefined security rules, ensuring only authorized connections are allowed to go through.

## HTTPS/SSL:

With the IP address in hand, your browser initiates an HTTP (or HTTPS) request to the web server hosting Google’s website. HTTP, short for Hypertext Transfer Protocol, governs the communication between your browser and the server. Through this standardized protocol, requests for web resources are made and responses are received. SSL (Secure Sockets Layer) or TLS (Transport Layer Security) are encryptions that ensure that data, such as login credentials or bank credentials remain private and protected.

## Load-Balancer:

For efficiency and to avoid overloading any one server, many high-traffic websites like Google use load balancers. These devices distribute incoming web traffic across multiple servers, streamlining the user experience and reducing downtime.

## Web Server:

Upon receiving the HTTP request, the web server returns the requested web page, along with the files or other resources needed to display it. These elements include HTML, CSS, JavaScript, images, and more. The server then collects this information as an HTTP response and sends it back to your browser.

## Application Server:

In addition to serving static content, a few web applications may require dynamic processing. In such instances, a software server comes into play. The application server executes server-facet code, which includes PHP or Python scripts, to generate dynamic content based on user interactions or database queries.

## Database:

For websites with dynamic content, interactions with a database server are necessary to retrieve or keep records. The database ensures data integrity and persistence, enabling the website to deliver personalized and up-to-date content to users.


In summary, the process of accessing “google.com” involves a multitude of components working together seamlessly, from DNS resolution and TCP/IP connections to HTTPS encryption, load balancing, web and application servers, firewall protection, and database management. Understanding the roles of these components provides insight into the robust infrastructure powering the internet and the mechanisms safeguarding user data and experiences.
