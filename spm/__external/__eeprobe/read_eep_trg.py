from spm.__wrapper__ import Runtime


def read_eep_trg(*args, **kwargs):
    """
      READ_EEP_TRG reads triggers from an EEProbe *.trg file  
         
        This function returns an Nx1 array with the N triggers  
         
        [trg] = read_eep_trg(filename)  
         
        trg(i).time   ... trigger latency in ms  
        trg(i).offset ... byte offset  
        trg(i).code   ... trigger code (string)  
        trg(i).type   ... numeric value of trg.code  
         
        where i as number between 1 and N (the number of triggers found)  
         
        An EEProbe trigger file is formatted like  
          0.00195312 256  
          0.000     10350  __  
          17.033   2242926   1  
          20.535   2701934   5  
          21.096   2775406  13  
          21.098   2775662   8  
          ...  
        where the first column is the trigger latency in seconds, the second  
        column is the byte offset in the file and the third column is the triggercode.   
        The triggercode can be numeric or a string. The first line of the file contains the  
        sample duration.  
         
        Author: Robert Oostenveld, Aalborg University, Denmark, 11 March 2003  
         
        See also READ_EEP_CNT, READ_EEP_REJ, READ_EEP_AVR  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/eeprobe/read_eep_trg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("read_eep_trg", *args, **kwargs)
