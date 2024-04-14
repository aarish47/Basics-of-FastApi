# **DELETE request:**

A `DELETE request is an HTTP request method used to request the removal of a resource from a server`. When a client sends a DELETE request to a server, it indicates that it wants the specified resource to be deleted.

`DELETE requests are idempotent, which means that making the same DELETE request multiple times should have the same effect as making it once.` If the resource specified in the DELETE request does not exist on the server, the server typically responds with a status code indicating that the resource was not found.