workspace(
    name = "kobo_tweaks",
)

## Versions

# https://github.com/pgaskin/NickelMenu/releases
NICKEL_MENU_VERSION = "0.4.0"

## End Versions

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_file")

http_file(
    name = "nickel_menu",
    downloaded_file_path = "KoboRoot.tgz",
    urls = [
        "https://github.com/pgaskin/NickelMenu/releases/download/v{version}/KoboRoot.tgz".format(version = NICKEL_MENU_VERSION),
    ],
)
