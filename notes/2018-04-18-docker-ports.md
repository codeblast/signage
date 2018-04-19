It seems like the solution to deal with the issue I had
sharing multiple container ports to a single host port
(80) is to use an nginx container that acts as a
"reverse proxy". So it forwards incoming requests
on its port 80 to any number of unique ports used
internally by each container's services.

Next step is to figure out how to use Docker's features
to deal with a "microservice"-type scenario where you
have multiple Docker containers for different parts of
the application. Each container is using/exposing
a different port internally, and externally they all
listen on a shared incoming port 80.

Possibly relevant:

How to Deploy Microservices with Docker
https://linode.com/docs/applications/containers/deploying-microservices-with-docker/

Using Docker in API Gateway and Microservice Development
https://blog.codeship.com/using-docker-in-api-gateway-and-microservice-development/
