"""Tools for working with a tar file"""

def concat_files(name, srcs, out, **kwargs):
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [out],
        cmd = "cat $(SRCS) > $@",
        **kwargs
    )

def easy_tar(name, srcs, out, strip_prefix, **kwargs):
    layers = "/".join([".." for subpath in strip_prefix.split("/")])
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [out],
        cmd = "cd {prefix} && tar --dereference -czvf {layers}/$@ $$(echo \"$(SRCS)\" | sed 's|{prefix}/||g' -)".format(prefix = strip_prefix, layers=layers),
        **kwargs
    )
