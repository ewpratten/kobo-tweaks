filegroup(
    name = "firmware_bundle",
    srcs = [
        "//KoboRoot/etc",
        "//KoboRoot/opt",
    ],
    visibility = ["//visibility:public"],
)

genrule(
    name = "tar",
    srcs = [
        ":firmware_bundle",
    ],
    outs = ["KoboRoot.tgz"],
    cmd = "cd KoboRoot && tar --dereference -czvf ../$@ $$(echo \"$(SRCS)\" | sed 's|KoboRoot/||g' -)",
    visibility = ["//visibility:public"],
)
