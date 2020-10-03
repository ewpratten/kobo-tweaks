load("//tools:tar.bzl", "concat_files")
load("@rules_pkg//:pkg.bzl", "pkg_tar")

concat_files(
    name = "firmware",
    srcs = [
        ":firmware_bundle",
    ],
    out = "KoboRoot.tgz",
)

pkg_tar(
    name = "firmware_bundle",
    extension = "tgz",
    deps = [
        "//python3",
        "//telnet_server",
        "//kt:tar",
        "@nickel_menu//file",
    ],
)
