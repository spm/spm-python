from mpython import Runtime


def _nex_wf(*args, **kwargs):
    """
      nex_wf(filename, varname): Read waveform variable from a .nex file

        [adfreq, n, ts, nf, w] = nex_wf(filename, varname)

        INPUT:
          filename - if empty string, will use File Open dialog
          varname - variable name


        OUTPUT:
          n - number of waveforms
          ts - array of waveform timestamps (in seconds)
          nf - number of data points in each waveform
          w - matrix of waveform a/d values [n nf] (in millivolts)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/nex_wf.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("nex_wf", *args, **kwargs)
