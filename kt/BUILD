load("@rules_python//python:defs.bzl", "py_binary")
load("//tools:tar.bzl", "easy_tar")

filegroup(
    name = "kt_sources",
    srcs = [
        "//kt/mnt",
    ],
)

easy_tar(
    name = "tar",
    srcs = [
        ":kt_sources",
    ],
    out = "KoboRoot.tgz",
    strip_prefix = "kt",
    visibility = ["//visibility:public"],
)

py_binary(
    name = "kt",
    srcs = [
        ":kt_sources",
    ],
    visibility = ["//visibility:public"],
)
