import requests

response = requests.get("https://api.github.com")
# print(f"{response}\n")


if response.status_code == 200:
    # response.headers returns a dictionary of response headers.
    print(f"Response Headers: {response.headers}\n")

    # response.encoding returns the encoding used to decode response.content.
    print(f"Response Encoding: {response.encoding}\n")

    # response.elapsed returns a timedelta object with the time elapsed
    # from sending the request to the arrival of the response.
    print(f"Response Elapsed: {response.elapsed}\n")

    # response.close() closes the connection to the server.
    print(f"Response Close: {response.close}\n")

    # response.content returns the content of the response, in bytes.
    print(f"Response Content: {response.content}\n")

    # response.cookies returns a CookieJar object with the cookies sen
    # back from the server.
    print(f"Response Cookies: {response.cookies}\n")

    # response.history returns a list of response objects holding the history
    # of request (url).
    print(f"Response History: {response.history}\n")

    # response.is_permanent_redirect returns True if the response is the
    # permanent redirected url, otherwise False.
    print(f"Response is permanent redirect: {response.is_permanent_redirect}\n")

    # response.is_redirect returns True if the response was redirected,
    # otherwise False.
    print(f"Response is redirect: {response.is_redirect}\n")

    # response.iter_content() iterates over the response.content.
    for v in response.iter_content():
        print(f"Response iter content: {v}\n")

    # esponse.json() returns a JSON object of the result
    # (if the result was written in JSON format, if not it raises an error).
    print(f"Response JSON: {response.json()}\n")

    # 	response.url returns the URL of the response.
    print(f"Response URL: {response.url}\n")

    # response.text returns the content of the response, in unicode.
    print(f"Response text: {response.text}\n")

    # response.status_code returns a number that indicates the status
    # (200 is OK, 404 is Not Found).
    print(f"Response Status Code: {response.status_code}\n")

    # response.request returns the request object that requested this response.
    print(f"Response Request: {response.request}\n")

    # response.reason returns a text corresponding to the status code.
    print(f"Response Reeason: {response.reason}\n")

    # response.raise_for_status() returns an HTTPError object if an error has
    # occurred during the process.
    print(f"Response for Status: {response.raise_for_status()}\n")

    # response.ok returns True if status_code is less than 200, otherwise False.
    print(f"Response OK: {response.ok}\n")

    # 	response.links returns the header links.
    print(f"Response Links: {response.links}\n")

else:
    print(f"Status Code: {response.status_code}")
