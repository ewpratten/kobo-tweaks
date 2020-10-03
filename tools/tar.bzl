"""Tools for working with a tar file"""

def concat_files(name, srcs, out, **kwargs):
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [out],
        cmd = "cat $(SRCS) > $@",
        **kwargs
    )

