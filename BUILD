genrule(
    name = "firmware",
    srcs = [
        "@nickel_menu//file",
        "//KoboRoot",
    ],
    outs = [
        "KoboRoot.tgz",
    ],
    cmd = "cat $(SRCS) > $@",
)
