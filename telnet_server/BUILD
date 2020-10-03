load("//tools:tar.bzl", "easy_tar")

easy_tar(
    name = "telnet_server",
    srcs = [
        "//telnet_server/etc",
        "//telnet_server/opt",
    ],
    out = "KoboRoot.tgz",
    strip_prefix = "telnet_server",
    visibility = ["//visibility:public"],
)
