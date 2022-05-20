import typing
from furl import furl


class GitDependencyConfig:

    def __init__(
        self,
        scheme: typing.Optional[str] = "https",
        netloc: typing.Optional[str] = "github.com",
        path: typing.Optional[str] = "/",
        username: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        branch: typing.Optional[str] = "main",
    ):
        self.scheme = scheme
        self.netloc = netloc
        self.path = path
        self.username = username
        self.password = password
        self.branch = branch

    def __call__(self, dependency_names: typing.List[str]):
        return [self._get_dependency_url(name) for name in dependency_names]

    def _get_dependency_url(self, dependency_name: str) -> str:
        url = furl(
            scheme=f"git+{self.scheme}",
            netloc=self.netloc,
            path=self.path,
        )
        url.username = self.username
        url.password = self.password
        url.path.segments.append(f"{dependency_name}.git@{self.branch}")
        url.fragment.args["egg"] = dependency_name
        return f"{dependency_name} @ {url}"


