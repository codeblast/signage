How do I get two or more images share the same host port?

At the moment, we have three images exporting their HTTP ports:

1. admin: port 8081 (nginx default port 80 mapped to local port 8081)
3. api: port 8080 (flask default)
3. pages: port 80 (nginx default)

Eventually I'd like all HTTP servers to share the same port.
Is this possible with port mapping in docker-compose.yml,
or would the servers need to be configured to serve at the
correct port? I.e. I guess I'd have to change the API's
Flask initialization to `app.run(port=80, host='0.0.0.0')`.

## commands

tonight I had to merge a new file to my previous commit
(before pushing to github of course), so this seems to work:

```bash
git add .
git commit --amend --no-edit
```
