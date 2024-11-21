from spm.__wrapper__ import Runtime


def _closedf(*args, **kwargs):
    """
      EDF=closedf(EDF)  
        Opens an EDF File (European Data Format for Biosignals) into MATLAB  
        <A HREF="http://www.medfac.leidenuniv.nl/neurology/knf/kemp/edf.htm">About EDF</A>   
         
        EDF   struct of EDF-Header of a EDF-File  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/closedf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("closedf", *args, **kwargs)
