from spm.__wrapper__ import Runtime


def spm_make_standalone(*args, **kwargs):
    """
      Compile SPM as a standalone executable using the MATLAB Compiler  
          https://www.mathworks.com/products/compiler.html  
         
        This will generate a standalone application, which can be run outside  
        MATLAB, and therefore does not require a MATLAB licence.  
         
        On Windows:  
          spm.exe <modality>  
          spm.exe batch <batch.m(at)>  
          spm.exe script script.m  
         
        On Linux/Mac:  
          ./run_spm.sh <MCRroot> <modality>  
          ./run_spm.sh <MCRroot> batch <batch.m(at)>  
          ./run_spm.sh <MCRroot> script script.m  
         
        The first command starts SPM in interactive mode with GUI. The second  
        executes a batch file or starts the Batch Editor if none is provided,  
        while the third command evaluates the content of script.m. Extra  
        command line arguments are available in a cell array variable named  
        "inputs".  
         
        Full list of options is accessible from:  
          ./run_spm.sh <MCRroot> --help  
         
        When deployed, compiled applications will require the MATLAB Runtime:  
          https://www.mathworks.com/products/compiler/matlab-runtime.html  
          
        See https://www.fil.ion.ucl.ac.uk/spm/docs/installation/standalone/ and  
        spm_standalone.m  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_make_standalone.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_make_standalone", *args, **kwargs, nargout=0)
