def azureml_main(frame1):
    import matplotlib
    matplotlib.use('agg')  # Set backend
    
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import statsmodels.graphics.boxplots as sm

    Azure = True
    
## Compute a column with the score accruacy for each row.
    num_rows = frame1.shape[0]
    frame1['Score'] = pd.DataFrame({'Score': ['II'] * num_rows}).astype(str)
    for indx in range(num_rows):
        if((frame1.ix[indx, 'readmi_class'] == 'YES') & (frame1.ix[indx, 'Scored Labels'] == 'YES')): \
          frame1.ix[indx, 'Score'] = 'TP'
        elif((frame1.ix[indx, 'readmi_class'] == 'NO') & (frame1.ix[indx, 'Scored Labels'] == 'NO')): \
          frame1.ix[indx, 'Score'] = 'TN'
        elif((frame1.ix[indx, 'readmi_class'] == 'YES') & (frame1.ix[indx, 'Scored Labels'] == 'NO')): \
          frame1.ix[indx, 'Score'] = 'FN'  
        else: frame1.ix[indx, 'Score'] = 'FP'       
    
## Create a series of bar plots for the various levels of the
## string columns in the data frame by readmi_class. 
    names = list(frame1)
    num_cols = frame1.shape[1]
    err_list = ['TP', 'FP', 'TN', 'FN']
    for indx in range(num_cols):
        if(frame1.ix[:, indx].dtype not in [np.int64, np.int32, np.float64]):             
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            i = 1
            for err in err_list: 
                temp = frame1.ix[frame1.Score == err, indx].value_counts()
                ax = fig.add_subplot(1, 4, i)
                temp.plot(kind = 'bar', ax = ax)
                ax.set_title('Values of \n' + names[indx] + '\n for ' + err)  
                i += 1
                
            if(Azure == True): fig.savefig('bar_' + names[indx] + '.png')    

## Now make some box plots of the columns with numerical values.
    for indx in range(num_cols):
        if(frame1.ix[:, indx].dtype in [np.int64, np.int32, np.float64]):
            fig = plt.figure(figsize = (12,6))
            fig.clf()
            i = 1
            for err in err_list:   
                temp = frame1.ix[frame1.Score == err, indx]
                ax = fig.add_subplot(1, 4, i)
                ax.boxplot(temp.as_matrix())
                ax.set_title('Values of \n' + names[indx] + '\n for ' + err) 
                i += 1
            
            if(Azure == True): fig.savefig('box_' + names[indx] + '.png')

    return frame1
    