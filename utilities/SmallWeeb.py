import requests
import time


class Paths:
    def __init__(self):
        self.api_base = "https://rra.ram.moe"
        self.cdn_base = "https://cdn.ram.moe"

    def __api_base__(self): return self.api_base

    def __cdn_base__(self): return self.cdn_base


class Request:
    def __init__(self, paths):
        self.paths = paths

    def return_image(self):
        return self.paths.cdn_base + "/" + str(self.data['path']).split("/i/")[1]

    def request_send(self, type, is_nsfw: bool = None):
        if not is_nsfw:
            try:
                r = requests.request(url=self.paths.api_base + "/i/r?type=" + type, method="GET")
            except requests.Timeout:
                raise SystemError("Request Timed out <HTTP [408]>")
            except requests.exceptions.TooManyRedirects:
                raise SystemError("ERR_TOO_MANY_REDIRECTS OR HTTP <400> Bad Request")
            except requests.RequestException as e:
                raise SystemError(e)
            return r
        elif isinstance(is_nsfw, bool) and is_nsfw == True:
            try:
                r = requests.request(url=self.paths.api_base + "/i/r?type=" + type + "&nsfw=true", method="GET")
            except requests.Timeout:
                raise SystemError("Request Timed out <HTTP [408]>")
            except requests.exceptions.TooManyRedirects:
                raise SystemError("ERR_TOO_MANY_REDIRECTS OR HTTP <400> Bad Request")
            except requests.RequestException as e:
                raise SystemError(e)
            return r

    def cry(self):
        before = time.monotonic()
        self.data = self.request_send("cry").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def cuddle(self):
        before = time.monotonic()
        self.data = self.request_send("cuddle").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def hug(self):
        before = time.monotonic()
        self.data = self.request_send("hug").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def kiss(self):
        before = time.monotonic()
        self.data = self.request_send("kiss").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def lewd(self):
        before = time.monotonic()
        self.data = self.request_send("lewd").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def lick(self):
        before = time.monotonic()
        self.data = self.request_send("lick").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def nom(self):
        before = time.monotonic()
        self.data = self.request_send("nom").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def nyan(self):
        before = time.monotonic()
        self.data = self.request_send("nyan").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def owo(self):
        before = time.monotonic()
        self.data = self.request_send("owo").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def pat(self):
        before = time.monotonic()
        self.data = self.request_send("pat").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def pout(self):
        before = time.monotonic()
        self.data = self.request_send("pout").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def rem(self):
        before = time.monotonic()
        self.data = self.request_send("rem").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def slap(self):
        before = time.monotonic()
        self.data = self.request_send("slap").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def smug(self):
        before = time.monotonic()
        self.data = self.request_send("smug").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def stare(self):
        before = time.monotonic()
        self.data = self.request_send("stare").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def tickle(self):
        before = time.monotonic()
        self.data = self.request_send("tickle").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def triggered(self):
        before = time.monotonic()
        self.data = self.request_send("triggered").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def nsfw_gtn(self):
        before = time.monotonic()
        self.data = self.request_send("nsfw-gtn", True).json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def potato(self):
        before = time.monotonic()
        self.data = self.request_send("potato").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]

    def kermit(self):
        before = time.monotonic()
        self.data = self.request_send("kermit").json()
        return [self.return_image(), round((time.monotonic() - before) * 1000)]
