from spm.__wrapper__ import Runtime


def _ft_test_compare(*args, **kwargs):
    """
      FT_TEST_COMPARE documentation is included inside ft_test documentation.  
          
        See also FT_TEST  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/ft_test_compare.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_test_compare", *args, **kwargs)
