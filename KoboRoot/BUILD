filegroup(
    name = "firmware_update",
    srcs = [
        "//KoboRoot/etc",
        "//KoboRoot/opt",
    ],
)

genrule(
    name = "KoboRoot",
    srcs = [
        ":firmware_update",
    ],
    outs = ["KoboRoot.tgz"],
    cmd = "cd KoboRoot && zip ../$@ $$(echo \"$(SRCS)\" | sed 's|KoboRoot/||g' -)",
    visibility = ["//visibility:public"],
)
