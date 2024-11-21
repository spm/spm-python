from spm.__wrapper__ import Runtime


def ft_test(*args, **kwargs):
    """
      FT_TEST performs selected FieldTrip test scripts, finds and updates the dependencies of test scripts, finds which high-level FieldTrip functions are not tested, or reports on previous test  
        results from the dashboard database.  
         
        Use as  
          ft_test inventorize        ...  
          ft_test run                ...  
          ft_test find_dependency    ...  
          ft_test update_dependency  ...  
          ft_test untested_functions ...  
          ft_test moxunit_run        ... % this is obsolete  
          ft_test report             ... % this is obsolete  
          ft_test compare            ... % this is obsolete  
          
        ========= INVENTORIZE =========  
          
        To list the tests based on their dependencies, you would do   
          ft_test inventorize  
        to list all test functions, or  
          ft_test inventorize data no  
        to list test functions that don't need any external data to run.  
           
        Additional optional arguments are specified as key-value pairs and can include  
          dependency       = string or cell-array of strings  
          upload           = string, upload test results to the dashboard, can be 'yes' or 'no' (default = 'yes')  
          dccnpath         = string, allow files to be read from the DCCN path, can be 'yes' or 'no' (default is automatic)  
          maxmem           = number (in bytes) or string such as 10GB  
          maxwalltime      = number (in seconds) or string such as HH:MM:SS  
          data             = string or cell-array of strings with 'no', 'public' and/or 'private'  
          sort             = string, can be 'alphabetical', 'walltime', 'mem' or 'random' (default = 'alphabetical')  
          returnerror      = string, whether give an error upon detecting a failed script, can be 'immediate', 'final', 'no' (default = 'no')  
          
        ========= RUN =========  
         
        To execute a test and submit the results to the dashboard database, you would do  
          ft_test run  
        to run all test functions, or  
          ft_test run test_bug46  
        to run a selected test.  
         
        Test functions should not require any input arguments. Any output arguments will  
        not be considered.  
         
        Additional optional arguments are specified as key-value pairs and can include  
          dependency       = string or cell-array of strings  
          upload           = string, upload test results to the dashboard, can be 'yes' or 'no' (default = 'yes')  
          dccnpath         = string, allow files to be read from the DCCN path, can be 'yes' or 'no' (default is automatic)  
          maxmem           = number (in bytes) or string such as 10GB  
          maxwalltime      = number (in seconds) or string such as HH:MM:SS  
          data             = string or cell-array of strings with 'no', 'public' and/or 'private'  
          sort             = string, can be 'alphabetical', 'walltime', 'mem' or 'random' (default = 'alphabetical')  
          returnerror      = string, whether give an error upon detecting a failed script, can be 'immediate', 'final', 'no' (default = 'no')  
          
        ========= FIND_DEPENDENCY =========  
          
        To find on what functions test scripts depend on, you would do  
          ft_test find_dependency test_bug46  
        to find on what functions test_bug46 depends on.  
          
        It outputs:  
          inlist   = Nx1 cell-array, describes the rows and lists the test scripts  
          outlist  = 1xM cell-array, describes the columns and lists the dependencies  
          depmat   = NxM dependency matrix, see below  
          
        The dependency matrix contains the following values:  
         - 0 if there is no dependency  
         - 2 for a direct dependency  
          
        ========= UPDATE_DEPENDENCY =========  
          
        To update the DEPENDENCY header in a specific test script, you would do:  
          ft_test update_dependency test_bug46  
          
        ========= UNTESTED_FUNCTIONS =========  
          
        To find FieldTrip high-level functions not tested by any test scripts,  
        you would do  
          ft_test untested_functions  
         
        ========= MOXUNIT_RUN =========  
         
        To execute tests using MOxUNit, you would do  
          ft_test moxunit_run  
         
        This feature is still experimental, but should support the same  
        options as ft_test run (see above), and in addition:  
          xmloutput         = string, filename for JUnit-like XML file with test  
                              results (used for shippable CI).  
          exclude_if_prefix_equals_failed = string, if set to false (or 'no')  
                              then tests are also run if their filename starts  
                              with 'failed'. If set to true (or 'yes'), which is  
                              the default, then filenames starting with 'failed'  
                              are skipped.  
         
        ========= REPORT =========  
         
        To print a table with the results on screen, you would do  
          ft_test report  
        to show all, or for a specific one  
          ft_test report test_bug46  
         
        Additional query arguments are specified as key-value pairs and can include  
          matlabversion    = string, for example 2016b  
          fieldtripversion = string  
          branch           = string  
          arch             = string, can be glnxa64, maci64. win32 or win64  
          hostname         = string  
          user             = string  
         
        Optionally, you may capture the output to get the results as a Matlab table  
        array, in which case they are not automatically displayed.  
          rslt = ft_test('report', 'fieldtripversion', 'cef3396');  
         
        ========= COMPARE =========  
         
        To print a table comparing different test results, you would do  
          ft_test compare matlabversion     2015b    2016b  
          ft_test compare fieldtripversion  ea3c2b9  314d186  
          ft_test compare arch              glnxa64  win32  
         
        Additional query arguments are specified as key-value pairs and can include  
          matlabversion    = string, for example 2016b  
          fieldtripversion = string  
          branch           = string  
          arch             = string, can be glnxa64, maci64. win32 or win64  
          hostname         = string  
          user             = string  
         
        See also DCCNPATH, FT_VERSION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_test.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_test", *args, **kwargs)
