from spm._runtime import Runtime


def _combineClusters(*args, **kwargs):
    """
      COMBINECLUSTERS is a helper function for FINDCLUSTER. It searches for  
        adjacent clusters in neighbouring channels and combines them.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/combineClusters.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("combineClusters", *args, **kwargs)
