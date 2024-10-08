### [Load Balancing](load_balancing/README.md)
- **Topic:** Load Balancing
- **Summary:** 
  - **Definition:** Distributing incoming network traffic across multiple servers.
  - **Types:**
    - **Hardware Load Balancers:** 
      - **Description:** Dedicated devices designed specifically for load balancing tasks. They offer high performance and reliability but are often expensive.
      - **Example:** F5 Networks, Citrix ADC.
    - **Software Load Balancers:** 
      - **Description:** Software-based solutions that can be installed on standard servers. They are flexible and cost-effective.
      - **Examples:** NGINX, HAProxy.
      - **Python Snippet:**
        ```python
        from flask import Flask, request
        import requests

        app = Flask(__name__)

        servers = ['http://server1', 'http://server2', 'http://server3']
        current_server = 0

        @app.route('/')
        def load_balance():
            global current_server
            response = requests.get(servers[current_server])
            current_server = (current_server + 1) % len(servers)
            return response.content

        if __name__ == '__main__':
            app.run()
        ```
    - **Layer 4 vs. Layer 7 Load Balancers:** 
      - **Layer 4 Load Balancers:** Operate at the transport layer (TCP/UDP). They make routing decisions based on IP address and port.
      - **Layer 7 Load Balancers:** Operate at the application layer (HTTP/HTTPS). They make routing decisions based on content of the request (e.g., URL, headers).
      - **Python Snippet for Layer 7:**
        ```python
        from flask import Flask, request, redirect

        app = Flask(__name__)

        @app.route('/')
        def load_balance():
            if 'api' in request.url:
                return redirect('http://api_server')
            else:
                return redirect('http://web_server')

        if __name__ == '__main__':
            app.run()
        ```
  - **Algorithms:** 
    - **Round-robin:** Distributes requests evenly across all servers in a circular order.
    - **Least connections:** Sends requests to the server with the fewest active connections.
    - **IP hash:** Distributes requests based on the client's IP address.
    - **Python Snippet for Round-robin:**
      ```python
      servers = ['http://server1', 'http://server2', 'http://server3']
      current_server = 0

      def round_robin():
          global current_server
          server = servers[current_server]
          current_server = (current_server + 1) % len(servers)
          return server
      ```
  - **Challenges:** 
    - **Session persistence:** Ensuring that a user's session is consistently routed to the same server.
    - **SSL termination:** Handling SSL encryption/decryption at the load balancer.
    - **Handling failures:** Detecting and rerouting traffic away from failed servers.
  - **Use Cases:** 
    - **Ensuring high availability:** Distributing traffic to prevent any single server from becoming a bottleneck.
    - **Improving performance:** Balancing the load to optimize resource utilization.
    - **Scaling applications:** Adding more servers to handle increased traffic.