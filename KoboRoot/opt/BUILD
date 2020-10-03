filegroup(
    name = "opt",
    srcs = [
        "afterinit.sh",
        "inetd.conf",
        ":config_guess",
    ],
    visibility = ["//visibility:public"],
)

genrule(
    name = "config_guess",
    srcs = [
        "@config_guess//file",
    ],
    outs = [
        "config.guess",
    ],
    cmd = "cp $< $@",
)
