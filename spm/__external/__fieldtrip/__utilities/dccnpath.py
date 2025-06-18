from mpython import Runtime


def dccnpath(*args, **kwargs):
    """
      DCCNPATH manages the filename and path for test files. It helps to locate and read
        test file from Linux, Windows or macOS computers both inside and outside the DCCN.

        Use as
          filename = dccnpath(filename)
        where the input filename corresponds to the test data on the DCCN cluster and the
        output filename corresponds to the local file including the full path where the
        test data is available.

        The location of the test data on the DCCN cluster is '/project/3031000.02/test' and
        the location of the externally downloadable data is '/project/3031000.02/external/download'
        and the specification of the input filename MUST start with the string '/project/3031000.02'.

        This function will search-and-replace the location on the DCCN cluster by the
        location that applies to your computer. If needed, it will replace '/home' by 'H:',
        '/project' by 'P:' and will replace forward by backward slashes.

        In case you have a local copy of the data, or if you are inside the DCCN and have
        mounted the network drives in a non-standard fashion, you should specify the
        data location using
           global ft_default
           ft_default.dccnpath = '/your/copy';

        If you DO HAVE a local copy of the public data, it should contain a directory
        with the name 'external/download'. The content of the test directory should match
        that on the FieldTrip download server, for example '/your/copy/external/download/ctf'.

        If you DO NOT have a local copy and do not define ft_default.dccnpath manually,
        then this function will automatically try to download the public data to a
        temporary directory.

        See also WHICH, WEBSAVE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/dccnpath.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("dccnpath", *args, **kwargs)
