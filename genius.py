from workflow import web


class APIException(Exception):
    def __init__(self, status, message, url):
        self.status = status
        self.message = message
        self.url = url

        super(APIException, self).__init__(
            "{status} > {message}".format(
                status=self.status,
                message=self.message
            )
        )


class Genius:
    BASE_URL = "https://api.genius.com"

    def __init__(self, access_token):
        assert access_token
        self.access_token = "Bearer {access_token}".format(access_token=access_token)

    def __call__(self, service, **params):
        url = "{base_url}/{service}".format(base_url=self.BASE_URL, service=service)
        params["text_format"] = "plain"

        response = web.get(
            url=url,
            params=params,
            headers={"Authorization": self.access_token}
        ).json()

        meta = response["meta"]

        if meta["status"] != 200:
            raise APIException(meta["status"], meta["message"], url)

        return response["response"]

    def search(self, text, page=1, per_page=20):
        assert text
        assert page > 0
        assert 21 > per_page > 1

        result = self("search", q=text, page=page, per_page=per_page)

        return map(
            lambda hit: hit["result"],
            result.get("hits", [])
        )
