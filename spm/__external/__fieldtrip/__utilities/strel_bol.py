from spm._runtime import Runtime


def strel_bol(*args, **kwargs):
    """
      STREL_BOL constructs a 3D sphere with the specified radius  
        that can be used as structural element in 3D image processing  
         
        See STREL, IMERODE, IMDILATE (image processing toolbox)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/strel_bol.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("strel_bol", *args, **kwargs)
