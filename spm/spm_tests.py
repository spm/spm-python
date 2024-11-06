from spm.__wrapper__ import Runtime


def spm_tests(*args, **kwargs):
    """
      Unit Testing Framework  
        FORMAT results = spm_tests(name,value,...)  
        name,value  - pairs of optional parameter names and values:  
            verbose:   verbosity level of test run progress report [default: 2]  
            display:   display test results [default: false]  
            coverage:  display code coverage [default: false]  
            cobertura: save code coverage results in the Cobertura XML format [default: false]  
            tag:       test tag selector [default: '', ie all tests]  
            tap:       save a Test Anything Protocol (TAP) file [default: false]  
            test:      name of function to test [default: '', ie all tests]  
            class:     class of test 'regression' or 'unit'. [deault: 'unit']  
        results     - TestResult array containing information describing the  
                      result of running the test suite.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_tests.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_tests", *args, **kwargs)
